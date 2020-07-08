# 0x00. Python - Hello, World

<details><summary>Project Requirements ☑️</summary>

#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- he first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
#### Shell Scripts
- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable
#### C Scripts
- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 14.04 LTS
- Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded
</details>

<details><summary>Resources 💡</summary>

* [The Python tutorial (Read the first three chapters)](https://docs.python.org/3/tutorial/index.html)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python (Read up until “3.1.2. Strings” included)](https://docs.python.org/3/tutorial/introduction.html)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program with Python](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
</details>

#### Learning Objectives 🤓

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using print
* How to use strings
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check your code with PEP 8

---
## Tasks

### [0. Run Python file](./0-run)
<details><summary>Instructions</summary>

* Write a Shell script that runs a Python script.
* The Python file name will be saved in the environment variable $PYFILE
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Holberton School
guillaume@ubuntu:~/py/0x00$ 
```
</details>

### [1. Run inline](./1-run_inline)
<details><summary>Instructions</summary>

* Write a Shell script that runs Python code.
* The Python code will be saved in the environment variable $PYCODE
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Holberton School: 98
guillaume@ubuntu:~/py/0x00$ 
```
</details>

### [2. Hello, print](./2-print.py)
<details><summary>Instructions</summary>

* Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
</details>

### [3. Print integer](./3-print_number.py)
<details><summary>Instructions</summary>

* Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
> C is strongly typed… not in Python! The variable number can be assigned to a string, a float, a bool etc… Forcing the type during a string format ("...".format(...)) is a way to control the type of a variable
</details>

### [4. Print float](./4-print_float.py)
<details><summary>Instructions</summary>

* Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
```

```
</details>

### [5. Print string](./5-print_string.py)
<details><summary>Instructions</summary>

* Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
```

```
</details>

### [6. Play with strings](./6-concat.py)
<details><summary>Instructions</summary>

* Complete this source code to print Welcome to Holberton School!
```

```
</details>

### [7. Copy - Cut - Paste](./7-edges.py)
<details><summary>Instructions</summary>

* Complete this source code
```

```
</details>

### [8. Create a new sentence](./8-concat_edges.py)
<details><summary>Instructions</summary>

* Complete this source code to print object-oriented programming with Python, followed by a new line.
```

```
</details>

### [9. Easter Egg](./9-easter_egg.py)
<details><summary>Instructions</summary>

* Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
```

```
</details>

### [10. Linked list cycle](./10-check_cycle.c)
<details><summary>Instructions</summary>

* Technical interview preparation:
```

```
</details>

---

## Author
[Michelle Domingo](https://github.com/michedomingo)
