import math
import argparse
import sys
# import numpy

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["annuity", "diff"], help="Choose the type of monthly payment: 'annuity' or 'diff'", required=True)
parser.add_argument("-a", "--payment", type=int, help="Choose a monthly payment if you selected type 'annuity'")  # , default=-1)
parser.add_argument("-p", "--principal", type=float, help="Specify the loan principal in $")
parser.add_argument("-n", "--periods", type=int, help="Specify over how many months you want to pay back the loan")
parser.add_argument("-i", "--interest", type=float, help="Put in the yearly loan interest rate in %") # , required=True)
user_input = parser.parse_args()

# print(user_input)

if (user_input.type == 'diff' and user_input.payment is not None) or user_input.interest is None or not len(sys.argv) == 5:
    print('Incorrect parameters')
    sys.exit() # 'Incorrect parameters')

i = user_input.interest / (100 * 12)
overpayment = 0
if user_input.type == 'diff' and user_input.payment is None and len(sys.argv) == 5:
    D_m = [0] * user_input.periods
    for m in range(user_input.periods):
        D_m[m] = int(math.ceil(user_input.principal / user_input.periods + i * (user_input.principal - (user_input.principal * m) / user_input.periods)))
        print('Month {}: payment is {}$'.format(m+1, D_m[m]))
    overpayment = sum(D_m) - int(user_input.principal)
    print('Overpayment = {}$'.format(overpayment))

elif user_input.type == 'annuity' and user_input.interest is not None and len(sys.argv) == 5:
    if user_input.principal is None:
        principal = int(user_input.payment / ((i * (1 + i)**user_input.periods) / ((1 + i)**user_input.periods - 1)))
        print('Your loan principal is going to be {}$!'.format(principal))
        overpayment = user_input.payment * user_input.periods - int(principal)
    elif user_input.payment is None:
        payment = math.ceil(user_input.principal * (i * (1+i)**user_input.periods) / ((1+i)**user_input.periods - 1))
        print('Your monthly payment = {}$!'.format(math.ceil(payment)))
        overpayment = user_input.periods * int(payment) - int(user_input.principal)
    elif user_input.periods is None:
        n = math.log(user_input.payment / (user_input.payment - i * user_input.principal), (1 + i))
        n = math.ceil(n)
        years = n // 12
        months = n % 12
        str_and = ' and '
        if years == 0:
            str_years = ''
            str_and = ''
        elif years == 1:
            str_years = '1 year and '
        else:
            str_years = '{} years'.format(int(years))

        if months == 0:
            str_months = ''
            str_and = ''
        elif months == 1:
            str_months = '1 month'
        else:
            str_months = '{} months'.format(int(months))

        str_time = str_years + str_and + str_months
        print('It will take {} to repay this loan!'.format(str_time))
        overpayment = int(n) * user_input.payment - int(user_input.principal)
    print('Overpayment = {}$'.format(overpayment))
#
