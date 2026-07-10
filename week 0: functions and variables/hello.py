#Ask user for their name (remove whitespaces from the str and capitalize users name)
name = input("whats your name? ").strip().title()

#split users name into first name and last name 
first, last = name.split()

#Say Hello to the user 
print(f"hello, {first}")