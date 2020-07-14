# 0x0C. Python - Almost a circle

<details><summary>Project Requirements ☑️</summary>
...
</details>

<details><summary>Resources 💡</summary>
...
</details>

#### Learning Objectives 🤓

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

### [0. If it's not tested it doesn't work](./tests/)
<details><summary>Instructions</summary>

* All your files, classes and methods must be unit tested and be PEP 8 validated
```

```
</details>

### [1. Base class](./models/base.py)
<details><summary>Instructions</summary>

* Write the first class Base:
```

```
</details>

### [2. First Rectangle](./models/rectangle.py)
<details><summary>Instructions</summary>

* Write the class Rectangle that inherits from Base:
```

```
</details>

### [3. Validate attributes](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
```

```
</details>

### [4. Area first](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
```

```
</details>

### [5. Display #0](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
```

```
</details>

### [6. __str__](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
```

```
</details>

### [7. Display #1](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
```

```
</details>

### [8. Update #0](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
```

```
</details>

### [9. Update #1](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
```

```
</details>

### [10. And now, the Square!](./models/square.py)
<details><summary>Instructions</summary>

* Write the class Square that inherits from Rectangle:
```

```
</details>

### [11. Square size](./models/square.py)
<details><summary>Instructions</summary>

* Update the class Square by adding the public getter and setter size
```

```
</details>

### [12. Square update](./models/square.py)
<details><summary>Instructions</summary>

* Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
```

```
</details>

### [13. Rectangle instance to dictionary representation](./models/rectangle.py)
<details><summary>Instructions</summary>

* Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
```

```
</details>

### [14. Square instance to dictionary representation](./models/square.py)
<details><summary>Instructions</summary>

* Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:
```

```
</details>

### [15. Dictionary to JSON string](./models/base.py)
<details><summary>Instructions</summary>

* JSON is one of the standard formats for sharing data representation.
```

```
</details>

### [16. JSON string to file](./models/base.py)
<details><summary>Instructions</summary>

* Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:
```

```
</details>

### [17. JSON string to dictionary](./models/base.py)
<details><summary>Instructions</summary>

* Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:
```

```
</details>

### [18. Dictionary to Instance](./models/base.py)
<details><summary>Instructions</summary>

* Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:
```

```
</details>

### [19. File to instances](./models/base.py)
<details><summary>Instructions</summary>

* Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
```

```
</details>

### [20. JSON ok, but CSV?](./models/)
<details><summary>Instructions</summary>

* Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:
```

```
</details>

### [21. Let's draw it](./models/base.py)
<details><summary>Instructions</summary>

* Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:
```

```
</details>

---

## Author
* **Michelle Domingo** - [michedomingo](https://github.com/michedomingo)