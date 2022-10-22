from datetime import datetime

def GetEmpInfo():
    empname = input("Enter Employee Name: ")
    return empname

def GetTimeframe():
    firstday = input("Enter Start Date as mm\dd\yyyy: ")
    lastday = input("Enter Stop Date as mm\dd\yyyy: ")
    return firstday, lastday

def GetHoursWorked():
    hours = float(input("Enter Hours Worked: "))
    return hours

def GetHourlyRate():
    hourrate = float(input("Enter Hourly Rate: "))
    return hourrate

def GetTaxRate():
    taxrate = float(input("Enter Tax Rate as decimal: "))
    return taxrate

def CalcTaxNetPay(hours, hourrate, taxrate):
    grosspay = hours * hourrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmp = 0
    TotHours = 0.00
    TotGp = 0.00
    TotTax = 0.00
    TotNp = 0.00
    
    EmpFile = open("empdatafile.txt","r")
    while True:
        rundate = input ("Enter a start date for the report (MM/DD/YYYY) or ALL for complete data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Incorrect date format. Please re-enter:")
            print()
            continue
    while True:
        EmpDataFile = EmpFile.readline()
        if not EmpDataFile:
            break
        EmpDataFile = EmpDataFile.replace("\n", "")
        EmpData = EmpDataFile.split("|")
        firstday = EmpData[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(firstday, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
       
        lastday = EmpData[1]
        empname = EmpData[2]
        hours = float(EmpData[3])
        hourrate = float(EmpData[4])
        taxrate = float(EmpData[5])
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourrate, taxrate)
        print(firstday,lastday, empname, f"{hours:,.2f}", f"${hourrate:,.2f}", f"${grosspay:,.2f}", f"{taxrate:,.1%}", f"${incometax:,.2f}", f"${netpay:,.2f}")
        TotEmp += 1
        TotHours += hours
        TotGp += grosspay
        TotTax += incometax
        TotNp += netpay
        EmpTotals["TotEmp"] = TotEmp
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGp"] = TotGp
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNp"] = TotNp
        DetailsPrinted = True
    if (DetailsPrinted):
        PrintTotals (EmpTotals)
    else:
        print("No data on file to return.")

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Work: {EmpTotals["TotHours"]:,.2f}')
    print(f'Total Gross Pay: ${EmpTotals["TotGp"]:,.2f}')
    print(f'Total Income Tax: ${EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: ${EmpTotals["TotNp"]:,.2f}')

if __name__== "__main__":
    UserRole, UserName = Login()
    DetailsPrinted = False 
    EmpTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is invalid. Please re-enter.")
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("empdatafile.txt", "a+")
            while True:
                empname = GetEmpInfo()
                if (empname.upper() == "END"):
                    break
                firstday, lastday = GetTimeframe()
                hours = GetHoursWorked()
                hourrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDataFile = firstday + "|" + lastday + "|" + empname + "|" + str(hours) + "|" + str(hourrate) + "|" +str(taxrate) + "\n"
                EmpFile.write(EmpDataFile)

            EmpFile.close()
            printinfo(DetailsPrinted)
