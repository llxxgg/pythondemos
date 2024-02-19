# map
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 5
print(alien_0)

# 获取
print(f"alien color is {alien_0['color']}")

car = alien_0.get('car', 'empty')
print(f"alien car is {car}")

car = alien_0.get('car')
print(f"alien car is {car}")

for k, v in alien_0.items():
    print(f"key:{k} value:{v}")

for key in alien_0.keys():
    print(key)

# 遍历字典时，会默认遍历所有的键
for key in alien_0:
    print(key)

for val in alien_0.values():
    print(val)

for val in set(alien_0.values()):
    print(val)

# 创建集合, 无序
languages = {'python', 'c', 'golang', 'python'}
print(languages)
