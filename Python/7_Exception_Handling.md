# Python notes 

python can support the three paradings of programing: OO, funtional, secuential(imperative)

### Exception Handling


```python 
try: 
  with open('myfile.txt') as fh:
    file_data = fh.read()
  print(file_data)
except FileNotFoundError:
  print('file is missing.')
except PermissionError:
  print('this is not allowed')
except: 
  print('Some other error occurred.')
```
