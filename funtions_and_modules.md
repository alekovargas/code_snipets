# Python notes 

### Funtions and Modules 



 funtion < module < Standard Library 

* Function describes a reusable chunk of code
* When a function is part of Python class it is known as a method 

```python
def a_descriptive_name(arguments):
    """ A documentation string docstring """
    #code 
    #code 
    #code 
    optional_value = 1
    return optional_value 
```

* when the interpreter encounters a `return` statement in your function suite, the funtion terminates at the return statement and any value provided 
to the `return` statement is passed back to your calling code. 

#### bool

is always false if: evaluate to zero, empty list, empty dictionary, "None" value.

```shell
>>> bool(0)
False

>>> bool(1)
True
```











