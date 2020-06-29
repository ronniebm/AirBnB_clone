#!/usr/bin/python3
"""Console version"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
