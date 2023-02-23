input_number = int(input("Enter a number from 100 to 999: "))
if input_number >= 100 and input_number <= 999:
    result = input_number % 10 + input_number // 100 + (input_number % 100) // 10
    print("Sum of digits is {} ({} + {} + {})".format(result, input_number // 100,
                                                      (input_number % 100) // 10, input_number % 10))
else:
    print("Number is incorrect")
