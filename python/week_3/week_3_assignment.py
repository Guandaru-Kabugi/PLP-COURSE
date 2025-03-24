#task 1
def calculate_discount(price, discount_percent):
    convert_percent = discount_percent / 100
    if convert_percent >= 0.2:
        discount = convert_percent * price
        discounted_price = price - discount
        print (discounted_price)
    else:
        print (price)
    
calculate_discount(100, 30)
calculate_discount(100, 50)
calculate_discount(100, 10)
calculate_discount(100, 20)
    

#task 2
def calculate_discount():
    price = float(input("Enter price: "))
    discount_percent = float(input("Enter discount percentage as just a number with percent sign: "))
    convert_percent = discount_percent / 100
    if convert_percent >= 0.2:
        discount = convert_percent * price
        discounted_price = price - discount
        print (discounted_price)
    else:
        print (price)
    
calculate_discount()