num = int(input('Desejo ver a tabuada do número: '))
print("*" * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print("*" * 12)
