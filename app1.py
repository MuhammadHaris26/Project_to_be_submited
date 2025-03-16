#Mad libs python project

noun1 = input("Enter an noun 1: ")
verb1 = input("Enter a verb 1: ")
noun2 = input("Enter an noun 2: ")
adjective1 = input("Enter an adjective 1 : ")
noun3 = input("Enter an noun 3: ")
verb2 = input("Enter a verb 2: ")
adjective2 = input("Enter an adjective 2: ")
adjective3 = input("Enter an adjective 3: ")

Story = (f"""Hey! My name is {noun1}. I am currently {verb1} {noun2} at Air University Islamabad.
 I am very {adjective1} with my course, and all our {noun3} {verb2} {adjective2}, dedicated, and {adjective3}.""")
print("_" * 43)
print("Your Mad libs python project")
print("_" * 43)
print(Story)