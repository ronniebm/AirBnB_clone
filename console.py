#!/usr/bin/python3
"""Console version"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    classes = {"BaseModel"}

    def do_EOF(self, line):
        """
        EOF [command]:
        -------------
        End Of File, used to exit from the console.
        """
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
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
            return False
        try:
            new_inst = eval(line + '()')
            models.storage.save()
            print(new_inst.id)
        except NameError:
            print('** class doesn\'t exist **')

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name
        and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()

        if len(args) == 0:
            print('** class name missing **')
        elif not args[0] in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            objects = models.storage.all()
            key_find = args[0] + '.' + args[1]
            if key_find in objects:
                print(objects[key_find])
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
