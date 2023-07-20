# List: (used to store multiple items in a single variable) 
my_List = ["Monday", "Tuesday", "Wednesday"]
print(my_List)
my_List = ["Monday", "Tuesday", "Wednesday", "Monday"]
print(my_List)
# Length of a list:
my_List = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
print(len(my_List))
# Type:
my_List = ["Monday", "Tuesday", "Wednesday", "Wednesday"]
print(type(my_List))
my_List1 = [12, 12.121212, 12j, "Hello World!", True]
print(my_List1)
print(type(my_List1))
# list() constructor:
my_List2 = list(("Apple", "Kiwi"))
print(my_List2)
# Access items:
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[2:])
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[:5])
my_List3 = ["Apple", "Kiwi", "Orange", "Melon", "Cherry"]
print(my_List3[-2:])
# Practice questions:
print(len(my_List3))
print(type(my_List3))
print(my_List3[1])
print(my_List3[-2])
# Change items:
my_List4 = ["Apple", "Kiwi", "Orange"]
print(my_List4)
my_List4[1] = "Pear"
print(my_List4)
my_List4[1:3] = ["Pineapple", "Watermelon"]
print(my_List4)
# Adding items:
# append():
my_List4 = ["Apple", "Kiwi", "Orange"]
my_List4.append("Pear")
print(my_List4)
# insert():
my_List4 = ["Apple", "Kiwi", "Orange"]
my_List4.insert(1, "Pear")
print(my_List4)
# Practice questions 2:
the_List = list(("One", "Two", "Three", "Four"))
print(the_List)
print(the_List[2])
the_List[0] = 1
print(the_List)
the_List.append("Five")
print(the_List)
the_List.insert(1, 1.5)
print(the_List)