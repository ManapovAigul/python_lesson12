# elif x % 5 == 0:
#     print('Five')
# else:
#     print('Zero')
# a =[1, 2, 3, 4, 5]

obshaya_summa_za_gody = 0
def bank(a, years):
    years = years + 1
    for i in range(1, years):
        obshaya_summa_za_god = a * 0.1 + a
        a = obshaya_summa_za_god
    return a

def bank1(a, years):
    for year in range(years):
        a *= 1.1
    return a

if __name__ == '__main__':
   print(a)

