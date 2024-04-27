def on_display():
    print("Welcome to Tax Buddy\n\n")
    print("Menu\n")
    print("1. Tax Estimation\n2.Exit")

    option = input(int("Enter an option between 1 and 2"))

    while(option == 1):
        tax_estimation()
    else:
        print("Exiting program...")
        

def get_companyName():
    companyName=input(str("Input your company name: "))


def get_country():
    country=input(str("Please enter your country: "))

def get_assests():
    assestsValue=input(float("Input the toatal depreciation and armotization value of your assests: "))
    
def get_income():

    income=input(float("Please enter your income: ")) 

    while(income <= 83333):
        print("You are not required to register for VAT")
        break
        

def get_expenses():
    expense=input(float("Please enter your total expenses: "))


def calculate_taxable_income(income, assets, expenses):
    gross_income = income - (assets + expenses)
    return income*0.28

def tax_estimation():
    get_companyName()
    get_country()
    get_assests()
    get_income()
    get_expenses()
    calculate_taxable_income()






