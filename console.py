#!/usr/bin/python3
"""Console version"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    __classes = [
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
        ]

    def do_EOF(self, line):
        """
        EOF [command]:
        -------------
        End Of File, used to exit from the console.
        """
        print()
        return True

    def do_quit(self, line):
        """
        quit [command]:
        ---------------
        used to exit from the console.
        """
        return True

    def emptyline(self):
        """This is the override of the cmd default's
        emptyline method, which is called when an empty
        line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args[0] + '()')
            models.storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                print(objects[key_find])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel
        """
        args = line.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute (save
        the change into the JSON file).
        Ex: $ update BaseModel <valid id> attrib value
        """
        args = line.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        elif "{" not in line and "}" not in line:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find)
            kwargs = eval("{" + line.split("{")[1].split("}")[0] +
                          "}")
            if obj is None:
                print("** no instance found **")
                return
            for key, val in kwargs.items():
                setattr(obj, key, val)
            models.storage.save()

    def do_User(self, line):
        """Retrieve all instances of User class.
        Ex: $ User.all()
        """
        class_name = "User"
        HBNBCommand.generic_commands(line, class_name)

    def do_BaseModel(self, line):
        """Retrieve all instances of BaseModel class.
        Ex: $ BaseModel.all()
        """
        class_name = "BaseModel"
        HBNBCommand.generic_commands(line, class_name)

    def do_Amenity(self, line):
        """Retrieve all instances of Amenity class.
        Ex: $ Amenity.all()
        """
        class_name = "Amenity"
        HBNBCommand.generic_commands(line, class_name)

    def do_City(self, line):
        """Retrieve all instances of City class.
        Ex: $ City.all()
        """
        class_name = "City"
        HBNBCommand.generic_commands(line, class_name)

    def do_Place(self, line):
        """Retrieve all instances of Place class.
        Ex: $ Place.all()
        """
        class_name = "Place"
        HBNBCommand.generic_commands(line, class_name)

    def do_Review(self, line):
        """Retrieve all instances of Review class.
        Ex: $ Review.all()
        """
        class_name = "Review"
        HBNBCommand.generic_commands(line, class_name)

    def do_State(self, line):
        """Retrieve all instances of State class.
        Ex: $ State.all()
        """
        class_name = "State"
        HBNBCommand.generic_commands(line, class_name)

    @staticmethod
    def generic_commands(line, class_name):
        objects = models.storage.all()
        method = line.split(".")[1].split("(")[0]

        if "(" and ")" in line:
            if method == "all":
                HBNBCommand.do_all(HBNBCommand, class_name)
            elif method == "count":
                counter = 0
                for key in objects:
                    if key.split(".")[0] == class_name:
                        counter += 1
                print(counter)
            elif method == "show":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        print(value)
            elif method == "destroy":
                if '"' not in line:
                    pass
                else:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    if value is None:
                        print("** no instance found **")
                    else:
                        objects.pop(key, None)
                        models.storage.save()
            elif method == "update":
                if '"' not in line and "," not in line:
                    pass
                elif "{" not in line and "}" not in line:
                    obj_id = line.split('"')[1]
                    key = class_name + "." + obj_id
                    value = objects.get(key)
                    attr = line.split(",")[1].split('"')[1]
                    new_val = line.split(",")[2].split('"')[1]
                    args = class_name + " "+obj_id+" "+attr+" "+new_val
                    if value is None:
                        print("** no instance found **")
                    else:
                        HBNBCommand.do_update(HBNBCommand, args)
                else:
                    obj_id = line.split('"')[1]
                    new_dict_str = line.split("{")[1].split("}")[0]
                    new_dict_str = "{" + new_dict_str + "}"
                    args = class_name + " "+obj_id+" "+new_dict_str

                    HBNBCommand.do_update(HBNBCommand, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
