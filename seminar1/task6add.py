ticket_number = int(input("Enter a number of ticket(6 digits): "))
first_part = ticket_number // 1000
second_part = ticket_number % 1000
first_sum = first_part % 10 + first_part // 100 + (first_part % 100) // 10
second_sum = second_part % 10 + second_part // 100 + (second_part % 100) // 10
if first_sum == second_sum:
    print("yes")
else:
    print("no")
