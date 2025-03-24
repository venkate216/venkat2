a =int (input("enter a first number:"))
b=int (input("enter a second number:"))
operation=input ("add/sub/multi/div:")
if (operation=="add"):
    print (a+b)

elif (operation=="sub"):
     print (a-b)

elif (operation=="multi"):
    print (a*b)

elif (operation=="div"):
    print (a/b)

else:
    print ("invalid operation")
