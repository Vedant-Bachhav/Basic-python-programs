# Program generates random password using random module
import random

alphabets=["a", "b" ,'c' ,"d" ,"e", "f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l", "m","n", 'o', 'p', 'q', 'r' ,'s', 't', 'u', 'v' ,'w','x' ,'y' ,'z']
random.shuffle(alphabets)

numbers=["0","1","2","3","4","5","6","7","8","9"]
random.shuffle(numbers)

special_chars=["@","#","$","^","&","*","?"]
random.shuffle(special_chars)

# the password is 12 digit

a1 = random.choice(alphabets)
a2 = random.choice(alphabets)
a3 = random.choice(alphabets)
a4 = random.choice(alphabets)

n1 = random.choice(numbers)
n2 = random.choice(numbers)
n3 = random.choice(numbers)
n4 = random.choice(numbers)

s1 = random.choice(special_chars)
s2 = random.choice(special_chars)
s3 = random.choice(special_chars)
s4 = random.choice(special_chars)


passwordlist=[a1,a2,a3,a4,s1,s2,s3,s4,n1,n2,n3,n4]


password1 = ''.join(passwordlist)
print("The unshuffled version : ",password1)


random.shuffle(passwordlist)
password2= ''.join(passwordlist)
print("The shuffled version is: ",password2)