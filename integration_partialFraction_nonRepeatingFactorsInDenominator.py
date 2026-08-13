import math

def integrate(coeffecientOf_x:float, degreeOf_x:int, numeratorConstant:float, degreeOfDenominator:int, factorCoeffecientOf_x:list, factorConstant:list):
    answer = ""
    answer_partial = ""
    constant_denominator = 1

    # To check whether can we use this type of partial fraction method to solve
    if degreeOfDenominator <= degreeOf_x:
        print("The degree of the denominator must be greater than the degree of numenator")
        return 0
    
    for i in range(degreeOfDenominator):
        for j in range(degreeOfDenominator):
            if j == i:
                continue

            constant_denominator *= (factorCoeffecientOf_x[j] * (-1) * (factorConstant[i] / factorCoeffecientOf_x[i]) + factorConstant[j])

        constant_numenator = (coeffecientOf_x * math.pow(((-1) * (factorConstant[i] / factorCoeffecientOf_x[i])), degreeOf_x)) + numeratorConstant

        constant = constant_numenator / constant_denominator
        Constant = round(constant, 4)

        answer_partial += '[ ' + "(" + str(Constant) + ")" + ' * ' + "log|" + str(factorCoeffecientOf_x[i]) + 'x' + ' + ' + '(' +str(factorConstant[i]) + ')' + '|' + ' ]' + ' + '

        # To reset the constant denomenator value to 1 for the next loop
        constant_denominator = 1

    # To add the integration constatn 'C'
    answer = answer_partial + 'C'
    return answer

#------------------------------------------------Main()------------------------------------------------

print("------------------------------------------------------------------------------------------")
print("   Non-repeated linear fractors in denominator type Partial Fraction Method Integration")
print("------------------------------------------------------------------------------------------")
print("\n\n")

a = []
b = []

# To make sure a valid number is entered
while True:
    try:

        n = int(input("Enter the degree of denominator : "))
        k = int(input("Enter the degree of numenator   : "))

        # To make sure we can use this type of partial fraction method integration
        while n < k:
            print("\nThe degree of the denominator must be greater than the degree of numenator\n")

            n = int(input("Enter the degree of denominator : "))
            k = int(input("Enter the degree of numenator   : "))

        break

    except ValueError:
        print("\nEnter a valid number\n")


print()

#To make sure a valid number is entered
while True:
    try:
        p  = float(input("Enter the value of numerator Coeffecient of x : "))
        q  = float(input("Enter the numerator additive constant         : "))
        break

    except ValueError:
        print("\nEnter a valid number\n")
print()

# To continuously append the list of denominator coeffecient of x and additive constant for every term
for i in range(n):

    # To make sure a valid number is entered
    while True:
        try:
            ai = float(input(f"Enter the {i + 1} factor coefficient of x : "))
            bi = float(input(f"Enter the {i + 1} factor consant          : "))
            break

        except ValueError:
            print("\nEnter a valid number\n")

    a.append(ai)
    b.append(bi)

Answer = integrate(p, k, q, n, a, b)

print('\n\nAnswer =', Answer)
        