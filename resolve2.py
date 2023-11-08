#!/usr/bin/env python3

import socket
import sys

## Open file with filename as argument

#usage: python3 resolve2.py filename

txt_file = open(sys.argv[1], "r")
# Read all the lines or subdomains in the file
content_list = txt_file.readlines()
#Create a list called final

final= []

#Add contents of file to the list final

for i in  content_list:
        final.append(i.strip())


for n in final:
    try:
        print(socket.gethostbyname(n), n, sep = '       \t')

# Create a file called livehosts and add the resolvable hosts to the file

        write_file = open("./livehosts", "a")
        write_file.write(socket.gethostbyname(n)+' : \t'+ n + '\n')

    except:
        print("Hostname Not Live : ", '\t', n)
        continue
