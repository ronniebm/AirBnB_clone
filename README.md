# AirBnB clone - The console
![enter image description here](https://i.imgur.com/44u0pXG.png)

## :clipboard: Table of Content
* [Description](#bookmark_tabs-description)
* [Requirements](#straight_ruler-requirements)
* [Command Interpreter](#computer-command-interpreter)
* [Examples](#flashlight-examples)
* [Contributors](#octocat-contributors)

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

### Installation

If you want to run the command interpreter follow the next steps:

* Clone the repository:
```git clone https://github.com/ronniebm/AirBnB_clone.git```

* Access AirBnb directory:
```cd AirBnb```

* Execute the following command:
```$ ./console```

* You can also execute in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Usage

After you execute the console you can use the following commands:

* help - Gives a little description of a command
* quit - Exit the program
* EOF - Exit the program
* create - Creates a new instance
* show - Prints the string representation of an instance based on the class name and id
* detroy - Deletes an instance based on the class name and id
* all - Prints all string representation of all instances based or not on the class name
* update - Updates an instance based on the class name and id by adding or updating attribute

Also:
```actions = [show, destroy, all, update, count]```

* `<class name>.actions()` - Executes actions dependind on the name of the class

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

## :flashlight: Examples

### help example

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
### create example

```

(hbnb) create BaseModel
0dfdc101-0895-44fc-88cd-4b21bb1dc32a
(hbnb)

```

### quit and EOF example

Quit and EOF commands stops the execution of the program

```
(hbnb) quit
$
```

```
(hbnb) EOF
$
```

### show example

```
(hbnb) show BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
[BaseModel] (0dfdc101-0895-44fc-88cd-4b21bb1dc32a) {'id': '0dfdc101-0895-44fc-88cd-4b21bb1dc32a', 'created\_at': datetime.datetime(2020, 7, 1, 16, 3, 59, 173753), 'updated\_at': datetime.datetime(2020, 7, 1, 16, 3, 59, 173761)}
```

### destroy example

```
(hbnb) destroy BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
(hbnb) show BaseModel 0dfdc101-0895-44fc-88cd-4b21bb1dc32a
** no instance found **
(hbnb) 
```

### all example

```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

### update example

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

### `<class name>.actions()` examples
`actions = [show, destroy, all, update, count]`

* `<class>.all()` example

```
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@holbertonshool.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 
```

* `<class.count()>` example
```
(hbnb) User.count()
2
(hbnb) 
```

* `<class.destroy>` example
```
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Holberton")
** no instance found **
(hbnb) 
```

## :octocat: Contributors 
[@Andres Hugueth - Github](https://github.com/andreshugueth) - [@Ronnie Barrios - Github](https://github.com/ronniebm)

