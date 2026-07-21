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



