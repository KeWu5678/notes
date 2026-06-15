### iterator and iterable:

iterable: object capable of returning its member one at a time. 
iterator: 


### generator and generator function 

- special class of iterator
- iterator function & iterator object

A generator is identified by ```yield```. It doesn't return any value but store them as iteratble.  
```python
def gen(num)
    while num > 0: 
        yield num   # indicates it is a generator
        num -= 1
    return  # equivalent to StopIteration. This function returns to a generator. 
            # You can return a value, but it won't be captured by the generator. 
            # It is stored in the Exception of the StopIteration

g = gen(5)
```


The generator doesn't store the current state through a variable, but through the **frame** (函数运行到哪一步)

#### method: gen.send()

## coroutine
### async io

coroutine function 

A cocoutine is defined by ``` async ```. When you call a coroutine function, it returns a coroutine object. It doesn't run the code inside the corountine function. 

How to run a coroutine function: 
1. enter ``` async ``` model, i.e., the event loop

```python asyncio.run(coroutine)```
2. make coroutine to task
    i. with await 
 
 ### numba JIT
@njit(inline = "always")
@njit(parallel = True)
inline="always" means "don't compile this as a standalone function — paste my body into whoever calls me." The function ceases to exist as an independent callable.
parallel=True means "compile this as a standalone function with multi-threaded loop execution."