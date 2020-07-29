# 0x0B. Python - Input/Output

<details><summary>Project Requirements ☑️</summary>

#### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
#### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
</details>

<details><summary>Resources 💡</summary>

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
</details>

#### Learning Objectives 🤓

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to open a file
* How to write text in a file
* How to read the full content of a file 
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string 
* How to convert a JSON string to a Python data structure

---
## Tasks

### [0. Read file](./0-read_file.py)
<details><summary>Instructions</summary><br>

* Write a function that reads a text file (UTF8) and prints it to stdout:
```

```
</details>

### [1. Number of lines](./1-number_of_lines.py)
<details><summary>Instructions</summary><br>

* Write a function that returns the number of lines of a text file:
```

```
</details>

### [2. Read n lines](./2-read_lines.py)
<details><summary>Instructions</summary><br>

* Write a function that reads n lines of a text file (UTF8) and prints it to stdout:
```

```
</details>

### [3. Write to a file](./3-write_file.py)
<details><summary>Instructions</summary><br>

* Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
```

```
</details>

### [4. Append to a file](./4-append_write.py)
<details><summary>Instructions</summary><br>

* Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
```

```
</details>

### [5. To JSON string](./5-to_json_string.py)
<details><summary>Instructions</summary><br>

* Write a function that returns the JSON representation of an object (string):
```

```
</details>

### [6. From JSON string to Object](./6-from_json_string.py)
<details><summary>Instructions</summary><br>

* Write a function that returns an object (Python data structure) represented by a JSON string:
```

```
</details>

### [7. Save Object to a file](./7-save_to_json_file.py)
<details><summary>Instructions</summary><br>

* Write a function that writes an Object to a text file, using a JSON representation:
```

```
</details>

### [8. Create object from a JSON file](./8-load_from_json_file.py)
<details><summary>Instructions</summary><br>

* Write a function that creates an Object from a “JSON file”:
```

```
</details>

### [9. Load, add, save](./9-add_item.py)
<details><summary>Instructions</summary><br>

* Write a script that adds all arguments to a Python list, and then save them to a file:
```

```
</details>

### [10. Class to JSON](./10-class_to_json.py)
<details><summary>Instructions</summary><br>

* Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
```

```
</details>

### [11. Student to JSON](./11-student.py)
<details><summary>Instructions</summary><br>

* Write a class Student that defines a student by:
```

```
</details>

### [12. Student to JSON with filter](./12-student.py)
<details><summary>Instructions</summary><br>

* Write a class Student that defines a student by: (based on 11-student.py)
```

```
</details>

### [13. Student to disk and reload](./13-student.py)
<details><summary>Instructions</summary><br>

* Write a class Student that defines a student by: (based on 12-student.py)
```

```
</details>

### [14. Pascal's Triangle](./14-pascal_triangle.py)
<details><summary>Instructions</summary><br>

* Technical interview preparation:
```

```
</details>

### [15. Search and update](./100-append_after.py)
<details><summary>Instructions</summary><br>

* Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
```

```
</details>

### [16. Log parsing](./101-stats.py)
<details><summary>Instructions</summary><br>

* Write a script that reads stdin line by line and computes metrics:
```

```
</details>

### [17. Hack the VM](./read_write_heap.py)
<details><summary>Instructions</summary><br>

* Write a script that finds a string in the heap of a running process, and replaces it.
```

```
</details>

---

## Author
[Michelle Domingo](https://github.com/michedomingo)
