# a company decided to give bonus of 5% to employee ih his year of service is mote than 5yrs. ask user for their salary and year of service and print the net bonis amount
x = float(input('monthly pay:'))
y = float(input('years of service:')) 
if y > 5:
    pay = x * 1.05
    net_pay = pay + x
    print(f'This is your net pay on overtime {net_pay}')
else:
    print(f"This is your net pay {x}")
print('All done')