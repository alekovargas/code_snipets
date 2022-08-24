# Python notes 

### OPEN PROCESS CLOSE 

```python 
todos = open('todos.txt', 'a')
print('text to add.', file= todos)
todos.close()
```
Do not forget to close the file, or data could potentially be lose.

Arguments to open:

- 'a': for append 
- 'w': for writing
- 'r': reading ( default)
- 'x': open a new files 

using `with` statment close automatically in your behalf whenever the suit code ends 

```python
with open ('todos.txt') as task:
    for chore in task:
        print(chore, end='')
```
### My-SQL, DB-API

Steps:

- Install the MySQL server.
- Install the MySQL database driver for python.
- Create database and tables.
- create python code to work with database and tables.

#### DB-API

provides an adbtraction layer so programers don't need to worry about the database technology, the idea is the database can be replaced without the need to trow code away.

your code <-> DB-API <-> MySQL connector (python driver) <-> MySQL database






                                                                                                      