# Program to output a given number of fibonacci sequence
def fibbo(digits):
    if(digits <= 1):
        return digits
    else:
        return (fibbo(digits-1) + fibbo(digits-2))

digits = int(input("Enter number of sequence:"))

print("Fibonacci sequence :")
for num in range(digits):
    print(fibbo(num))
