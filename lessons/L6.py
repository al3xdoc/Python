while True :
    a = input('Enter the first variable:')
    b = input('Enter the second variable:')
 
    if a == "Stop":
        break  
 
    try :
        a = int(a)
        b = int(b)
  

    except ValueError:
        result = a + b 
        print("The string is:" result)

    else:
        result = a + b
        print("The sum of the variables is :", result)

