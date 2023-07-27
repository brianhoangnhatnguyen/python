list1 = ['hello', 'hi', 'goodbye']
print(list1)
print(type(list1))
print(len(list1))
print(list1[1:])
print(list1[-3:-1])
sentence = "         today is thursday          "
print(sentence.strip())
sentence = "today is thursday"
print(sentence.capitalize())
random_things = tuple((12121, 123j, "hahahdf", 123.123123))
print(random_things)
random_things2 = list((12121, 123j, "hahahdf", 123.123123))
print(random_things2)
sentence = "today is thursday"
if "thursday" in sentence:
    print("yahoo")
greeting = ['hello', 'hi', 'goodbye']
greeting[2] = "hey"
print(greeting)
greeting = ['hello', 'hi', 'goodbye']
greeting.insert(0, "hiihi")
print(greeting)
anotherlist = ['OMG', 'NO', 'YES', 'MAYBE', 'THE MIMIC!!!!!']
anotherlist.append("asdf")
print(anotherlist)
anotherlist = ['OMG', 'NO', 'YES', 'MAYBE', 'THE MIMIC!!!!!']
notanotherlist = ['hi guys and', 'welcome to my', 'minecraft lets play']
anotherlist.extend(notanotherlist)
print(anotherlist)
notanotherlist.remove('hi guys and')
print(notanotherlist)
notanotherlist = ['hi guys and', 'welcome to my', 'minecraft lets play']
i = 0
while i < len(notanotherlist):
    print(notanotherlist[i])
    i=i+1
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 74, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
list2.sort(reverse = True)
print(list2)