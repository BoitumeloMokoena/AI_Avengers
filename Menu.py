def on_display():
    print("Welcome to Tax Buddy\n\n")
    print("Menu\n")
    print("1. Tax Estimation\n2.Exit")

def get_companyName():
    companyName=input(str("Input your company name: "))


def assests():
    assestsValue=input(float("Input the toatal depreciation and armotization value of your assests: "))
    
def income():

    income=input(float("Please enter your income: ")) 

    while(income <= 83333):
        print("You are not required to register for VAT")
        break
        

def expenses():
    expense=input(float("Please enter your total expenses: "))


def calculate_taxable_income(income, assets, expenses):
    gross_income = income - (assets + expenses)
    return income

def get_business_info():
    on_display()





