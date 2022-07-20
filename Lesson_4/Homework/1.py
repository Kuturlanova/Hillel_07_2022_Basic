# Homework_1
s = '43 більше ніж 34 але менше ніж 56'
str_list = s.split()
m = []
for i in str_list:
    if i.isdigit():
        m.append(int(i))
print(sum(m))

# Homework_2

fruits = ['apple', 'banana', 'mango', 'apricot']
fruits_new = []
for i in fruits:
    if i.lower().startswith('a'):
        fruits_new.append(i)

print(fruits_new)

# Homework_3

list1 = ['Anna', 'Mary', 'Bob', 'John']
list2 = ['Anna', 'Bob']
new_list = list(set(list1) ^ set(list2))
print(new_list)

# Homework_4


new_list = []
my_str = input()
if len(my_str) % 2 != 0:
    my_str += "_"
while len(my_str) > 0:
    new_list.append(my_str[:2])
    my_str = my_str[2:]
print(new_list)
