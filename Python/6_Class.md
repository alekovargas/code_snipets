# Python notes 

python can support the three paradings of programing: OO, funtional, secuential(imperative)

### Clases and abstracting behavior 

- Using class lets you bundle behavior and state together in an object.
- Use the Camel case capitalized to name class exmaple: CountFromBy().
- Objects share behavior but not state. 
- A method is a funtion defined within a class. 

### class 
all classes automaticalli inherits from class object, 
this provide the funtionality of the standar dunder methods, known as " magic methods".

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
```

To instantiate a class 
```python
p1 = Person('Juan', 10)
```

### Methods 

Methods are declared with `self` as first argument, 

```python
def increase(self)

```

It does not have to be named `self` , you can call it whatever you like, but it has to be the first parameter of any function in the class:

```python
def myfunc(abc):
    print("Hello my name is " + abc.name)
```

### funtion decorators: Wrapping functions 

* Decorator: a technique whereby you can add code to an existing function without having to change any of the existing function’s code.
* You can return a function from a function, as well as send a function to a function.

A function can accept an arbitrary number of arguments if (*arg) is used 

```python
def func(*arg):
    for a ina args:
        print ( a, end= '')
```

A decorator maintains the decorated function’s signature

Your decorator needs to ensure that the function it returns takes the same number and type of arguments as expected by the decorated function.

#### decorator template 

```python 
from functools import wraps

def decorator_name(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    # 1. code executed BEFORE calling the decorated function.
    # 2. Call the decorated function as required, returning its results if needed.
        return funct( *args, **kwargs)
    # 3. Code to execute INSTEAD of calling the decorated function 
  return wrapper
```




### signature of a funtion
The number and type of any function’s arguments is known as its signature





