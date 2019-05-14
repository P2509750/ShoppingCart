import math
import sys

def shopping():
    print("============| Options |============")
    print("|        [1] --> Select items     |")
    print("|        [q] --> Quit             |")
    print("===================================")
    
    
    prices={"coffee":5,
            "milk":0.71,
            "tea":3,
            "sugar":0.69,
            "water":0.45,
            "orange":0.8,
            "beer":1.30,
            "chocolate":1,
            "onion":0.1,
            "lemon":0.3}
    
    basket=[]
    count=0
    total=0
    
    select=input("What would you like to do?: ").lower()
    
    if select=="q":
        print("See you next time! BYE :)")
        sys.exit()
    elif select!="1":
        print("Input Error! You have to chose between [1] or [q]")
        sys.exit()
        
    while True:
        
            print("=======================| Products |=======================")
            print("|		1. Coffee      200g    £5.00		 |")
            print("|		2. Milk       1L      £0.71		 |")
            print("|		3. Tea        750g    £3.00              |")
            print("|		4. Sugar      1Kg     £0.69              |")
            print("|		5. Water      2L      £0.45              |")
            print("|		6. Orange     500g    £0.80              |")
            print("|		7. Beer       500ml   £1.30              |")
            print("|		9. Chocolate  200g    £1.00              |")
            print("|		8. Onion              £0.10/each         |")
            print("|		10. Lemon             £ 0.30/each        |")
            print("======================| Instruction |=====================")
            print("|  Type name of item [E.g.'coffee'] to add it into basket |")
            print("|                         or                             |")
            print("|  Type [checkout] to pay for your products              |")
            print("==========================================================")
                        
            select=input("Please type your items or [checkout] to pay: ")
            
            if select=="checkout":
                print("Total to pay:",total)
                payment=float(input("Please pay now: "))
                while True:
            
                    if payment==total:
                        print("Thank you! Good Bye :)")
                        break
                      
                    elif payment > total:
                        calc=payment-total
                        print("Thank you! Don't forget to take your change! BYE :) \n change:",calc)
                        break
                        
                    elif payment < total:
                        print("OOPS! Something is missing! Try to pay again:")
                        payment=int(input("Pay again:"))

                break
            
            quantity=int(input("Please enter the quantity: "))
            count+=quantity
            total+=int(quantity)*prices[select]
            basket.append(str(select))
            print("Your basket contain",count,"items with total price:£",total)
        
shopping() 
