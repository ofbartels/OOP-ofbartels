def sortNumbers(num1, num2):

    if num1 <= num2:

        return num1, num2
    else:

        return num2, num1


try:

    line = input()
    a, b = map(int, line.split())
    sorted_nums = sortNumbers(a, b)
    print(f"{sorted_nums[0]} {sorted_nums[1]}")

except ValueError:
    print("Please enter valid integers.")
