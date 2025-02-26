"""
author: tao
date: 25.2

演示python list
"""

fruit_list = ["apple", "banana", "cherry"]

print(fruit_list)
print(fruit_list[0])
print(fruit_list[1])
print(len(fruit_list))

fruit_list.append("orange")
print(fruit_list)

fruit_list[0] = "pear"
print(fruit_list)

del fruit_list[0]
print(fruit_list)

fruit_list.remove("banana")
print(fruit_list)