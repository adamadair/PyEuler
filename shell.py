import cmd, importlib
from subprocess import call


class Shell(cmd.Cmd):
    intro = 'Welcome to Adam\'s Project Euler Shell\n'
    prompt = '> '

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

    def run_problem(self, number):
        # if number == '001':
        #     P001().run_me()
        # else:
        #     print('Problem {0} does not have a solution.'.format(number))
        try:
            module = importlib.import_module('solutions.p' + number)
            my_class = getattr(module, 'P' + number)
            my_instance = my_class()
            my_instance.run_me()
        except:
            print('Problem {0} does not have a solution.'.format(number))
