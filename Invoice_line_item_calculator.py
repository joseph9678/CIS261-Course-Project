def get_price():
    while True:
        try:                                              #Try block. ??? 
            price = float(input("Enter price:  "))   #float decimaled number. 
            return price
        except ValueError:              #data validation         #value error Catch all 
            print("Invalid decimal number. Please try again.")



def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quatity:   "))  #interger
            return quantity
        except ValueError:  #data validation
            print("Invalid interger. Please try again. ")



def main():
    print("The Invoice Line Item Calculator\n")

    answer = 'y'
    while answer.lower() == "y":
        price = get_price()
        quantity = get_quantity()

        total = price * quantity

        print()
        print("PRICE:  ", f"{price: .2f}") #formatting = print with 2 decimals. "{price: .2f}
        print("QUANTITY: ",  quantity)
        print("TOTAL:  ", f"{total: .2f}")
        answer = input("Enter another line item? (y/n):  ")
        print()

    print("Bye!")

 
if __name__ == "__main__":
    main()
