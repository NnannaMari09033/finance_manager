from json_con import file

class finance_manager(file):
  def __init__(self):
    self.income = 0
    self.expenses = self.load_from_file('json_store/mobiles.json')
    

  def salary(self):
    self.income = int(input("enter your monthly income: "))
    return self.income
    
  def choice(self):
    while True:
      print()
      print("enter to input your expenses or indicate you are done: ")
      print()
      command = input("enter 'e' or 'd': ")
      print()
      if command == "e":
        expense_category = input("enter your expense category: ")
        amount = int(input("enter the amount you spent: "))

        self.expenses.append({"expense_category": expense_category, "amount": amount})
        self.save_to_file(self.expenses,'json_store/mobiles.json')
       
        more_expense = input("do you have more exepenses 'yes' or 'no': ")
        if more_expense == "yes":
          expense_category = input("enter the expense category: ")
          amount = int(input("enter the amount you spent: "))
        elif more_expense == "no":
          break

      elif command == "d":
        print()
        print("Thank you for using this services")
        break
      
      
  def summation(self): 
    total_income = sum(expense['amount'] for expense in self.expenses)
    return total_income
    
 
    
  def remaining_b(self):
    remaining_balance = self.income - self.summation()
    return remaining_balance
  
  def summary(self):
    print("============\n")
    print(f"income: {self.income}")
    print(f"summation: {self.summation()}")
    print(f"balance: {self.remaining_b()}")
    print("===========\n")

  def comparison(self):
    if self.income > self.summation():
      print("congratulations you have used your money wisely")
    elif self.salary == self.summation:
      print("you did well but try to minimize your expenditures next time!")
    else:
      print("you exceeded your salary for the month!")
          
print("welcome to the record book!")
print()
pdm = finance_manager()
pdm.salary()
pdm.choice()
pdm.summation()
pdm.remaining_b()
pdm.summary()
pdm.comparison()


