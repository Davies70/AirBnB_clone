#!/usr/bin/python3

""" console module v 0.0.1 """

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    """ creating a console """

    def do_EOF(self, args):
        """ EOF command to exit the program """
        raise SystemExit

    def do_quit(self, args):
        """ quit command to exit the program """
        raise SystemExit

    def emptyline(self):
        """ do nothing after emptyline + enter """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
