.PHONY: extract up down load rebuild browser report clean

PY ?= python3
CYPHER = docker compose exec -T neo4j cypher-shell -u neo4j -p stochgraph

## extract: run stage 0 (mechanical) and write the vault files
extract:
	$(PY) -m stochgraph extract

## up: start Neo4j and wait for it to accept connections
up:
	docker compose up -d
	@printf 'waiting for neo4j'
	@until $(CYPHER) 'RETURN 1' >/dev/null 2>&1; do printf '.'; sleep 2; done; echo ' ready'

down:
	docker compose down

## load: rebuild the graph in Neo4j from the vault files
load:
	$(CYPHER) -f /graph/graph.cypher
	@echo '--- loaded ---'
	@$(CYPHER) 'MATCH (n) RETURN labels(n) AS label, count(*) AS n ORDER BY n DESC;'

## rebuild: extract, then reload — the normal loop
rebuild: extract up load

browser:
	open http://localhost:7474

report:
	$(PY) -m stochgraph report

## clean: drop the derived database (the vault files are untouched)
clean:
	docker compose down -v
	rm -rf .neo4j
