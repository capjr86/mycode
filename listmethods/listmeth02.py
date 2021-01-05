#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
# i removed 443 from the proto2 list
proto2.pop(2)
print(proto2)
icecream= ["flavors", "salty"]
icecream.append(99)
user = input("What is your name?")
print(f"{icecream[2]} {icecream[0]} and {user}, chooses to be {icecream[1]}")
