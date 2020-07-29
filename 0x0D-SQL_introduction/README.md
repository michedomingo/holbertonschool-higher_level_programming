# 0x0D. SQL - Introduction

<details><summary>Project Requirements ☑️</summary>

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc
</details>

<details><summary>Resources 💡</summary>

* [What is Database & SQL?](https://intranet.hbtn.io/rltoken/khEqMKp1PHvKpfO18d4fLQ)
* [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/qrONF5FZPsRxRJ2FkLVPcg)
* [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/ibCYnC9CDgZg5NQQvccBWw)
* [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/yelYhpf7l0FcRIPCVfnMLw)
* [SQL technique: functions](https://intranet.hbtn.io/rltoken/3aQcovOE-clrD8yIfxFE9Q)
* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/lTXnq6pdk59x2h_Y-q0-Hg)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/R--kAkehyaawZFY4m1inxQ)
* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/aGZu7ulJpbbKcDhcz49yrg)
* [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/XrqR4oh6zsk0eOKoTgkA3Q)
</details>

#### Learning Objectives 🤓

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

---
## Tasks

### [0. List databases](./0-list_databases.sql)
<details><summary>Write a script that lists all databases of your MySQL server.</summary><br>

* 
```

```
</details>

### [1. Create a database](./1-create_database_if_missing.sql)
<details><summary>Write a script that creates the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [2. Delete a database](./2-remove_database.sql)
<details><summary>Write a script that deletes the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [3. List tables](./3-list_tables.sql)
<details><summary>Write a script that lists all the tables of a database in your MySQL server.</summary><br>

* 
```

```
</details>

### [4. First table](./4-first_table.sql)
<details><summary>Write a script that creates a table called first_table in the current database in your MySQL server.</summary><br>

* 
```

```
</details>

### [5. Full description](./5-full_table.sql)
<details><summary>Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [6. List all in table](./6-list_values.sql)
<details><summary>Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [7. First add](./7-insert_value.sql)
<details><summary>Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.</summary><br>

* 
```

```
</details>

### [8. Count 89](./8-count_89.sql)
<details><summary>Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [9. Full creation](./9-full_creation.sql)
<details><summary>Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.</summary><br>

* 
```

```
</details>

### [10. List by best](./10-top_score.sql)
<details><summary>Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [11. Select the best](./11-best_score.sql)
<details><summary>Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [12. Cheating is bad](./12-no_cheating.sql)
<details><summary>Write a script that updates the score of Bob to 10 in the table second_table.</summary><br>

* 
```

```
</details>

### [13. Score too low](./13-change_class.sql)
<details><summary>Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [14. Average](./14-average.sql)
<details><summary>Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [15. Number by score](./15-groups.sql)
<details><summary>Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [16. Say my name](./16-no_link.sql)
<details><summary>Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.</summary><br>

* 
```

```
</details>

### [17. Go to UTF8](./100-move_to_utf8.sql)
<details><summary>Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.</summary><br>

* 
```

```
</details>

### [18. Temperatures #0](./101-avg_temperatures.sql)
<details><summary>Import in hbtn_0c_0 database this table dump: download</summary><br>

* 
```

```
</details>

### [19. Temperatures #1](./102-top_city.sql)
<details><summary>Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)</summary><br>

* 
```

```
</details>

### [20. Temperatures #2](./103-max_state.sql)
<details><summary>Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)</summary><br>

* 
```

```
</details>
---

## Author
[Michelle Domingo](https://github.com/michedomingo)