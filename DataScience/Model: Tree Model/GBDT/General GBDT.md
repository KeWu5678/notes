## Algorithm

## Metrics

- Feature Contribution (SHAP value): This is calulated after the the training by weight:

  phi_j = sum over all S ⊆ F \ {j} of:                                                                                                               
                                                                                                                                                     
      |S|! * (|F| - |S| - 1)!                                                                                                                        
      -------------------------  *  [ f(S ∪ {j}) - f(S) ]                                                                                            
                |F|!                                                                                                                                 
                                                                                                                                                     
  Where:                                                                                                                                             
  - phi_j is the Shapley value for feature j                                                                                                       
  - F is the full set of features                                                                                                                    
  - S is a subset of features not including j
  - f(S) is the model prediction using feature set S                                                                                                 
  - |S| and |F| are the sizes of sets S and F 


- Gain: SSE increase of the gradient (taking over the predictions) of the realized split: This is calculated during the training

