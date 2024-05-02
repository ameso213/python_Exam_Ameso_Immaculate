#a)program to ask for employees salary and their year of service

def bonus_for_employees():
    run = 1
    while run == 1:
        salary = int(input("Please enter your salary: "))
        years_of_service = int(input("Please enter your years of service: "))
        
        if years_of_service > 4:
            bonus = salary * 0.08
        elif years_of_service == 3:
            bonus = salary * 0.05
        else:
            bonus = 0  # No bonus
            
     # Calculating the  net salary
        net_salary = salary + bonus  
        return bonus, net_salary  

bonus, net_salary = bonus_for_employees()
print("Net bonus amount:", bonus)
print("Net salary amount:", net_salary)



