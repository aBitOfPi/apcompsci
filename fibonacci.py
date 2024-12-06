starters = {0: 0, 1: 1}

def fibonacci(n):
  if n not in starters:
      starters[n] = fibonacci(n-1) + fibonacci(n-2)
      print(str(fibonacci(n-1))+' left')
      print(str(fibonacci(n-2))+' right')
  return starters[n]

number = int(input("Enter the number for fiboonacci value: "))
result = fibonacci(number)
print(f"The value of fibbonaci {number} is {result}")