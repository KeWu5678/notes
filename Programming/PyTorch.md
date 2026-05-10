# Optimizer
## torch.optim (Optimizer)
— method: step() or step(closure)

### Procedures
#### standard procedure
for 1st order method like Adam
```python
	optimizer.zero_grad():	# clear the gradient.
	loss.backward(): 		# backward propogation.
	optimizer.step(): 		# update the iterate.
```
#### advanced procedure
```python	
	closure()
		opt.zero_grad()		# A closure function is needed to 
		obj = obj()			# compute the loss
		obj.backward()		# backward propogation
		return obj			# return to the loss 
	
	step(closure)			# update the internal history: x_(k + 1) = x_k + ...
```

The model object: 
— self.net(): contrains architectures, forward logic submodels, methods like train() and eval(). 

# Network
## torch.nn (The Network)
### torch.nn.functional
#### torch.nn.functional.linear(input, weights, bias)
--It is the backbone to construct the kernel of the network. It separate all the linearity information. 
--It returns a matrix with the row as the observation and column as the neuron. 
--Any further nonlinearity can be applied with activation() or pointwise operation like ** p. 

### torch.nn.Module

### torch.nn.Embedding


# Data
## dataset and dataloader


## object: Tensor

### matrix multiplication 
reshape(*): 
reshape preserves the tensor’s linear (1D) order of elements as they appear in memory (or in the implied iteration order)
-1: infer it from the context. 
- reshape (-1): row/vector conversion 
- reshape (()): convert to scalar 

# Lightning