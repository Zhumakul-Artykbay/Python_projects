import random
dic = {}
ok = True
while ok:
        
    print("""
1. Create an account
2. Log into account
0. Exit
    """)   
    case = int(input())
    
    if case == 1:
        
        card_number = "400000"
        randomlist = random.sample(range(0, 10), 10)
        string_list = [str(i) for i in randomlist]
        card_number += "".join(string_list) 
        randomlist_PIN = random.sample(range(0, 10), 4)
        string_pin_list = [str(i) for i in randomlist_PIN]
        PIN  = "".join(string_pin_list)
        print(f"""
Your card has been created
Your card number:
{card_number}
Your card PIN:
{PIN}
        """.format(card_number, PIN))
        dic[card_number] = PIN
    elif case == 2:
        print("Enter your card number:")
        input_card_num = input()
        print("Enter your PIN:")
        input_PIN = input()
        
        if input_card_num in dic and dic[input_card_num] == input_PIN:
            
            print("You have successfully logged in!")
            balance = 0
            logged = True
            
            while logged:
                print("""
                1. Balance
                2. Log out
                0. Exit
                """)
                
                log_case = int(input())
                
                if log_case == 1:
                    print(f"Balance: {balance}") 
                elif log_case == 2:
                    print("You have successfully logged out!")
                    logged = False
                elif log_case == 0:
                    logged = False
                    ok = False                    
        else:
            print("Wrong card number or PIN!")
    elif case == 0:
        ok = False

print("Bye!")           
    