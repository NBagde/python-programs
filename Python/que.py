l=[]
while True:
    c=int(input('''
      1 Push Elements
      2 Pop First Elements
      3 Front Element
      4 Last Elements
      5 Display queue
      6 Exit
      '''))
    if(c==1):
      n=input("Enter the value:-");
      l.append(n)
      print(l)
    elif(c==2):
      if(len(l)==0):
        print("Empty queue")
      else:
        del l[0]
        print(l)
    elif(c==3):
      if(len(l)==0):
        print("Empty queue")
      else:
        print("First queue value:-",l[0])
    elif(c==4):
      if(len(l)==0):
        print("Empty Queue")
      else:
        print("Last queue value:-",l[-1])
    elif(c==5):
       print("Display queue",l)
    elif(c==6):
       break;
    else:
       print("Invalid Opr...")
         
    
