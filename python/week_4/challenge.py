try:
    with open('input.txt', 'r') as file:
        content = file.read()
        print(content)
        word_count = len(content.split())
        print(f"Word count: {word_count}")
        capitalized_content = content.upper()
        with open('output.txt', 'w') as output_file:
            output_file.write(capitalized_content)
except FileNotFoundError:
    print("File not found. Please check the filename.") 