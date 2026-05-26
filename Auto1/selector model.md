## model

### training
X: online retail flagged cars
F: cars c2b fallbacked at the branch
C: cars purchased at the branch

The model predicts the probability of a online retail flagged car that is fallbacked onsite and bought. 
p(X) := P(F ∩ C | X) = P(C | F ∩ X) P (F | X)

For P(F|X) we use a modified selector model to predict the cars that is rejected for retail onsite
For P(C|F ∩ X) we use the bookinghero model, with the training set as the onsite fallbacked cars, and predict the conversion. 

I avoided to predict P(C| X, F = 1) and compare it with P(C | X, F = 0) to avoid dealing with confounder and counterfactuals. 

### Inference
In the inference stage we make the decision based on the following 2 criteria. 

1. car is likely to be fallbacked after:
P(F|X) > threshold

2. the conversion p is not within an acceptable range: 



### Test the model


### features
1. customer information
2. conversion at booking vs. conversion at branch
#### added booking hero features


#### price elasticity
abs_margin
active_dashboard_lights
appointment_first_book_datetime
appointment_start_datetime
assumption_funnel_flag
bought
branch_id
branch_lat
branch_lng
CLASS
created_on
crossborder
current_retail_flag
dat_ecode
email
evaluation_end_datetime
evaluation_start_datetime
exp_customer_price
exp_sales_price
experiment
experiment_bucket
exterior_color
exterior_condition
formula_id
has_scratches
hash
height
interior_condition
internal_submission
key_count
laser_flag
last_exp_sales_price_datetime
last_onsite_datetime
last_submitted_on
lead_creation_datetime
lead_lat
lead_lng
lead_zipcode
length
margin_formula
margin_multiplier
marketing_channel
new_car_price
onsite_price
phone_provided
ratio
retail_priced
risk_free
sell_date
*** sellpoint ***
selltype
source_id
stable_price
*** submission_count ***
test_drives
typhoon_ds_elig_flag
typhoon_exp_elig_flag
vehicle_id
vin
width
zip_mandatory




#### margin
****Auto1 platform****: 
margin = ESP - price 
****Autohero platform****:  
margin = retail price - (exp_retail_sales_price + target_margin) - total_retail_cost + tax advantage + autohero_bonus

Cost: 
'inbound-logistic',
'special-tax',
'optical-repair',
'mechanical-repair',
'maintenance-repair',
'extra-work',
'technical-inspection',
'de-registration',
'exit-check-cleaning',
'workshop-handling',
'refueling',
'photos',
'legal-warranty-and-non-warranty-claims',
'legal-registration',
'interior-cleaning',
'exterior-cleaning',
'exit-check-polishing',
'refurbishment'   -- only filled for retail autopriced cars
