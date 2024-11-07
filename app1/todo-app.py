# Create a todo list
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user = input('Enter add, show, edit, complete or exit to finish. : ')
    user = user.strip().lower() # This will change the string the user typed and remove extra spaces

    if user.startswith("add"):
        todo = user[4:] + '\n'

        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user.startswith("show"):
        todos = functions.get_todos()
        '''
        new_todos = [item.strip('\n') for item in todos]
        - this is a list comprehension to remove \n and store new item without blank spaces
        '''
        for i, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f'{i + 1}-{item}'
            print(row)
        list_length = len(todos)
        print(f'You have {list_length} item in your to do list.\n')
    elif user.startswith("edit"):
        try:
            number = int(user[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new to do: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid!")
            continue
    elif user.startswith("complete"):
        try:
            number = int(user[9:])

            todos = functions.get_todos()
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f'Todo {todos_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print("There is no item with that number! Please try again.")
            continue
    elif user.startswith("exit"):
        break
    else:
        print("Command invalid!")
        # case _:  Use the underscore name convention for an undefined variable therefore if none of the cases match it will execute this.
print('Bye!')


