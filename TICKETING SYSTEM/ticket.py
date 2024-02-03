# Get user height to determine if user will be able to ride or not
try:
    user_height = float(input("Enter your height in meters: "))

    user_age = int(input("Please enter your age:"))
    
    max_height = 3.5
   
    


#detere=mine from height if user can ride or not
    
except ValueError :
    if user_height >= 3.5:
        print("Invalid Input !! Enter a number")

    

    
    
else:
        if user_height > 1.2 :
            print("You can aboard the roller coaster. Enjoy your experience")
    
        elif user_height <= 1.2 :
            print("Sorry you do not meet the required height. You cannot go aboard the roller coaster!!")
            
            
## Ticketing system 
#--------- AMount to be paid




        amount = (5, 7 , 12, 0)


#--12 year olds and below $5


        if user_age < 12 :
            bill = amount[0]
            print(f'Your ticket costs $ {bill}')
    
        elif user_age > 12 and user_age <18 :
            bill = amount[1]
            print(f'Your ticket costs $ {bill}')
    
    
        elif user_age >= 18 and user_age < 45:
            bill = amount[2]
            print(f'Your ticket costs $ {bill}')
    
    
        else :
            bill = amount[3]
            print(f'Your ticket costs $ {bill}')


        wants_photo = input("Do you want a photo ? Y/N \n")

        if wants_photo == 'Y':
            bill += 3
            print(bill)
            
        else:
            print(f'Your ticket cost $ {bill}')
     
       
    