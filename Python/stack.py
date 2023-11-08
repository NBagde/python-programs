#stack(LIFO)lastin/firstout,(fILO)firstin/lastout
l=[]
while True:
    c=int(input('''
    1 Push elements
    2 Pop elements
    3 Peek element(disply last element
    4 Display stack 
    5 exit
    '''))
    if c==1:
       n=input("Enter the value");
       l.append(n)
       print(l)
    elif c==2:
       if(len(l)==0):
          print("Empty Stack")
       else:
          p=l.pop()
          print(p)
          print(l)
    elif c==3:
          if(len(l)==0):
            print("Empty Stack")
          else:
            print("Last stack value",l[-1])
    elif c==4:
       print("Display Stack",l)
    elif c==5:
       break;
    else:
       print("invalid operation")
             
           
