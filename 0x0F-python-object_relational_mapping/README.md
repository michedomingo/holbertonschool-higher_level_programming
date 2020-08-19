# 0x0F. Python - Object-relational mapping

<details><summary>Project Requirements ☑️</summary>
...
</details>

<details><summary>Resources 💡</summary>

* [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA)
* [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw)
* [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/KskI6xMlQCYJyE0UVPJfKQ)
* [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ)
* [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA)
* [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/SSoBE3ckyGFi3NexCH3nuw)
* [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg)
* [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A)
* [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw)
* [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw)
* [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw)
</details>

#### Learning Objectives 🤓

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script 
* What ORM means
* How to map a Python Class to a MySQL table

---
## Tasks

### [0. Get all states](./0-select_states.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all states from the database hbtn_0e_0_usa: 
```

```
</details>

### [1. Filter states](./1-filter_states.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: 
```

```
</details>

### [2. Filter states by user input](./2-my_filter_states.py)
<details><summary>Instructions</summary><br>

* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
```

```
</details>

### [3. SQL Injection...](./3-my_safe_filter_states.py)
<details><summary>Instructions</summary><br>

* Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
```

```
</details>

### [4. Cities by states](./4-cities_by_state.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all cities from the database hbtn_0e_4_usa 
```

```
</details>

### [5. All cities by state](./5-filter_cities.py)
<details><summary>Instructions</summary><br>

* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa 
```

```
</details>

### [6. First state model](./model_state.py)
<details><summary>Instructions</summary><br>

* 
```

```
</details>

### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all State objects from the database hbtn_0e_6_usa 
```

```
</details>

### [8. First state](./8-model_state_fetch_first.py)
* Write a script that prints the first State object from the database hbtn_0e_6_usa 
<details><summary>Instructions</summary><br>

```

```
</details>

### [9. Contains `a`](./9-model_state_filter_a.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa 
```

```
</details>

### [10. Get a state](./10-model_state_my_get.py)
<details><summary>Instructions</summary><br>

* Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa 
```

```
</details>

### [11. Add a new state](./11-model_state_insert.py)
<details><summary>Instructions</summary><br>

* Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa 
```

```
</details>

### [12. Update a state](./12-model_state_update_id_2.py)
<details><summary>Instructions</summary><br>

* Write a script that changes the name of a State object from the database hbtn_0e_6_usa 
```

```
</details>

### [13. Delete states](./13-model_state_delete_a.py)
<details><summary>Instructions</summary><br>

* Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa 
```

```
</details>

### [14. Cities in state](./model_city.py)
<details><summary>Instructions</summary><br>

* Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
```

```
</details>

### [15. City relationship](./relationship_city.py)
<details><summary>Instructions</summary><br>

* Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:
```

```
</details>

### [16. List relationship](./101-relationship_states_cities_list.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa 
```

```
</details>

### [17. From city](./102-relationship_cities_states_list.py)
<details><summary>Instructions</summary><br>

* Write a script that lists all City objects from the database hbtn_0e_101_usa 
```

```
</details>
---

## Author
[Michelle Domingo](https://github.com/michedomingo)
