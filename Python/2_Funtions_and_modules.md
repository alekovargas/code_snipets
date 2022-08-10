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
    optional_value = arguments 
    return optional_value 
```

* When the interpreter encounters a `return` statement in your function suite, the funtion terminates at the return statement and any value provided 
to the `return` statement is passed back to your calling code.
* The only way to return multiple values, is to package the multiple values in a single data structure and return it. 

#### Annotations ( type hints)
They provide details about your function, but they o not imply another behavior such as type checking. 


```python
def a_descriptive_name(arguments:str) -> str:
    """ A documentation string docstring , input type string, return is a string """
    #code 
    #code 
    #code 
    optional_value = arguments 
    return optional_value
```
#### functions with default values 

```python
def a_descriptive_name(argument1:str, argument2:str= 'hola' ) -> set:
    optional_value = argument2
    nothing = argument1 
    return set(optional_value)

```
* positional assignment: the method parameters are assigned based on their position
* keyword assignments: in this carse funtion/method arguments are referd by the argument name: 
```python
    a_descriptive_name(argument2='ab', argument1='cd')
```

#### bool

Is always false if: evaluate to zero, empty list, empty dictionary, "None" value.

```shell
>>> bool(0)
False

>>> bool(1)
True
```

### How to share functions 

Module in python is any file that contains funtions,
make modules available to your program just using `import` statement  

There are three main location where your interpreter searches for modules:
- Your current working directory. ( Interpreter look it first )
- Your interpreter's site package locations.
- The standard library location.

#### By object reference call semantic 

The interpreter looks at the type of the value referred to by the object reference, so if the 
variable refers:

- A mutable value: Then call by reference semantics apply ( list, dictionaries, sets)
- An immutable value: then Call by value semantics apply ( string, integers, tuples)


#### \_\_name__ "dunder name"
The __name__ is maintained by the python interpreter and,  when used anywhere within
your program’s code, is set to the name of the currently active module








