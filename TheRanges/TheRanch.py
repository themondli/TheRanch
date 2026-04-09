import math

print("Binary Line Test")

print("The numbers in the sequence are = ")
twitter = []
for i in range(0, 10+1):
    binary = int(input("Enter: "))
    twitter.append(binary)

print("The numbers that are divisible by 10 are = {")
for j in twitter:
    if(j % 5 == 0):
        print(f"{j}", end=" ")

print('}')

while (True):
    letter = input("Enter a sentence: ")

    letterArray = letter.lower().split()
    letterSet = set(letterArray)
    alphaOmega = sorted(letterSet)

    for i in alphaOmega:
        if(i.isalnum()):
            print(alphaOmega)
        else:
            print("Invalid attempt! try again.")

    break

C = 50
H = 30

##D = int(input("Number is "))
print("The sequence of this equation is: {")
for D in range(1, 200+1): 
    q = round((math.sqrt((2*C*D)/(H))), 3)
    print(f"{q}", end=", ")

print('}')
