# Python notes 
### 1) Fundamentals  

- Interpreted not compiled.
- A collection of functions make a module.
- Funtions + modules = standard library 
- Python is batteries included.
- Python standard library https://docs.python.org/3/library/
- Suites are blocks of code.
- : colon, introduce a suite of code that must be indented to the right.
- Else if , in python is elif (Condition) : 
- Everything is an object in python any object can be assigned to a variable.
- Python is sort of object oriented, more precise object–based.
```bash 
>>> python shell
```

### 2) Ordered Data 

Python comes whit four build data structures 

#### 2.2. list
An ordered mutable collection of objects ( similar to an array in other languages)

They are dynamic, can grown and shrink on demand, no need to pre declare the size 
heterogenous: you can mix’n’match objects of different types.
As with an array slots are numbered from zero upwards these are index values.

Example:
```python
prices = []
odds = [1,3,5,7,9]
car = ['BMW', 2020, 2.2 ]
```
Methods:

* len(list_name): To check how many objects use
* .append: To add and object to the end of the list. 
* .remove(): remove an especific ocurrence.
* .pop(): remove object especified by index value.
* .extend: take a second list and add each object to an existing list.
* .insert: insert and object to an existing list, in a expecified index value.

```python
#to copy a list 

list2 = list1.copy()
list2 = list1  # don't, this only reference the same objects in both list

# For loop 
for x in list1:
    print('\t', char)

#slices 
list1[x:y] # x is the start y the end 
list1[:y] # from begin to y 
list1[-7:] # from -7 to the end  

```

#### 2.3 Tuple
An ordered immutable collection of objects 
a tuple is a constant list 

```python
vowels = ( 'a', 'e', 'i', 'o', 'u' )
vowels = ('aeiou' ,) # trailing comma makes is a tuple 
```


#### 2.4 Dictionary 
Is an unordered set of key/value pairs 
are unordered and mutable 
they are two columned multirow data structures, 
can grow or shrink on demand 
the values associated with a key can be any object ( of any type )

The key part of a python dictionary is typically a string 

Example:
```python
person3 = { 'Name': 'Ford Prefect', 
            'Gender':'Male',
            'Occupation': 'Researcher', 
            'Home Planet':'Betelgeuse Seven' }
```
```bash
>>> person3['Name']
'Ford Perfect'
```

insertion order is not maintained. 
Dictionary lookup is fast. ( thanks to a highly optimized hashing algorithm).


#### 2.5 Set 
can grow or shrink on demand.
ensure that none of the objects are duplicated.
support operators, intersection, difference.

```python
vowels = { 'a', 'e', 'i', 'o', 'u' }
vowels = set('aeiou')
```




