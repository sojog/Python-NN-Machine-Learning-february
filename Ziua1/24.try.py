def myFunction(num):

    try:                             # line 1
        return 10/num           # line 2
    except ZeroDivisionError:
        print('error')          # line 3
    finally:                                # line 4
        print ("The result is ")


print (myFunction(3))