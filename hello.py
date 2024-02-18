message = "hello world"
print(message.title().upper())

firstName = "ada"
lastName = "lovelace"
fullName = f"{firstName} {lastName}"
print(fullName)

str = "python "
print(str.rstrip())

universeAge = 14_000_000_000
print(universeAge)

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# 注释

names = ['zhangsan', 'lisi', 'wangwu']
print(names)
names[0] = 'zhuliu'
names.append('qianqi')
print(names)
names.insert(1, 'zhuwu')
print(names)
del names[0]
print(names)
lastItem = names.pop()
print(lastItem)
names.append('lisi')
names.remove('lisi')  # remove只删除第一个指定的值
print(names)

cars = ['bmw', 'audi', 'toyota']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

cars.reverse()
print(cars)
print(len(cars))
print(cars[-1])

print('------------------')
# 遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n")
for num in range(1, 5):
    print(num)

print("\n")
for num in range(5):
    print(num)

numList = list(range(5))
print(numList)

print('----------')
digits = [1, 2, 3, 4, 5, 6]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# if
print(cars)
for car in cars:
    if car == 'audi' or car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
# in / not in
if 'mushrooms' in requested_toppings:
    print('contain mushrooms')

age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')

print('-----')
requested_toppings = []
for item in requested_toppings:
    print(item)
