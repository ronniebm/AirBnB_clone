#!/usr/bin/python3
"""Console version"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    def do_greet(self, line):
        """
        This is help for greet command.
        -------------------------------
        blah blah
        """
        print("hello")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
