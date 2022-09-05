#!/usr/bin/python3

""" console module v 0.0.1 """

import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """ creating a consile """

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}


    def do_EOF(self, args):
        """ EOF command to exit the program """
        raise SystemExit

    def do_quit(self, args):
        """ quit command to exit the program """
        raise SystemExit

    def emptyline(self):
        """ do nothing after emptyline + enter """
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.classes.keys():
            print("** class doesn't exist ** (ex: $ create MyModel)")
        else:
            model = HBNBCommand.classes[args]()
            model.save
            print(model.id)

    def do_show(self, classNam):
        """Print string representation of an instance"""
        base_list = classNam.split()
        if len(base_list) == 0:
            print("** class name missing **")
            return
        elif base_list[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(base_list) == 1:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            keys = base_list[0] + '.' + base_list[1]
            if keys in instances:
                print(instances[keys])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        className = line.split()

        if len(className) == 0:
            print("** class name missing **")
            return
        elif className[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className) == 1:
            print("** instance id missing **")
        else:
            instances = className[0] + "." + className[1]
            if instances in models.storage.all():
                del models.storage.all()[instances]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, classNam):
        """Print a string of an instance based on class name"""
        args = classNam.split(" ")
        if args[0] == "" or args[0] in HBNBCommand.classes:
            string = []
            objs = storage.all()
            for key in objs.keys():
                if args == [''] or key.split(".")[0] == args[0]:
                    string.append(str(objs[key]))
            print(string)
        else:
            print("** class doesn't exist **")

    def do_update(self, classNam):
        """Updates an instance based on the class name"""

        classNam = shlex.split(classNam)

        if len(classNam) == 0:
            print("** class name missing **")
            return
        if classNam[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist *+")
            return
        if len(classNam) == 1:
            print("** instance id missing **")
            return
        args = classNam[0] + '.' + classNam[1]
        if args not in models.storage.all():
            print("** no instance found **")
            return
        if len(classNam) == 2:
            print("** attribute name missing **")
            return
        if len(classNam) == 3:
            print("** value missing **")
            return
        attr = classNam[2]
        value = classNam[3]
        objs = storage.all()
        id = classNam[0] + "." + classNam[1]
        objs[id][attr] = value
        models.storage.update_obejts(objs)



if __name__ == '__main__':
    HBNBCommand().cmdloop()