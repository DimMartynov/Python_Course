str1 = 'This is a string.   '
str2 = ' This is another string. 0'
print(str1 + str2)
print(len(str1))
print(str1.title())
print(str1.lower())
print(str1.upper())
print(str1.rstrip())
print(str2.lstrip())
print(str1.strip())
print(str2.strip('0'))

ch = str1[8]
print(ch)
chm = str2[4:6]
print(chm)
print(str2[1:], str2[:3], str2[:], str2[1:5:2])

m = int(16)
n = int(7)

p = str2 + str(m)
print(p)

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("{:.1f}".format(float(n1)) + " plus " + "{:.2f}".format(float(n2)) + " = ", "{:.3f}".format(n3))

a = 1 / 3
print("{:7.3f}".format(a))

a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

list1 = [20, 93, 84, 5, 70, 23, 8, 5, 45, 67, 13]
dir(list)
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

print(list1)
list1[4] = 71
print(list1)
list1.append(14)
print(list1)
list1.insert(4, 4)
print(list1)
list1.remove(list1[7])
print(list1)
list1.remove(list1[-1])
print(list1)

list1.sort(reverse=True)
print(list1)
list2 = [0, 93, 48, 7, 50, 9, 23, 7, 40, 59, 8, 27, 85, 43, 20, 2]
list3 = sorted(list2)
print(list2)
print(list3)

seq = (2, 8, 23, 97, 92, 44, 17, 8, 44, 12)
print(dir(seq))
help(tuple.index)
help(tuple.count)
print(seq.count(8))
print(seq.index(44))
tup = tuple(list3)
print(tup)

D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D)

dp = {}
dp['name'] = input("Enter name: ")
dp['age'] = input("Enter age: ")
print(dp)


rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}
rec['job'].append('secr')

print('Name: ' + rec['name']['firstname'] + ' ' + rec['name']['lastname'])
print('First name: ' + rec['name']['firstname'])

print(rec)
print('Full name: ' + rec['name']['firstname'] + ' ' + rec['name']['lastname'])
print('Jobs: ' + rec['job'][0] + ', ' + rec['job'][1] + ', ' + rec['job'][2])
print('Age: ' + str(rec['age']))

