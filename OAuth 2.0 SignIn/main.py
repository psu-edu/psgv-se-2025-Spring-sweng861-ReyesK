
import os


loop=()

print('Press "1" to sign in with Google or "2" to for LinkedIn.')
signInNum=int(input())


    
if signInNum == 1:
    os.system("python googleAuth.py")
    loop=True
    
elif signInNum == 2:
    os.system("python linkedinAuth.py")
    loop=True
    
elif signInNum != 1 or 2:
    loop = False



while loop == False:

        print("Please enter a valid number.\n1 for Google or 2 for LinkedIn.")
        
        signIn=int(input())
        
        if signIn == 1:

            os.system("python googleAuth.py")
            loop=True
            
        elif signIn == 2:
            os.system("python linkedinAuth.py")
            loop = True
            
        elif signIn!= 1 or 2:
            loop = False

    
        

