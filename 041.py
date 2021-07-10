number >= 0
def prime_number(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    
    return True

number = input()
if prime_number(int(num)) == True:
    print("yes")
else:
    print("no")