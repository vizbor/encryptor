# -*- coding: utf-8 -*-
"""
Code Breaker
Created on Mon Feb 26 21:22:45 2018

@author: Josh
"""
import secrets as sec
f=[]
c=[]
k=(int(input("Number Here: ")))

d=str(sec.randbits(k))
f.append(d)
   
print(f)    

for x in range(256):
    c=d.split(",")

c=int(d)   
print(c)



output=[]

output = [ord(chr) - 96 for chr in input('Secret Message: ')]
  
b = 0
code = []
#c = [ord(chr) - 96 for chr in input('Message Key: ')]

#if len(c) < len(output):
 #   c = c * len(output)

for word in output:
    letter = output[b] + c
    code.insert(b ,int(letter))
    b = b + 1
   
e= input("Enter name for your message: ")
e= e + ".txt"    
print(code, file=open(e, "w+"))
print("Your message has been encoded, don't forget the key!")
input("Press enter to exit")