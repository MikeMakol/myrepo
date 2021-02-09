
def sumProblem(x, y):
    sum = x + y
    sentence = "The sum of {} and {} is {}.".format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2,3)
    sumProblem(123456789,567832444)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

#print(sumProblem(2, 3))
main()