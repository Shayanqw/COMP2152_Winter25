import random

elements = ["Hydrogen", "Helium", "lithium", "Beryllium", "Boron", "Carbon"]
print('elements:', elements)


# def say_hi(name, message='Hello'):
#    print(f'{name}: {message}')

# say_hi(name='shayan')

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid number.')
            continue


try:
    elements = get_valid_int_input('Enter the index of the elements you like: ')
    element_roll = random.randint(1, 6)
    totalNum = elements + element_roll
    if element_roll <= 2:
        print("you rolled a week number")
    elif element_roll <= 4:
        print("your element is moderate")
    else:
        print("great element")
except IndexError:
    print("Error: Invalid element index")

except Exception as e:
    print("f")
