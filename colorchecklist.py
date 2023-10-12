checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print (str(index) + list_item)
        index += 1

def mark_completed(index):
    return checklist

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")

        read(item_index)
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")
        return True

user_value = user_input("Please Enter a Value:")
print(user_value)

def test():
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
