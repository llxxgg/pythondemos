import json

# with open('1.txt') as file_object:
#     content = file_object.read()

# print(content)

# 逐行读取
# with open('1.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())


# with open('1.txt') as file_object:
#     lines = file_object.readlines()

# pi = ''
# for line in lines:
#     pi += line.rstrip()

# print(pi)

# with open('programe.txt', 'a') as file_object:
#     file_object.write("\ni love programming 2")


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("can't divide by zero")

# """json.dump"""

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# file_name = 'json_dump.txt'
# with open(file_name, mode='w') as f:
#     json.dump(nums, f)


# with open(file_name) as f:
#     json_load_nums = json.load(f)

# print(json_load_nums)

username = input("what is your name?")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
