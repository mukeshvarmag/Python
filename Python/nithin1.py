from tabulate import tabulate
divide =[["Nikhil", 21,"male",5], 
          ["Ravi", 25,"male",9], 
          ["Manish", 36,"female",7], 
          ["Prince", 40,"male",4]]


head = ["Name", "age","gender","class"]
print(tabulate(divide, headers=head, tablefmt="grid"))