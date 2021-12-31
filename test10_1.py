# Rewrite your pay program using try and except so that you rprogran handles non-numeric input gracefully by printing a messsage and exiting the program. The
hours = input('Enter Hours:')
rate = input('Enter Rates:')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
print(fh, fr)
if fh > 40:
    print('overtime')
    f_pay = fh * fr
    otp = (fh-40) * (fr * 0.5)
    print(f_pay,otp)
else:
    print('Regular')
    f_pay = fh * fr
    otp = 0
    print(f_pay,otp)
actual_pay = f_pay + otp
print('Pay:',actual_pay)

# another (simpler) way to run the same question without an error message on a wrong input (the previous is a better program)
hr = float(input('Hours worked:'))
rt = float(input('rate per day:'))
if hr > 40:
    print('overtime')
    ovth = hr - 40
    ovtr = 1.5 * rt
    ovtp = (40 * rt) + (ovth * ovtr)
    print('pay: ',ovtp)
else:
    print('Regular')
    tp = hr * rt
    print('pay: ',tp)
print('All Done')