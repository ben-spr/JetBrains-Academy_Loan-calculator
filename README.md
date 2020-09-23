# Loan-calculator
Loan calculator for the JetBrains Academy course, executable via terminal
When running it via terminal, you can specify the following:
--type (required): type of the monthly payments, 'annuity' for constant payments, 'diff' for differentiated, decreasing payments
--interest (required): yearly interest rate in %
--principal : desired loan principal
--payment (only viable if type != 'diff'): desired monthly payment
--periods : desired number of months over which the loan should be repaid


Specify any 4 of the 5 parameters to calculate the missing one. Type and interest are mandatory inputs.
