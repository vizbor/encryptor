
e=input("File Name here: ")
k = e + ".txt"

file = open(k, "r")

f = file.read()
code=[]
code = list(map(int, f[1:-2].split(",")))

file.close()
c=[]
c = [ord(chr) - 96 for chr in input('Type the Code Word: ')]
if len(c) < len(code):
    c = c * len(code)
mess = []    
a = 0
for number in code:
    character = number + 96
    character = character - c[a]
    character = chr(character)
    mess.append(character)
    a = a + 1
 
mess = ''.join(mess[0:])

e = e + "decoded"+".txt"

print (mess)
print(mess, file=open(e, "w+"))
input("Press enter to exit")
