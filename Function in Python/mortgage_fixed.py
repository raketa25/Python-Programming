"""
this is a full mortgage payment simulation with edge cases taken into account.
"""
def mortgage(total, payment, interest):
    interest = (interest / 12) / 100
    month = 0
    paid = 0
    total_interest = 0
    if payment > (total * interest):
        while total >= 0:
            total_interest = (total * interest) + total_interest
            total = total - payment
            total = (total * interest) + total
            paid = paid + payment
            month += 1
        year = month / 12
    else:
        print('Minimum Payment is Too Low to EVER be Paid off')
        year = 'error'
        paid = 'error'
        total_interest = 'error'
    return year, paid, total_interest

price = int(input("Enter the initial mortgage:> "))
interest = int(input("Enter the interest rate:> "))
payment = int(input("Enter the payment installment:> "))

response = mortgage(price, payment, interest)

print(f'Repayment Years: {response[0]}')
print(f'Total Paid: {response[1]}')
print(f'Interest Paid: {response[2]:.3f}')