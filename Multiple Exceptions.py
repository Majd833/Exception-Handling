try:
    num1, num2=eval(input("Enter two numbers separated by a comma:"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Division by zero is an ERROR!!")
except SyntaxError:
    print("You should enter your numbers separated by a comma ,like this:1,2")
except:
    print("You should enter numbers")
else:
    print("No exception")
finally:
    print("This will always run no matter what")