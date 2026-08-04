"""Stage 1 pass over section 1.1 — the first concept extraction.

Run once to seed the registry and annotations, then read back with
``python -m stochgraph check``. Kept in the repo as the worked example of what a
stage-1 pass produces; later sections are extracted the same way, against the
registry this one establishes.
"""

from pathlib import Path

from stochgraph.annotate import Annotation, Conclusion, save_annotation
from stochgraph.concepts import Concept, Registry

GRAPH = Path(__file__).resolve().parents[2] / "Math" / "stochana" / "graph"

C = [
    # --- objects ---------------------------------------------------------
    Concept("obj/stochastic-process", "Object", "stochastic process",
            refine="Process", symbol="X", defined_by="s/1.1.1"),
    Concept("obj/probability-space", "Object", "probability space",
            refine="Space", symbol="(Ω, F, P)"),
    Concept("obj/filtration", "Object", "filtration", refine="SigmaField",
            symbol="(F_t)", defined_by="s/1.1.6"),
    Concept("obj/filtered-probability-space", "Object", "filtered probability space",
            refine="Space", aliases=["stochastic basis"], defined_by="s/1.1.6"),
    Concept("obj/progressive-sigma-field", "Object", "progressive σ-field",
            refine="SigmaField", defined_by="s/1.1.7"),
    Concept("obj/predictable-sigma-field", "Object", "predictable σ-field",
            refine="SigmaField", defined_by="s/1.1.7"),
    Concept("obj/brownian-motion", "Object", "Brownian motion", refine="Process",
            symbol="B", aliases=["standard Brownian motion", "BM"],
            defined_by="s/1.1.12"),
    Concept("obj/poisson-process", "Object", "Poisson process", refine="Process",
            symbol="N", defined_by="s/1.1.13"),
    Concept("obj/levy-process", "Object", "Lévy process", refine="Process",
            defined_by="s/1.1.13"),

    # --- properties (arity 1) --------------------------------------------
    Concept("prop/measurable", "Property", "measurable", arity=1,
            defined_by="s/1.1.5"),
    Concept("prop/progressively-measurable", "Property", "progressively measurable",
            arity=1, defined_by="s/1.1.7"),
    Concept("prop/adapted", "Property", "adapted", arity=1, defined_by="s/1.1.7"),
    Concept("prop/continuous", "Property", "continuous", arity=1,
            aliases=["all trajectories continuous"], defined_by="s/1.1.11"),
    Concept("prop/left-continuous-paths", "Property", "left-continuous paths",
            arity=1,
            aliases=["all trajectories are left-continuous", "left-continuous"]),
    Concept("prop/right-continuous-paths", "Property", "right-continuous paths",
            arity=1,
            aliases=["all trajectories are right-continuous", "right-continuous"]),
    Concept("prop/cadlag", "Property", "càdlàg", arity=1,
            aliases=["right-continuous with left limits"], defined_by="s/1.1.11"),
    Concept("prop/caglad", "Property", "càglàd", arity=1,
            aliases=["left-continuous with right limits"], defined_by="s/1.1.11"),
    Concept("prop/independent-increments", "Property", "independent increments",
            arity=1, defined_by="s/1.1.12"),
    Concept("prop/stationary-increments", "Property", "stationary increments",
            arity=1, defined_by="s/1.1.12"),
    Concept("prop/poisson-increments", "Property", "Poisson distributed increments",
            arity=1, defined_by="s/1.1.13"),
    Concept("prop/stochastically-continuous", "Property", "stochastically continuous",
            arity=1, defined_by="s/1.1.13"),
    Concept("prop/starts-at-zero", "Property", "starts in zero", arity=1),
    Concept("prop/almost-surely-continuous-paths", "Property",
            "almost surely continuous sample paths", arity=1),

    # --- relations (arity 2) ---------------------------------------------
    Concept("rel/indistinguishable", "Relation", "indistinguishable", arity=2,
            defined_by="s/1.1.1"),
    Concept("rel/modification", "Relation", "modification", arity=2,
            defined_by="s/1.1.1"),
    Concept("rel/same-fdd", "Relation", "same finite dimensional distributions",
            arity=2, aliases=["same fdd"], defined_by="s/1.1.2"),
]

A = [
    Annotation("s/1.1.1", about=["obj/stochastic-process"],
               defines=["rel/indistinguishable", "rel/modification"]),
    Annotation("s/1.1.2", about=["obj/stochastic-process"],
               defines=["rel/same-fdd"]),
    # Two independent implications in one statement — hence per-conclusion `given`.
    Annotation("s/1.1.3", concludes=[
        Conclusion("rel/modification", given=["rel/indistinguishable"]),
        Conclusion("rel/same-fdd", given=["rel/modification"]),
    ]),
    # The converses fail. Negation is first-class: these become NOT_IMPLIES edges,
    # without which an agent could derive the converse from 1.1.3 alone.
    Annotation("ex/1", concludes=[
        Conclusion("rel/indistinguishable", given=["rel/modification"], negated=True),
        Conclusion("rel/modification", given=["rel/same-fdd"], negated=True),
    ], note="Converse of 1.1.3, both parts."),
    # "left-continuous (or right-continuous)" is a disjunction, recorded as two
    # implications rather than invented as a third property.
    Annotation("s/1.1.4", concludes=[
        Conclusion("rel/indistinguishable",
                   given=["rel/modification", "prop/left-continuous-paths"]),
        Conclusion("rel/indistinguishable",
                   given=["rel/modification", "prop/right-continuous-paths"]),
    ]),
    Annotation("s/1.1.5", about=["obj/stochastic-process", "obj/probability-space"],
               defines=["prop/measurable"]),
    Annotation("s/1.1.6", defines=["obj/filtration", "obj/filtered-probability-space"]),
    Annotation("s/1.1.7", about=["obj/filtered-probability-space"],
               defines=["prop/progressively-measurable", "prop/adapted",
                        "obj/progressive-sigma-field", "obj/predictable-sigma-field"]),
    Annotation("ex/2", about=["obj/progressive-sigma-field",
                              "obj/predictable-sigma-field"]),
    Annotation("ex/3", requires=["prop/progressively-measurable"],
               concludes=[Conclusion("prop/progressively-measurable")],
               note="The running integral of a progressive process is progressive; "
                    "the hypothesis and conclusion share a predicate, so no edge "
                    "is projected."),
    Annotation("s/1.1.8", requires=["prop/progressively-measurable"], concludes=[
        Conclusion("prop/measurable"),
        Conclusion("prop/adapted"),
    ]),
    Annotation("ex/4", concludes=[
        Conclusion("prop/progressively-measurable", given=["prop/measurable"],
                   negated=True),
        Conclusion("prop/measurable", given=["prop/adapted"], negated=True),
    ], note="Converse of 1.1.8, both parts."),
    Annotation("s/1.1.9", requires=["prop/adapted", "prop/measurable"],
               about=["obj/stochastic-process"],
               note="Conclusion is the *existence* of a progressively measurable "
                    "modification. Existential conclusions have no encoding yet — "
                    "left unprojected rather than approximated."),
    Annotation("s/1.1.10", concludes=[
        Conclusion("prop/progressively-measurable",
                   given=["prop/adapted", "prop/right-continuous-paths"]),
        Conclusion("prop/progressively-measurable",
                   given=["prop/adapted", "prop/left-continuous-paths"]),
    ]),
    Annotation("s/1.1.11", about=["obj/stochastic-process"],
               defines=["prop/continuous", "prop/cadlag", "prop/caglad"]),
    Annotation("ex/5", note="Property of càdlàg functions, not of a process."),
    # Bound conclusions: these name an object, so they project to HAS_PROPERTY
    # edges and are what populates the object layer.
    Annotation("s/1.1.12", about=["obj/brownian-motion"],
               defines=["obj/brownian-motion", "prop/independent-increments",
                        "prop/stationary-increments"],
               concludes=[
                   Conclusion("prop/starts-at-zero", args=["obj/brownian-motion"]),
                   Conclusion("prop/independent-increments",
                              args=["obj/brownian-motion"]),
                   Conclusion("prop/stationary-increments",
                              args=["obj/brownian-motion"]),
                   Conclusion("prop/almost-surely-continuous-paths",
                              args=["obj/brownian-motion"]),
               ]),
    Annotation("s/1.1.13", about=["obj/poisson-process", "obj/levy-process"],
               defines=["obj/poisson-process", "obj/levy-process",
                        "prop/poisson-increments", "prop/stochastically-continuous"],
               concludes=[
                   Conclusion("prop/starts-at-zero", args=["obj/poisson-process"]),
                   Conclusion("prop/cadlag", args=["obj/poisson-process"]),
                   Conclusion("prop/independent-increments",
                              args=["obj/poisson-process"]),
                   Conclusion("prop/poisson-increments", args=["obj/poisson-process"]),
                   Conclusion("prop/starts-at-zero", args=["obj/levy-process"]),
                   Conclusion("prop/cadlag", args=["obj/levy-process"]),
                   Conclusion("prop/independent-increments", args=["obj/levy-process"]),
                   Conclusion("prop/stationary-increments", args=["obj/levy-process"]),
                   Conclusion("prop/stochastically-continuous",
                              args=["obj/levy-process"]),
               ]),
]


def main() -> int:
    registry = Registry.load(GRAPH)
    problems = []
    for concept in C:
        # Idempotent: re-running a pass must be a no-op, not an error. Only a
        # genuine conflict (same id, different content) is worth reporting.
        existing = registry.get(concept.id)
        if existing is not None:
            if existing != concept:
                problems.append(f"{concept.id}: conflicts with the registered entry")
            continue
        problems.extend(registry.accept(concept))
    if problems:
        for problem in problems:
            print("  ", problem)
        return 1
    registry.save(GRAPH)
    for annotation in A:
        save_annotation(annotation, GRAPH)
    print(f"seeded {len(C)} concepts, {len(A)} annotations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
