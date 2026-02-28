name = input("What's your name? \n")
color = input("What is your favorite color?")
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file\n")
    file.write(f"Their favorite color is {color}")