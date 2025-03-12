"""
Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

"""

# Challenge 1

def user_input():
    integer_list = []

    user_input_value = int(input("How many integers do you want to add to the list? "))
    for number in range(user_input_value):
        number = int(input("Please enter the number: "))
        integer_list.append(number)
    sum_of_numbers = sum(integer_list)
    print(f'The sum is : {sum_of_numbers}')


# user_input()

#Challenge 2

def challenge_2():
    books = ("The Wall Speaks", "48 Laws of Power","Count of ALexandra","Subtle Art of Not Giving A Fuck","The Rationale Male")
    for book in books:
        print(book)

# challenge_2()


#Challenge 3

def challenge_3():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    color = input("What is your favorite color? ")

    dict_person = {}

    dict_person["name"] = name
    dict_person["age"] = age
    dict_person["color"] = color

    print("Here are your details: ")

    print(dict_person)


# challenge_3()

# Challenge 4

def new_set():
    set_a = {2,3,5,4,6}
    set(set_a)
    print(set_a)
    print(type(set_a))

    set_b = {1,4,6,7,9,2}
    set(set_b)

    print(type(set_b))

    set_c = set_a.intersection(set_b)
    print(f"set c: {set_c}")


# new_set()


#Challenge 5

def word_input():
    number_of_words = int(input("How many words do you want to add? "))
    words = []

    for i in range(number_of_words):
        word = input("Enter the word:  ")
        words.append(word)

    odd_word_length = [word for word in words if len(word) % 2 != 0]

    print(f"ALl Words :  {words}")
    print(f"Odd Words : {odd_word_length}")


word_input()
