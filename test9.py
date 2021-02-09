from test import printme
import importlib
importlib.reload(test)

printme("Zara")
print("Azima")



def fib(n):  # return fibonacci series upto n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    f = fib(100)
   # print(f)
#content = dir(f)
#print(content)
