// Saved views. Paste one into Neo4j Browser (http://localhost:7474).
// Each answers a specific question; none of them draws the whole graph, because
// a few hundred nodes at once is a hairball that tells you nothing.

// --------------------------------------------------------------------------
// (0) LAYER 2 ONLY — the concept graph, statements suppressed.
// This is the default view: what relates to what, and why.
// --------------------------------------------------------------------------
MATCH (a)-[r]->(b)
WHERE (a:Object OR a:Property OR a:Relation)
  AND (b:Object OR b:Property OR b:Relation)
RETURN a, r, b;

// Objects and their relations to other objects only (no predicates).
// Empty until a statement relates two *named* objects — the space inclusions
// L0 subset Lbar(M) subset L(M) are in section 4.2, not chapters 1-3.
MATCH (a:Object)-[r]->(b:Object) RETURN a, r, b;


// --------------------------------------------------------------------------
// (a) Object neighbourhood — "what is L2 related to, and why?"
// Stage 1+ (needs the concept layer). Every edge carries `_via`, the ref of the
// statement that justifies it, so the picture is always traceable to a page.
// --------------------------------------------------------------------------
MATCH path = (o:Object {name: $name})-[r]-(other)
RETURN path;


// --------------------------------------------------------------------------
// (b) Dependency tree — everything a statement rests on, transitively.
// This is the query the whole design exists for, and the one an agent cannot do
// by reading files: it is a frontier walk, not a lookup.
// --------------------------------------------------------------------------
MATCH path = (s:Statement {ref: $ref})-[:CITES*1..6]->(dep:Statement)
RETURN path;

// ... and the blast radius: what fails if this statement is wrong.
MATCH path = (dependent:Statement)-[:CITES*1..6]->(s:Statement {ref: $ref})
RETURN path;


// --------------------------------------------------------------------------
// (c) Chapter concept map — objects and relations only, statements suppressed.
// The revision picture. Stage 1+.
// --------------------------------------------------------------------------
MATCH (o:Object)-[r]-(p)
WHERE (p:Object OR p:Property OR p:Relation)
  AND r._via IS NOT NULL
RETURN o, r, p;

// Restricted to one chapter: `_via` is a statement node id ("s/1.1.4", "ex/1"),
// so the chapter is the head of the referenced statement's ref.
MATCH (s:Statement)<-[]-() WITH s WHERE split(s.ref, '.')[0] = $chapter
MATCH (o:Object)-[r]-(p) WHERE r._via = s.id
RETURN o, r, p;


// --------------------------------------------------------------------------
// (d) Gaps — the view that finds holes in the notes and in your understanding.
// --------------------------------------------------------------------------

// Statements that cite nothing and are cited by nothing: either genuinely
// self-contained, or their dependencies are stated in prose the extractor could
// not see. Worth reading down this list.
MATCH (s:Statement)
WHERE NOT (s)-[:CITES]->() AND NOT ()-[:CITES]->(s)
RETURN s.ref AS ref, s._kind AS kind, s._page AS page, s.statement_text AS text
ORDER BY s._page;

// Results asserted but not proved here — sound to cite, unsupported in these
// notes. Includes every exercise.
MATCH (s:Statement)
WHERE s.proved_here = false AND coalesce(s._out_of_scope, false) = false
RETURN s.ref AS ref, s._kind AS kind, s._page AS page
ORDER BY s._page;

// Forward references out of the extracted range — what chapters 1-3 lean on
// from chapters 4-6.
MATCH (a:Statement)-[:CITES]->(b:Statement {_out_of_scope: true})
RETURN b.ref AS target, collect(a.ref) AS cited_by
ORDER BY target;

// Load-bearing results: most depended upon, transitively.
MATCH (dependent:Statement)-[:CITES*1..6]->(s:Statement)
RETURN s.ref AS ref, s._kind AS kind, count(DISTINCT dependent) AS dependents
ORDER BY dependents DESC LIMIT 20;
