# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108
total_paid = 0.0
months = 0

while principal > 0:
    if months == 0:
       actual_payment = payment + extra_payment
    elif months >= 12*5 : 
       actual_payment = 0
       actual_payment = extra_payment + payment
       print(actual_payment)
    else:
        actual_payment = 0
        actual_payment = payment
    principal = principal * (1+rate/12) - actual_payment
    total_paid = total_paid + payment
    months = months + 1
    print(months, total_paid, principal) 