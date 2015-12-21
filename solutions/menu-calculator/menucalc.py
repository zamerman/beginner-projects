# Menu Calculator
# Python 3.5.10
# Written by rsz


# create dictionary
menu = {'Chicken Strips': 3.50, 'French Fries': 2.50, 'Hamburger': 4.00,
        'Hotdog': 3.50, 'Large Drink': 1.75, 'Medium Drink': 1.50,
        'Milk Shake': 2.25, 'Salad': 3.75, 'Small Drink':1.25}
        
# list to call dictionary values 
menulist = ['Chicken Strips','French Fries', 'Hamburger', 'Hotdog',
            'Large Drink' ,'Medium Drink' ,'Milk Shake', 'Salad', 'Small Drink']

for i in menulist:
    print(i + ':' +  ' $' + str(menu[i]))

# check for amount of items
def count(Order):
    final = ""
    for i in range (1, 10):
        if order.count(str(i)) > 0:
            print(str(menulist[i-1]) + ': ' +  str(order.count(str(i))))
        
# main loop
while True:
    order = str(input('\nEnter the order: '))
    total = 0
    count(order)

    for i in order:
        if int(i) == 0:
            print('Enter correct values 1-9')
            break
        total = total + float(menu[menulist[int(i)-1]])
        

    print('The total amount is', total)
    
