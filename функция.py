numbers = [5, 2, 7]
#numbers[3] = 100
numbers.append(100)
numbers.insert(1, True)

b = [5, 6, 8]
numbers.extend(b)
#numbers.reverse()
numbers.sort()


numbers.pop()
numbers.remove(True)

#numbers.clear()

#print(numbers.count(True))
print(len(numbers))
