import datetime
def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):

    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)

    net_pay = float(total_hours) * float(hourly_rate) - tax

    return tax, net_pay

def get_name():

    name = input("Enter employee name: ")

    return name

def get_total_hours():

    total_hours = float(input("Enter total hours: "))

    return total_hours

def get_hourly_rate():

    hourly_rate = float(input("Enter hourly rate: "))

    return hourly_rate

def get_tax_rate():

    tax_rate = float(input("Enter tax rate (in %): "))

    return tax_rate

def get_gross_pay(total_hours, hourly_rate):

    gross_pay = float(total_hours) * float(hourly_rate)

    return gross_pay


def display_employee_info(from_date, to_date, name, total_hours, hourly_rate, tax_rate, tax, gross_pay, net_pay):

    print("----------------------------------------------------")
    print("From date:", from_date.strftime('%m/%d/%Y'))
    print("To date:", to_date.strftime('%m/%d/%Y'))
    print("Employee name:", name)
    print("Total hours:", total_hours)
    print("Hourly rate:", hourly_rate)
    print("Gross pay:", gross_pay)
    print("Tax rate:", tax_rate)
    print("Income tax:", tax)
    print("Net pay:", net_pay)

    print("----------------------------------------------------")

def display_total_info(total_dict):

    print("----------------------------------------------------")
    print("Total number of employees:", total_dict['total_employees'])
    print("Total hours:", total_dict['total_hours'])
    print("Total tax:", total_dict['total_tax'])
    print("Total gross pay:", total_dict['total_gross_pay'])
    print("Total net pay:", total_dict['total_net_pay'])

    print("----------------------------------------------------")

def get_from_and_to_dates():
    from_date = input("Enter from date in mm/dd/yyyy format:")
    from_date = datetime.datetime.strptime(from_date,"%m/%d/%Y").date()
    to_date = input("Enter to date in mm/dd/yyyy format:")
    to_date = datetime.datetime.strptime(to_date,"%m/%d/%Y").date()

    return from_date, to_date

def calculate_employees_taxes(employee_list, total_dict):
    for employee in employee_list:
        from_date, to_date,name, hours, hourly_rate, tax_rate = employee
        gross_pay = get_gross_pay(hours, hourly_rate)

        tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate, tax_rate)

        display_employee_info(from_date, to_date, name, hours, hourly_rate, tax_rate, tax, gross_pay, net_pay)

        # update total

        total_dict['total_employees'] += 1
        total_dict['total_hours'] += hours
        total_dict['total_tax'] += tax
        total_dict['total_gross_pay'] += gross_pay
        total_dict['total_net_pay'] += net_pay

def main():

    employee_list = []
    total_dict = {"total_employees" : 0, "total_hours" : 0,"total_tax":0,"total_gross_pay":0,"total_net_pay":0}
    while True:
        
        name = get_name()

        if name == "End":
            break
        # placed it below get name because no point in taking dates if the user name will be End
        from_date, to_date = get_from_and_to_dates()
        
        hours = get_total_hours()

        hourly_rate = get_hourly_rate()

        tax_rate = get_tax_rate()
        # just to start printing in new line once one user data insertion is completed
        print()
        employee_list.append([from_date, to_date,name, hours, hourly_rate, tax_rate])
    
    calculate_employees_taxes(employee_list, total_dict)
    # display total counts
    display_total_info(total_dict)

# import guard

if __name__ == "__main__":

    main()
