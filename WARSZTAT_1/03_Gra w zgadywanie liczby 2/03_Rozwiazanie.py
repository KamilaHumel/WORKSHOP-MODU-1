def gra():
    print('Pomyśl liczbę od 1 do 1000, a ja zgadnę ją w max. 10 próbach')
    min = 0
    max = 1000
    guess = int((max - min) / 2 + min)
    print(f"Zgaduję: {guess}")
    help = input('Podpowiedź za dużo / za mało / zgadłeś): ')

    i = 9

    try:
        for _ in range(10):
            while help !="zgadłeś":
                if help == 'za mało' and i != 0:
                    min = guess
                    guess = int((max - min) / 2 + min)
                    print(f"Zgaduję: {guess}")
                    help = input('Podpowiedź za dużo / za mało / zgadłeś): ')
                    i -= 1
                    print(i)


                elif help == 'za dużo' and i != 0:
                    max = guess
                    guess = int((max - min) / 2 + min)
                    print(f"Zgaduję: {guess}")
                    help = input('Podpowiedź za dużo / za mało / zgadłeś): ')
                    i -= 1
                    print(i)
                #elif i == 0:
                   # print('Przegrałem!')
                   # break

                else:
                    print('Nie oszukuj!')
                    print(f"Zgaduję: {guess}")
                    help = input('Podpowiedź za dużo / za mało / zgadłeś: ')

            print('Wygrałem!')



    except ValueError:
        print("It's not a number!")


gra()
