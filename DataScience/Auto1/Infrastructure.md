
## Feature Store
13.OCt. 

Why:
reimplementing process for same features: 
maintainance 
API - real-time limitations 
Consistency 

Resuable features: 
reduce the load: simplify the data fetching 
monitor the features
event-driven and real-time recommendation. 


What
centrolized repository of ML features. 

Retrieving, catalog, 
online store: key value store - online key value lookup - low latency  (DynanoDB)
offline store: data lake.  - exploration, training, SQL query. (S3)
same data, different data type. 

Terminology: 
Feature
Feature Group
Event time name 
Record
a record identifier and event time uniquely identify a record. 

Online store keeps only one record per event name identifier. Offline keeps all 

Integration: 
not all features can be stored in the feature store. 







we don’t loss any data 


Retrival:
table (feature group) exists in both online and offlien store, 
vector service: embedding. 

Concept 
Workflow
Use case



Discussion
offline store not (S3 + Athena) after ingesting, dating is not automatic and costly. 
Offline (Redshift + dbt(features, creating new table in redshift). dbt provides cdc (change data capture) and (but can not be done in python but only in dbt)

Kevin Graham
11:35 AM
SQS used as the DLQ:
No hard limit on the total number of messages (effectively unlimited queue length).
Max message payload: 256 KB (body + attributes). For larger payloads, store the data in S3 and put a pointer in the SQS message (or use the SQS Extended Client).
Message retention: configurable from 1 minute up to 14 days.
Ling-Chia Chen
11:47 AM
Using offline feature store also has the benefit that there is no mapping required anymore between inference and retraining. This is one of the main benefit for feature store to simplify data processing

Is it enough to look at key trigger or refresh on all change. 

Feast and Teclon 
granalarity of feature group: around entity. time-driven.  (entity centric and event centric) 
Buynow features. 

In repricing, how do we do it: 
same procesedure: datagetter api 
how do we design feature group?


Qa-testing prod-train
Recently. Mlflow: api not available in qa account
Now: in Jenkins pipline, introduce a slave. Use ml-flow to download the model. 





## Qeury Score:
Query catalog: centralized catalog

Why: redshift default catalog not easy access, limited memory time. 
reportinator. 

What: qualify the query performance. 

Metric:
Score: 1-100
hard limit: 
	nested loop join rows >= 1M
	execution time: 
	spectrum span size: 
	disk
	CPU time
soft-score
Weighs * percentile band
CPU 40: pt
execution time: 40 pt
nested loop join rows: 10 pt
blocks read from disk: 10 pt
the percentile is defined with the 11.2024: because that time we have no limits for queries. 
redash to redasd, reportinator to reportinator. 

QMR: is in charge of killling the query. 

speeding, block, 

the query from the customers. 

Why: 
check the impact on the system. QMR only tells you what rules you break (the first rule). 

how to access the score: 
In reddish. 

Reportinator: 
automated tool to generate the report of the query. 
Scored before executing on the reportinator, saving the execution time to generate the report. 

Django. 

Use case: 

If the business case has to break a hard rule, how do we do it?
the query score is not killing anything right now. 
percentile setting should be fine. 
if it breaks QMR, it’s highly likely it should be optimized.

what is the percentile of the reprotinator queries?
not sure: 
Reportinator: row counts, 1M, execution time 5min