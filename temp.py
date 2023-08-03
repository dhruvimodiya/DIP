
numbers = []
numbers = range(0,int(input("enter a number:- ")))
numbers = list(filter(lambda n:n%2 != 0,numbers))
print(list(numbers))
print(sum(numbers))