# homework
# задание 1

def range_list(num):
  return list(range(1, num + 1))

print(range_list(20))

# задание 2


def upper_lower(hello):
    return hello[0].upper() + hello[1:].lower()

print(upper_lower('hElLO'))
print(upper_lower('HOw ArE yoU')) 

# задание 3

add = ['banana', 'plane', 'computer', 'alan']
x10 = ['helicopter', 'brother', 'house', 'car']

print(list(enumerate(add)))
print(list(enumerate(x10)))
