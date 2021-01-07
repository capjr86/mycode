#!/usr/bin/env python3

def calc():
    while True:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            op = input("Please enter +, - , *, or /: ")
        
            if op == "+":
                print(n1, " + ", n2, "=", n1 + n2)
                break
    
            elif op == "-":
                print(n1, " - ", n2, "=", n1 - n2)
                break

            elif op == "*":
                print(n1, " * ", n2, "=", n1 * n2)
                break
    
            elif op == "/":
                print(n1, " / ", n2, "=", n1 / n2)
                break

        except:
            print("Please choose a valid number and operator")
                
calc()        
