The target labelling. 
T: the validation set are included in the target including. 
T: should we have more variation around the default price. 

Resources: 
https://www.pywhy.org/EconML/index.html

KS test

One-hot encoding is a waste of energy for trees.
Really interpret the data, the values. 

28.10

2nd stage: the weights — this is exactly the trick of R-learner. At least you have to have the weight. 

21.10
Manipulating features. 


24.9
K: pricing is only using ESP, but sell intent and others are not used. 
C: For conversion model they are used, treatment model only conversion.
T:  What are the variables in the 2nd stage. 
T: this is a loop we don’t want to get into. People may be able to manipulate it. There are many features are ignorable. Many features I don’t understand why we need them. 
For the conversion model, P59, you may say top15% , 100 Euro change have 1% conversion change. not bad. Chanllages: in experiment, we are changing the margin, which is related to price group. 
Question: whether we are comfortable using the model, maybe in the first version people can not learn, but in the future people may learn. 
C: more features, more complicated causal model. 

T: why cate works but logistic not
T: why b_1 there is negative number? why car demand more for high ESP, why the dvgprice change small. 
The auto 1 focus on below 10k, but we 

K: why purchasing conversion?: 
K: much more difficult to model, you are only able to affect the online action. 
K: then the causal graph is different. 
K: Easier first. 
T: one Euro may be questionable, but should be the ratio. 

Monotonicity: may apply the soft-plus. 

T: the next step is show rate, in between what the inference is unknown, the branch conversion is also unknown. If you want to model conversion, add the intermidiate step. 
Question: if looking at booking, whether we can model the elasicity, now not. Once we understand booking, then next step. 
C: TBD. 
T: the graph would be way more complicated.  I would go with booking first. Once we are convinced it’s working, we can move on. 

in online pricing repo, we have 2 dedicated repo (deal flow, online pricing). multiple epics in one repo?

excluded some potential post-treatment variabes (customer_expected_price). The conversion model drops. 

Log-transform the onsite price. bias correlation in the residual. (negative pricing comming from the outliers, onsite price is clipping to 1 euro). 

validate the model prediction. price variation from experiment data excluding the demand-based data. predict the cate with R-learner. change = onsite price(real) - onsite price(default margin). Then calculate the counter-factual

rank by cate. 
Treatment: price-delta
logistic regression: fit 1st and 2nd rank. 
the coefficient correlates with CATE, to validate the models ability to rank. 

Meeting: 9 Sept
Lemon Detector: 
Question: how to add it to control the effect of the lemon detector.
Introduction: uppricing for cherry, downpricing for lemon. 
Auto1 price, 
default onsite price
other onsite price 
control adjusted pricer price for the demand score. 

besides lemon detector we don’t have any other uplifting
caluculate the OP without on the car demand side, what is the original price, what is the output. 
get more variation beside the 1% of the current. 

R-learner: 
We only have down pricing of the data, you need to argue the effect is symmtrical. empirically elasticity is always low for wkda leads. How do we find the right group to downprice. 
Using the random experiment to see if the model matches the result. 
How to get more variation besides the current 1%
How to set the change: plot different shares of the multiplier group. How much percentage of multipliers acound the scatter are we seeing, how much the margin should we set. 

Change of the default margin multipliers: 
the increased the margin multiplier in all the country. They focus on the PPU, if they are focusing only on PPU instead of the only the convsersion. 
They way they are changing in line with us. We would have range to move the price. The volume would come up eventually. 

 
 


Queation: 
Initially: 
between 10k and 40k hardly any price variation, leading to small changes of the margin hence low influence on conversion. Observed by that the avg. ESP of the optimal solution concentrate on <= 10000 group. 

why are they different?
https://files.slack.com/files-pri/T02CP6RJP-F09D91P3WLA/screenshot_2025-09-03_at_09.29.20.png

https://files.slack.com/files-pri/T02CP6RJP-F09D53WEMNX/screenshot_2025-09-03_at_11.00.09.png
might be wrong.

The new ceilling suggested by Kamaran: 
In the low price range, push the margin ceiling higher. 

Definition clarification: 
Formula_ID
Onsite_price: latest wkda.car_evaluations.onsite_price: Is this the c2B onsite price? Yes
"the onsite price should be calculated at most 1-2 minutes after the A1_price is entered”  

table from Chieri: submitted_on: latest submission?




Task from kamaran: 
distribution of the feature: demand score: the same as in original query?
what is the reevaluation_version
are we now using all data instead of the margin experiment?



Query: 
Problem: User assigned to a different margin group during the resubmission. 
How to identify which experiment the user belong given a resubmission. 

what is the A1_price

negative margin: in wkda_retail_pricing.wkda_pricing_full.the expected sales price is not ESP, what is it? 

Meeting:  2. September
increase the variation of the data is not necessary. 

how to measure the elasticity, how can we test is true. 

C: one only define the elasticity, the second is to see the profit. 

The ordering of the cate: the cate seems to be the same expecct the last group. How can we verify our model. 

C: check the model prediction. 

colibration plot, 5 groups, group cars in the elastic region. We can see 

Meeting: 26. August 
residual is no longer linear, f: any machine learning model
enforce the monotonicity: algorithm does this, nn, treatment is the onsite_price, higher on_p, higher conversion. It depends on residual(output) = actual - first stage. 
residual(output ) independent of the treatment. 

tried the package danial mentioned, the lightgbm not compatible, the causal forest doesn’t have the monotonicity constraint. 

predicting the onsite_price with exp_price 

Customer contents: now the frequency is based on the registration date. The initial customer receives more frequently the email. The returning customers are not considered. 



  1. The SQL: point-in-time market context (queries/agg_train_data_scripts.sql)

  This is more sophisticated than it looks. The trick is avoiding leakage when building aggregate features that should reflect market state as of priced_at. The CTE structure:

  - cluster_data — base table: every priced lead in 7 EU countries, 2023-01-01 to 2024-12-01, with undec_price, post_adj, bought_status, ppu, and days_in_inventory = b2b_deal_datetime - priced_at.
  - dates_t / dates_manuf_t — distinct (priced_at, fuel, price_cat, country [, manufacturer, main_type]) keys — the join surface.
  - inventory_data (line 62): counts other leads where bought_datetime < priced_at < b2b_deal_datetime — i.e. cars that were already in inventory and not yet sold at the moment this lead was priced. This is the correct
   point-in-time inventory and is the kind of thing easy to get wrong (e.g. using "current inventory" would leak the future).
  - inventory_data_manuf does the same but stratified by (manufacturer, main_type).
  - features_7d_data / features_14d_data (line 106, 127): trailing-window means of booking rate, sell speed, and average decorator (AVG(post_adj)) over [priced_at - N days, priced_at - 1 day]. The decorator_last_7d /
  decorator_last_14d features capture the recent rule-based decorator's behavior in the same segment — the policy effectively sees "what was the going adjustment for cars like this".
  - profit_features (line 152): trailing 14-day average/max/min ppu and avg_days_in_inventory. Note the join condition uses b2b_deal_datetime - INTERVAL '15 day' AND b2b_deal_datetime - INTERVAL '1 day' — that uses
  b2b_deal_datetime of comparable leads (when they sold) relative to the current priced_at. This is subtle: at pricing time, you only know ppu for leads that have already sold by priced_at - 1 day. The condition
  dates_t.priced_at BETWEEN other_lead.b2b_deal_datetime - 15d AND other_lead.b2b_deal_datetime - 1d is equivalent to other_lead.b2b_deal_datetime BETWEEN dates_t.priced_at + 1d AND dates_t.priced_at + 15d — that's
  future deals, which would be a leak. Either this is a bug or I'm misreading the intent; worth flagging.

  Final SELECT joins everything back onto features_14d_data c and emits the wide market table, which is then cached as dwh_ds.c2b_agg_data and joined into data_load.ipynb against the per-lead c2b_features_static.

  2. Preprocessor (preprocessing.py) — the quirks

  - Two-stage NaN handling for categoricals (line 81): string columns get "missing", numeric categoricals get the sentinel 99999. Both go through OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan,
   min_frequency=1000) — categories with <1000 occurrences are merged into an "infrequent" bucket. This caps embedding cardinality and prevents per-rare-category overfitting.
  - year_processed hack (line 37): appends last_year + 1 to the encoder's vocabulary so future years at inference time don't blow up — important because the model will be served on data newer than training.
  - email_domain infrequent-fallback (line 89): captures the first infrequent category as a "dummy", then at transform time any unseen email domain is rewritten to that dummy before encoding. This is more careful than
  necessary — OrdinalEncoder with handle_unknown="use_encoded_value" already handles unknowns — so this seems to be defending against a specific failure mode (NaN propagation into the embedding lookup, which expects
  LongTensor).
  - NaN fillers learned from train data (line 138): per-column mean imputation for continuous features, learned once and frozen. This happens before StandardScaler, so imputed means become exactly 0 after scaling —
  i.e. NaN → "average lead" signal.
  - Hard filters in filter_data (line 183): reapp < 1.6, -2700 < ppu < 3070, mileage < 400k, 100 < undec_price < 40k. These drop outliers / corrupted records — but also bound the action support, meaning the policy is
  only trained on a price regime within ~1.6× the stable price. Extrapolating beyond is undefined.
  - fit_target_scaler is commented out in __init__ of the DataModule (line 145). The current code requires it be called manually after construction or it crashes in __scale_target because self.target_scaler is None.
  Notebooks must call it explicitly — fragile.

  3. ReplayDataset — the sold/unsold dance (dataset.py)

  The class is named "Replay" (RL nomenclature) but it's just a labeled supervised dataset. Two flags govern its behavior, and they encode the difference between the three training jobs:

  ┌───────────────────┬───────────────────────────────┬─────────────────┐
  │      Network      │        only_sold_cars         │ balance_samples │
  ├───────────────────┼───────────────────────────────┼─────────────────┤
  │ ConversionNetwork │ False                         │ True (likely)   │
  ├───────────────────┼───────────────────────────────┼─────────────────┤
  │ ProfitNetwork     │ True (or False with NaN mask) │ False           │
  ├───────────────────┼───────────────────────────────┼─────────────────┤
  │ PolicyNetwork     │ False                         │ True or False   │
  └───────────────────┴───────────────────────────────┴─────────────────┘

  - only_sold_cars=True (line 40): hard-filters to ~reward.isna() — used for profit because ppu is undefined for unsold.
  - balance_samples=True (line 46): random undersamples the larger class with random_state=42 to make sold/unsold roughly 50/50. Used for the conversion model when raw conversion rates are imbalanced — but this
  introduces a calibration bias: the model will systematically overestimate P(buy) on the full population unless calibrated post-hoc. The elasticity diagnostic in price_conv_analysis.py would surface this as a constant
   offset across all price bins. Worth checking whether they corrected it.
  - ProfitNetwork doesn't use only_sold_cars — instead it uses valid_mask = ~torch.isnan(rewards) inside the loss (line 61 of profit_model.py). Functionally equivalent, but means the dataloader still feeds in unsold
  examples that the loss silently ignores. That's wasteful (CPU/GPU work on rows that contribute nothing) — but probably intentional so the dataloader configuration can be shared across all three networks.

  4. train_helpers.train_model (train_helpers.py)

  A thin Lightning wrapper:
  - TensorBoard logs to lightning_logs/<model_name>/<timestamp>.
  - EarlyStopping(monitor="val_loss", mode="min"), ModelCheckpoint(save_weights_only=True).
  - Reloads the best checkpoint at the end (line 60) — so the returned network is the best-by-val-loss, not the last-epoch model.
  - Doesn't accept profit_network / conversion_network for the policy case (line 67) — the helper instantiates PolicyNetwork with None for both critics. So in practice the notebooks must bypass this helper for the
  policy training step and instantiate the policy network directly with pretrained critics injected. This is the seam where the "joint" training is actually orchestrated by the notebook (decorator_opt.ipynb), not by
  train_helpers.

  5. feature_importance.py mechanics

  - Uses Captum FeaturePermutation (line 64): shuffles each feature in isolation across the batch and measures the change in model output. Model-agnostic, doesn't require gradients flowing through embeddings (which is
  good — embeddings are non-differentiable w.r.t. categorical index).
  - model_wrapper (line 47) flattens (continuous, action, categorical) into a single tensor so Captum sees a single input. The action is appended to continuous because Captum needs continuous-style inputs to permute
  meaningfully — .long() is reapplied to categoricals inside the wrapper.
  - Hard-codes n=20000 samples (line 23) — fine for stable rankings, won't bog down a notebook.
  - The commented-out analyze_individual_prediction block (line 93–140) shows they prototyped per-sample Integrated Gradients for explainability but didn't keep it. For a future product, this is where per-decision "why
   did we recommend this price?" attribution would live.

  6. profit_model_eval.py — what to take from it

  - Does an inverse target_scaler.transform (line 43) so reported MAE/MSE are in euros, not z-scores. This is the only network whose metrics need un-scaling because conversion is sigmoid-bounded.
  - Reports mean_error (line 80) — i.e. signed bias. If positive, the model under-predicts ppu on average; if negative, over-predicts. For a policy that maximizes ppu · P(buy), even a small consistent bias in ppu
  propagates into systematic over- or under-pricing.
  - No price-stratified evaluation (unlike price_conv_analysis.py for the conversion model). That's a gap: the profit model could be accurate on average but wildly miscalibrated at high or low post_adj, and the policy
  will exploit exactly those regions.

  7. Putting the joint training step together (what decorator_opt.ipynb does)

  Based on the code structure (haven't read the notebook but the API constrains the shape):

  1. Load preprocessed train/val data (DataModule with load_path=...)
  2. Load checkpointed ConversionNetwork.eval() and ProfitNetwork.eval()
  3. Freeze: set requires_grad=False on every param of both critics
  4. policy = PolicyNetwork(..., profit_network=profit_net, conversion_network=conv_net)
  5. trainer.fit(policy, train_loader, val_loader)
     # Each step:
     #   policy outputs action a_pi
     #   profit_net(c, k, a_pi) -> q
     #   conv_net(c, k, a_pi) -> p_buy
     #   loss = -(q * p_buy).mean() + 200 * |a_pi - a_target|
  6. Save policy checkpoint

  The frozen-critics-with-injected-actions setup is deterministic-policy gradient (DPG) in disguise: the policy is differentiated through the critics' frozen weights w.r.t. the action it produces.

  8. Architecture-level critique (what to push back on)

  1. The L1 BC weight of 200 is enormous. With actions in roughly [-0.5, 0.5] and (ppu · p_buy) in z-score × probability ≈ [-2, 2], a 200× L1 will dominate the loss and the policy will barely deviate from
  actions_target. The expected behavior under that weight is "tiny perturbations around the rule-based decorator". That may be exactly the intent (safe deployment), but it should be a tuned hyperparameter, not a magic
  constant.
  2. No off-policy correction. The critics are trained on historical (state, action) pairs from the rule-based decorator. Outside that joint distribution, P(buy) and ppu predictions are extrapolations. The BC
  regularizer mitigates this but doesn't quantify it. Standard fixes — propensity weights, doubly-robust estimators, conservative Q-learning bonuses — are absent.
  3. No counterfactual offline policy evaluation (OPE). Before any A/B test, you'd want an IPS or doubly-robust estimate of the new policy's expected profit lift over the production decorator on held-out logged data.
  Not in this branch.
  4. Conversion model trained with class balancing → uncalibrated probabilities unless Platt-scaled or sigmoid-recalibrated. Multiplying an uncalibrated P(buy) by a regression of ppu gives a biased value estimate; the
  policy then maximizes the biased estimate.
  5. profit_features SQL join window looks like it accidentally references future deals (point 1 above). Worth verifying with whoever wrote it — if it's a leak, all avg_ppu_last_14d features are too optimistic.
  6. Monotonicity in price isn't guaranteed. The commented penalty in ConversionNetwork.shared_step would have enforced ∂P(buy)/∂action ≤ 0. Without it, the policy could find regions where the conversion network
  predicts P(buy) goes up with higher price (overfitting to noise) and exploit them. The elasticity diagnostic is descriptive, not prescriptive — it doesn't stop training from producing a non-monotonic surface.
  7. Two separate networks for ppu and P(buy) vs. one head predicting expected profit directly. The two-network factorization is more interpretable and lets you train ppu only on sold leads, but it doesn't model their
  joint uncertainty. A single multi-task network with two heads sharing a trunk would couple the representations and might be more sample-efficient.
  8. The branch is research-grade. No tests, no serving glue, no model registry integration, no calibration step, no OPE. Treating it as "scientific scaffolding to validate an approach" — which is appropriate — but the
   gap to a production rollout is substantial.