revenue = int(input("Enter company revenue: "))
costs = int(input("Enter costs of the company: "))
profit = revenue - costs
if profit > 0:
    print("The company has worked with profit. Its value is {}.".format(profit))
    print("Profitability of revenue is {}".format(profit / revenue))
    employees = int(input("Enter number of employees: "))
    print("The company's profit per employee is {}".format(profit / employees))
else:
    print("The company has worked with loss. Its value is {}.".format(profit))
