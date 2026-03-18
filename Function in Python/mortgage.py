"""

"""
def mortgage(total, payment, interest):
    interest = (interest / 12) / 100
    month = 0
    paid = 0
    total_interest = 0
    while total >= 0:
        total_interest = (total * interest) + total_interest
        total = total - payment
        total = (total * interest) + total
        paid = paid + payment
        month += 1
        print(total)
    year = month / 12
    return year, paid, total_interest

price = 100000
interest = 7
payment = 1400

response = mortgage(price, payment, interest)

print(f'Repayment Years: {response[0]}')
print(f'Total Paid: {response[1]}')
print(f'Interest Paid: {response[2]}')