#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
# close your file
dnsfile.close()


# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
    # loop over lines
    for svr in dnsfile:
        #print and end without a newline
        print(svr, end="")
# no need to close our file - closed automatically

