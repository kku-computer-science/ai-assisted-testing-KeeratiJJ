def Sum_of_Degits(num):
    while num >= 10:
        num_str = str(num)
        total = sum(int(digit) for digit in num_str)

        if total< 10:
            return total
        else:
            num = total

input_num = int(input("Enter Number: "))

result = Sum_of_Degits(input_num)
print("Result: ",result)