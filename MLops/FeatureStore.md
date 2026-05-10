# Feature Store

## Why Use a Feature Store?

### 1. Schema Unification
Define a feature once; all consumers see the same names and types.

### 2. Online / Offline Parity
The same feature definition feeds both:
- the **offline store** (Athena / S3) — what training reads
- the **online store** (Redis-backed) — what inference reads

So the column you trained on is provably the column you serve on. No more *"training pipeline computed `mileage / 1000` but inference forgot to"* bugs.

### 3. Low-Latency Serving
At inference time you do a key lookup:

```python
get_record(feature_group, car_id)
```

Sub-100ms — instead of running the original SQL joins or making 12 REST calls (hundreds of ms each). The expensive computation happens **once**, when the event fires, not at every prediction.

### 4. Pre-Computation / Freshness Contract
The feature pipeline runs once per event (e.g., when a self-eval is submitted) and writes to both stores with a TTL. The model never recomputes — it reads a snapshot.

### 5. Point-in-Time Correctness for Training
The offline store keeps history, so you can train on *"what did we know about this car at the moment of evaluation"* — avoiding leakage from later updates.

---

## Old vs. New Data-Getter Path

| Aspect | Old method (`DataGetterDB` from refurbishment) | `ds-datagetter` (new path) |
| --- | --- | --- |
| **Library** | Hand-rolled `iopy/db_data_getter.py` per service | `from ds_datagetter import DataGetter` (versioned, shared) |
| **Connection** | `dscred.DBConnect.getRedshiftConnection()` | `dg.redshift` — auto-resolves creds from your AWS identity → Secrets Manager (`prod/DS/<user>/redshift`) |
| **Subquery / params** | Sent as a string to DB | Native `"subquery"` placeholder, but `{idselect_query}` works as a normal string parameter — the rendered SQL is just substituted in |
| **Feature-store table refs** | N/A (raw `wkda.*` tables only) | `{{table_name}}` (double braces) → resolved via feature-store API. Optional. Your queries use raw `wkda.*` so you don't need this |
| **Temp table + main query in one string** | Sent as a single `pd.read_sql(query, conn)` | `RedshiftClient` auto-splits on `;` — runs the temp-table setup with a cursor, then the main query with `pd.read_sql`. Works transparently for your `CREATE TEMP TABLE idselect ...; ...main SQL...` pattern |
| **S3 unload** | Custom `s3_handler.py` per service | `dg.redshift.unload(bucket_path)` built in |
| **Async / online store** | Not supported | `dg.online.aget_record(...)`, `dg.api.pricing.get(...)` (only relevant if you later add inference) |
| **Logging** | `loguru` per service | `ds_logging` (structured — what you saw in the smoke-test output) |
| **Local setup** | DB env vars + `dscred` | AWS SSO + VPN. Already proved working with the smoke test |
