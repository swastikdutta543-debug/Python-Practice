print("hello world")

#ask user for their name
a = input("what's your name? ")

# Remove White space from str
a = a.strip()

#capitalize user's name
a= a.capitalize() # it only capitalize the first letter of the whole sentence not every 1st letter of every word

a = a.title() # in this case every 1st letter of every word of a sentence will be capitalized

#**** we can also add the both like a = a.strip().title() and also can be done like this a = input("....").strip().title()

#say hello to user
print("hello1 " + a) 
print("hello2",a)
print("hello3 ", end='')
print(a)
print(f"hello4 {a}")
print("hello5", a, sep='???') # output--> hello???a

#split the user name
first,last = a.split(" ")
print(f"hello {first}")