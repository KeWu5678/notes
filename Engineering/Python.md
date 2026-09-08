## DATA STRUCTURE. 
Static analysis cannot rely on the runtime value
### Dataclass
- why the dataclass?
A class already fullfills the purpose of the object-oriented programming. Methods and attributes are assigned to the calss. The dataclass is motivated by the "value" nature

- ```__init__```
- ```__eq___```: compare the value
- ```_repr___```: print the value 

### Pydantic (BaseModel)

| Aspect             | Pydantic `BaseModel`                                  | Python `dataclass`                          |
| ------------------ | ----------------------------------------------------- | ------------------------------------------- |
| Main purpose       | Validate and store structured data                    | Store structured data with less boilerplate |
| Runtime validation | Yes                                                   | No; type hints are not enforced             |
| Invalid input      | Raises `ValidationError`                              | Usually accepts it unchanged                |
| Type conversion    | Can convert compatible values, such as `"42"` to `42` | Does not convert values automatically       |
| Serialization      | `model_dump()` and `model_dump_json()`                | `asdict()` or custom code                   |
| Dependency         | Third-party `pydantic` package                        | Python standard library                     |
| Overhead           | Higher because it validates data                      | Lower                                       |
| Best for           | APIs, forms, configuration, and external input        | Trusted internal data                       |

**Rule of thumb:** use a `dataclass` for trusted input and `BaseModel` when input must be checked or converted.


## iterator and iterable: 

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

# SYSTEM CONTROL
## command line
```bash 
- phython -m: execute the module as a programm (the main is executed)
```

## packages
```python
1. sys
- sys.exit()
- sys.argv: List(str)   # return the list of the argument. 
```

