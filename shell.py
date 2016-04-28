import cmd, importlib
from subprocess import call
from tkinter import Tk


class Shell(cmd.Cmd):
    intro = 'Welcome to Adam\'s Project Euler Shell\n'
    prompt = '> '
    last_answer = ''

    def do_exit(self, arg):
        """Exits the shell."""
        return True

    def do_hello(self, arg):
        """hello
=====
Provides a warm and friendly greeting from the program to the person
whose name is provided.

usage: hello [name]

If the name is not provided, the user will be prompted for one.
        """
        if arg is None or arg == '':
            name = input('name: ')
        else:
            name = arg
        print('Hello, {0}!'.format(name))

    def do_problem(self, arg):
        """problem
=======
Execute the solution to a problem.

usage: problem <nnn>
where: <nnn> is the Project Euler problem number

example: > problem 001
        """
        if arg is None or arg == '':
            print("Missing problem number.")
            return
        else:
            self.run_problem(arg)

    def do_shell(self, arg):
        call(arg, shell=True)

    def do_clip(self, arg):
        """clip
=====
Saves last answer to clipboard.
"""
        if self.last_answer != '':
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(self.last_answer)

            print('"{}" saved to clip board.'.format(self.last_answer))
        else:
            print('Nothing to clip.')

    def run_problem(self, number):
        # if number == '001':
        #     P001().run_me()
        # else:
        #     print('Problem {0} does not have a solution.'.format(number))
        try:
            module = importlib.import_module('solutions.p' + number)
            my_class = getattr(module, 'P' + number)
            my_instance = my_class()
            self.last_answer = my_instance.run_me()
        except:
            print('Problem {0} does not have a solution.'.format(number))
