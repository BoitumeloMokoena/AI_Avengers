def on_display():
    print("Welcome to Tax Buddy\n\n")
    print("Menu\n")
    print("1. Tax Estimation\n2.Exit")

def get_companyName():
    companyName=input(str("Input your company name: "))
    return companyName

def assests():
    assestsValue=input(float("Input the total depreciation and armotization value of your assests: "))
    return assestsValue

def income():
    income=input(float("Please enter your income: ")) 
    while(income <= 83333):
        print("You are not required to register for VAT")
        break
    else:
        return income
        
def expenses():
    expense=input(float("Please enter your total expenses: "))
    return expense

def yearsInBusiness():
    noYears=input(int("Please enter the number of years you have been in business: "))
    while noYears<1:
        return ("You do not to pay tax!")
    else:
        return noYears

def get_EmpLessThan30():
    empLessThan30=input(int("How many less than 30 years employees do you have?: "))   

def calculate_taxable_income(income, assets, expenses):
    gross_income = income - (assets + expenses)
    return gross_income * 0.28

def get_business_info():
    on_display()




