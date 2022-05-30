from random import randint

def gra():
    komp_los = randint(0, 100)
    gracz_num = input('Guess the number: ')

    try:
        while komp_los != int(gracz_num):
            if komp_los > int(gracz_num):
                print("To small!")
                gracz_num = input('Guess the number: ')

            elif komp_los < int(gracz_num):
                print("To big!")
                gracz_num = input('Guess the number: ')
        print("You win!")

    except ValueError:
        print("It's not a number!")

gra()
