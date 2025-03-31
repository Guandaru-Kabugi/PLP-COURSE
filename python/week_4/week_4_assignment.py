try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
        word_count = len(content.split())
        print(f"Word count: {word_count}")
        with open('sample_output.txt', 'w') as output_file:
            # Convert content to title case
            capitalized_content = content.title()
            output_file.write(capitalized_content)
            print("Content has been written to sample_output.txt")
        # Print the capitalized content
        print("Capitalized content:")
        print(capitalized_content)
except FileNotFoundError:
    print("File not found. Please check the filename.")


#task 2

user_input = input("please enter the name of the file: ")
try:
    with open(user_input, 'r') as file:
        content = file.read()
        print(content)
        word_count = len(content.split())
        print(f"Word count: {word_count}")
        capitalized_content = content.title()
        with open('output.txt', 'w') as output_file:
            output_file.write(capitalized_content)
except FileNotFoundError:
   print("File not found. Please check the filename.")
except Exception as error:
   print("An error occurred:", error)