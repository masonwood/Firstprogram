print('How much yen do you want to convert to dollars?')
yen = input()
usd = float(yen)/129.71
usd = (round(usd, 2))
print(f'Your {yen}yen is equal to {usd} usd')