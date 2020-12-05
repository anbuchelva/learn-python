#Write your code below this line 👇
def prime_checker(number):
    is_prime = True 
    # using while loop
    # i = 2
    # while n > i-1:
    #     if n % i == 0 and n != i:
    #         is_prime = False
    #         i = n                  
    #     i += 1

    # using for loop
    for j in range(2, number):
        if number % j == 0:
            is_prime = False

    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)