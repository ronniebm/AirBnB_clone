# AirBnB clone - The console
<p align="center"><img src= "https://imgur.com/a/Ej5mveI"/></p>

## :bookmark\_tabs: Description
Command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## :straight\_ruler: Requirements

### Python Scripts

* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* The first line of all your files should be exactly #!/usr/bin/python3
* Your code should use the PEP 8 style (version 1.7 or more)
* All your files must be executable

### Python Unit Tests

* All your test files should be inside a folder tests
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test\_models/test\_base\_model.py
* e.g., For models/user.py, unit tests must be in: tests/test\_models/test\_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test\_models/test\_base\_model.py

## :computer: Command Interpreter

### How to start it

If you want to run the command interpreter follow the next steps:

* Clone the repository

```
git clone https://github.com/ronniebm/AirBnB_clone.git
```
* Execute the following command

```
./console

```

### Usage

After you execute the console you can use the following commands:

* help
* quit
* EOF
* create
* show
* detroy
* all
* update

#### Usage Example

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit

```

### Examples

#### help example

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  User  all  create  destroy  help  quit  show  update

(hbnb)

```

```
(hbnb) help create
Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel

(hbnb)
```
#### create example

```

(hbnb) create BaseModel
0dfdc101-0895-44fc-88cd-4b21bb1dc32a
(hbnb)

```

#### quit and EOF example

Quit and EOF commands stops the execution of the program

```
(hbnb) quit

```

```
(hbnb) EOF

```

#### show example

```
(hbnb) show BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
\[BaseModel\] (0dfdc101-0895-44fc-88cd-4b21bb1dc32a) {'id': '0dfdc101-0895-44fc-88cd-4b21bb1dc32a', 'created\_at': datetime.datetime(2020, 7, 1, 16, 3, 59, 173753), 'updated\_at': datetime.datetime(2020, 7, 1, 16, 3, 59, 173761)}

```

#### destroy example

```
(hbnb) destroy BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
(hbnb) show BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
** no instance found **
(hbnb) 
```

#### all example

```
(hbnb) all BaseModel
\["\[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created\_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated\_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

```

#### update example

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first\_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
\[BaseModel\] (49faff9a-6318-451f-87b6-910505c55907) {'first\_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created\_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated\_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

## :octocat: Contributors 
[@AndresHugueth - Github](https://github.com/andreshugueth) - [@RonnieBarrios - Github](https://github.com/ronniebm)

