import bank
a=bank.Bank()
print('welcome to online bank service ')
print('if you want to use our service click Yes')
n=input('')
if(n=='Yes'):
    print('click numbers what you want')
    print('       1.NEW ACCOUNT       ')
    print('       2.REPORT            ')
    print('       3.DEPOSIT           ')
    print('       4.WITHDRAW          ')
else:
    print('thanks for your visit')
a.func()
