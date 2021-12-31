UNIT_PRICE = 100
qty = int(input('quantity of good:'))
cst = qty * UNIT_PRICE
if cst > 1000:
    Actual_cost = cst * 0.9
    print(f'cost after discount is {Actual_cost}')
else:
    print(f'the actual cost is {cst}')
