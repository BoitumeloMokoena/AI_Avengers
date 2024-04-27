def on_display():
    print("Welcome to Tax Buddy\n\n")
    print("Menu\n")
    print("1. Tax Estimation\n2. Exit\n")
    choice = int(input("Choose option: "))
    if choice == 1:
        tax_estimation()
    elif choice == 2:
        print("Exiting...")
        return
    else:
        print("Invalid option")
def get_companyName():
    companyName = input("Input your company name: ")
    return companyName
def get_country():
    country = input("Please enter your country: ")
    return country
def get_assets():
    assetsValue = float(input("Input the total depreciation and amortization value of your assets: "))
    return assetsValue
def get_income():
    incomeValue = float(input("Please enter your income: "))
    while incomeValue <= 83333:
        print("You are not required to register for VAT")
        break
    else:
        return incomeValue
def get_expenses():
    expenseValue = float(input("Please enter your total expenses: "))
    return expenseValue
def calculate_taxable_income(income, assets, expenses):
    gross_income = income - (assets + expenses)
    return gross_income * 0.28
def tax_estimation():
    company_name = get_companyName()
    country = get_country()
    assets = get_assets()
    income = get_income()
    expenses = get_expenses()
    taxable_income = calculate_taxable_income(income, assets, expenses)
    print("Taxable Income:", taxable_income)
def get_business_info():
    on_display()
get_business_info()
