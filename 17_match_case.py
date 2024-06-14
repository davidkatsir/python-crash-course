value = 35

if type(value) is str:
    print("The value is string")
elif type(value) is int or type(value) is float:
    print("The value is number")
elif type(value) is bool:
    print("The value is boolean")
elif type(value) is list:
    print("The value is list")
else:
    print("The value is of unknown type!")

match type(value):
    case __builtins__.str:
        print("The value is string")
    case __builtins__.int | __builtins__.float:
        print("The value is number")
    case __builtins__.bool:
        print("The value is boolean")
    case __builtins__.list:
        print("The value is list")
    case _:
        print("The value is of unknown type!")

# Important Note
# In most day-to-day programming tasks, you don’t need
# to use __builtins__ directly. It’s usually more readable
# and straightforward to use built-in functions and types
# directly by their names. The __builtins__ namespace is more
# commonly used in more advanced scenarios, such as introspection, dynamic
# code execution, or avoiding shadowing issues.

# You can simplify the code by directly using the type names
# without referencing __builtins__. Here's the revised code:

value = "example"  # Change this to test with different values
value = 35.23
value = True
value = [12, False, "David", True, 7]

match type(value):
    case type_ if type_ is str:
        print("The value is string")
    case type_ if type_ is int or type_ is float:
        print("The value is number")
    case type_ if type_ is bool:
        print("The value is boolean")
    case type_ if type_ is list:
        print("The value is list")
    case _:
        print("The value is of unknown type!")

# More Match Case examples:

command = "start"

match command:
    case "start":
        print("Starting the system...")
    case "stop":
        print("Stopping the system...")
    case "pause":
        print("Pausing the system...")
    case "resume":
        print("Resuming the system...")
    case _:
        print("Unknown command!")

value = True

match value:
    case True:
        print("The value is True")
    case False:
        print("The value is False")
    case _:
        print("The value is neither True nor False")

number = 10

match number:
    case 1:
        print("The number is one")
    case 2:
        print("The number is two")
    case 10:
        print("The number is ten")
    case _:
        print("The number is something else")
