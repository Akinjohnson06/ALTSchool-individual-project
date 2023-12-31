#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to calculate total sales for the day
# TS meaning Total sales
def calculating_TS(morning_sales, evening_sales):
    total_sales = morning_sales + evening_sales
    return total_sales


# In[2]:


# Function to calculate worker's salary
# WS meaning Workers salary
def calculating_WS(hourly_rate, hours_worked):
    worker_salary = hourly_rate * hours_worked
    return worker_salary


# In[3]:


# Function to calculate profit
def calculating_profit(total_sales, total_cost):
    profit = total_sales - total_cost
    return profit


# In[4]:


# Function to calculate tips for a shift
# ST meaning shift tips
def calculating_ST(shift_sales):
    tips = 0.02 * shift_sales
    return tips


# In[5]:


# Function to calculate total tips for the day
# TT meaning Total tips 
def calculating_TT(morning_sales, evening_sales):
    total_tips = calculating_ST(morning_sales) + calculating_ST(evening_sales)
    return total_tips


# In[6]:


# User interface function
def menu():
    print("\nWELCOME TO THE ACCOUNTING AUTOMATION SYSTEM!!! (AAS) \n") #Abbreviated Accounting Automation System to (ASS)
    print('AVAILABLE MENU') # Heading of the Menu
    print('--------------') # I tried to underline 'Available Menu'. Didn't really turn out great
    print('Choose your menu below:') # Simply tells users to pick an option
    print('1. Total Sales') # option one for Total Sales
    print('2. Workers Salary') # option two for Workers Salary
    print('3. Profit') # option three for profit
    print('4. Total Tips') # option four for Total Tips
    print('5. Exit AAS') # # option five to Exit program (ASS)


# In[7]:


# Main codes
while True:
    menu()
    choice = input("\nSelect a choice from the menu (1-5): ")

    if choice == '1':
        morning_sales = float(input("Enter morning sales: "))
        evening_sales = float(input("Enter evening sales: "))
        print('\nINPUT RECEIVED.\nCHECK BELOW FOR RESULT!!!!!')
        total_sales = calculating_TS(morning_sales, evening_sales)
        print("\nTotal sales for the day: =N=", total_sales) # =N= is supposed to be a Naira sign

    elif choice == '2':
        hourly_rate = float(input("Enter hourly rate: "))
        hours_worked = float(input("Enter hours worked: "))
        print('\nINPUT RECEIVED.\nCHECK BELOW FOR RESULT!!!!!')
        worker_salary = calculating_WS(hourly_rate, hours_worked)
        print("\nWorker's salary: =N=", worker_salary) # =N= is supposed to be a Naira sign

    elif choice == '3':
        total_sales = float(input("Enter total sales: "))
        total_cost = float(input("Enter total cost: "))
        print('\nINPUT RECEIVED.\nCHECK BELOW FOR RESULT!!!!!')
        profit = calculating_profit(total_sales, total_cost)
        print("\nOutcome: =N=", profit) # =N= is supposed to be a Naira sign
        if total_sales < total_cost:
            print('There appears to be a Loss. Hence its Non-Profitable')
        elif total_sales > total_cost:
            print('There appears to be a Profit. The business is Profitable')
        else: #total_sales == total_cost:
            print('There appears to be a break even. Now we start making Profit/Loss') #depending on how they manage the business 
# A break even is a point where a business makes zero profit.
# Its a point where business cover all expenses and start making a profit


    elif choice == '4':
        morning_sales = float(input("Enter morning sales: "))
        evening_sales = float(input("Enter evening sales: "))
        print('\nINPUT RECEIVED.\nCHECK BELOW FOR RESULT!!!!!')
        total_tips = calculating_TT(morning_sales, evening_sales)
        print("\nTotal tips for the day: =N=", total_tips)

    elif choice == '5':
        print('\nINPUT RECEIVED.')
        print("\nExiting the program.")
        print("Exiting the program..")
        print("Exiting the program...")
        print("AAS has been terminated!!!\n")
        print('GOODBYE!!!!')
        break

    else:
        print("Invalid choice. Please try again.")


# # CHALLENGES ENCOUNTERED
# 
# I didn't really face challenges in defining much functions. The main challenge was in the main code especially with usings a while loop. That being said, below are the list of challenges I faced while doing the project:
# 
# 1. The very first challange i encounterd was critical thinking. I could'nt understand the questions properly. I was very confused
# 
# 2. I had a problem designing the Menu list. I couldn't figure out what should come next on the menu. I also tried underlining some items on the menu but it didnt turn out as I expected it to. Also, it took me a while to remember how to break into another line (\n).
# 
# 3. In the main code, I kept on putting my choice as an Interger instead of a string (choice = '1'). I spent about 2 days trying to figure it out. 
# 
# 4. I was a bit confused whether to break code immediately after the result of the choice is selected or just give a different option to break code. I guess I shoud read questions very well.
# 
# 5. At choice number 3, where you have the profit, i noticed that when you break even(No profit and no loss), It doesn't actually let you know, so i included it in the code.
# 
# 6. There is a part of the question that talks about Error Handling and till now, I haven't figures out what it means

# In[ ]:




