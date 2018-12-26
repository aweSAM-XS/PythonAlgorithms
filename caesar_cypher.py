
#This is a python program to decode and encode a caesar-cypher, given its key.

def encrypt(k):                                                                         #Function to encrypt a given string.
    n,i=0,0
    l="abcdefghijklmnopqrstuvwxyz"
    l=list(l)
    b=[]
    a=input("enter text to be encrypted: ")
    a=list(a)
    while(n<len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i=l.index(a[n].lower())
                i=(i+k)%26
                b.append(l[i].upper())
                n+=1
            else:
                i=l.index(a[n])
                i=(i+k)%26
                b.append(l[i])
                n+=1
        else:
            if(a[n]==' '):
                b.append(' ')
                n+=1
    print("The encrypted text is: ","".join(b))
       
def decrypt(k):                                                                         #Function to decrypt an encrypted string.
    n,i=0,0 
    l="abcdefghijklmnopqrstuvwxyz"
    l=list(l)
    b=[]
    a=input("Enter cipher to be decrypted: ")
    a=list(a)
    while(n<len(a)):
        if a[n].lower() in l:
            if a[n].isupper():
                i=l.index(a[n].lower())
                i=(i-k)%26
                b.append(l[i].upper())
                n+=1
            else:
                i=l.index(a[n])
                i=(i-k)%26
                b.append(l[i])
                n+=1
        else:
            if(a[n]==' '):
                b.append(' ')
                n+=1
    print("Cipher after decryption is: ","".join(b))

o=int(input("1.encrypt   2.decrypt   0.exit"))
while(o!=0):
    if(o==1):
        n=int(input("enter key"))
        encrypt(n)
    elif(o==2):
        n=int(input("enter key"))
        decrypt(n)
    else:
        print("enter valid option")
    o=int(input("1.encrypt 2.decrypt 0.exit"))