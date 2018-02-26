output=[]

output = [ord(chr) - 96 for chr in input('Secret Message: ')]
  
b = 0
code = []
c = [ord(chr) - 96 for chr in input('Message Key: ')]

if len(c) < len(output):
    c = c * len(output)

for word in output:
    letter = output[b] + c[b]
    code.insert(b ,int(letter))
    b = b + 1
   
e= input("Enter name for your message: ")
e= e + ".txt"    
print(code, file=open(e, "w+"))
print("Your message has been encoded, don't forget the key!")
input("Press enter to exit")