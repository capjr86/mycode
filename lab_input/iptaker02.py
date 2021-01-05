#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)

vendor_name = input("Please enter the vendor name:")

print("The vendor you entered is:", vendor_name)

user_name = input("What is your name?")

day_of_week = input("What day of the week is it?")

print("Hello", user_name +"!","Happy", day_of_week +"!")
