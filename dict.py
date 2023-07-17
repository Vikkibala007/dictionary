n={"name":"vikki","age":"20","degree":"BE","dept":"CSE"}
while True:
    print(" 1. add key_value pair \n 2. delete key_value pair \n 3. get key_value pair \n 4: update key_value pair \n 5:exit from the program  ")
    wish = int(input("enter you wish using above::" ))
    if wish == 1 :
        key = input ("enter your key")
        value = input ("enter your value ")
        n[key]=value
        print("key_value pair added succesfully")
        print(n)
    elif wish == 5 :
        print("exting the program ************** see you with another execution **")
        break
    elif wish==2 :
        x=input("enter the key to delete :")
        if x in n :
            del n[x]
            print("key value pair deleted succesfully") 
            print(n)
        else :
            print("key value pair is not found ")
    elif wish== 3 :
        x=input("enter the key to get value :")
        if x in n :
            v=n[x]
            print("value is :",v)
        else :
            print("value not found in the dictionary ")

    elif wish == 4 :
        x=input("enter the key to update ")
        y=input("enter the value to update")
        n[x]=y
        print("the key value pair updated successfully")
        print(n)
        
    else:
        print("enter correct choice ")    