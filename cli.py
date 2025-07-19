# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos("todos.txt")

        todos.append(todo)

        functions.write_todos(todos)  # since "todos.txt" is the default argument it need not be provided

    elif user_action.startswith('show'):

        todos = functions.get_todos("todos.txt")

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1

            todos = functions.get_todos("todos.txt")

            newTodo = input("Enter the new todo: ")
            todos[number] = newTodo + '\n'

            functions.write_todos(todos)   # since "todos.txt" is the default argument it need not be provided

        except ValueError:
            print("Your input is not valid:")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos("todos.txt")

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed"
            print (message)

        except IndexError:
            print("Your input is not valid:")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print ("input is not valid")

print("Bye!")