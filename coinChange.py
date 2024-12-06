userChange = int(float(input("How much money do you have? "))*100)
def greed(userChange):
  print("quarters: " + str(userChange//25))
  userChange = userChange % 25
  print("dimes: " + str(userChange//10))
  userChange = userChange % 10
  print("nickels: " + str(userChange//5))
  userChange = userChange % 6
  print("pennies: " + str(userChange))

greed(userChange)