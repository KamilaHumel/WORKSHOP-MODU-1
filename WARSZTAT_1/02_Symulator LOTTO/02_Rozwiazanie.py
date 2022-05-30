from random import randint, shuffle


def gra():
    a_gracz = input('Podaj pierwszą liczbę: ')
    b_gracz = input('Podaj drugą liczbę: ')
    c_gracz = input('Podaj trzecią liczbę: ')
    d_gracz = input('Podaj czwartą liczbę: ')
    e_gracz = input('Podaj piątą liczbę: ')
    f_gracz = input('Podaj szóstą liczbę: ')

    try:
        a = int(a_gracz)
        b = int(b_gracz)
        c = int(c_gracz)
        d = int(d_gracz)
        e = int(e_gracz)
        f = int(f_gracz)

        if a < 1 or a > 49:
            print("Zła wartość pierwszej liczby!")
        elif b < 1 or b > 49 or b == a:
            print("Zła wartość drugiej liczby!")
        elif c < 1 or c > 49 or c in {a, b}:
            print("Zła wartość trzeciej liczby!")
        elif d < 1 or d > 49 or d in {a, b, c}:
            print("Zła wartość czwartej liczby!")
        elif e < 1 or e > 49 or e in {a, b, c, d}:
            print("Zła wartość piątej liczby!")
        elif f < 1 or f > 49 or f in {a, b, c, d, e}:
            print("Zła wartość szóstej liczby!")
        else:
            gracz = [a, b, c, d, e, f]

            gracz.sort()
            print(f"Wytypowane przez Ciebie liczby to: {gracz}")
            komp_los = list(range(1, 50))
            shuffle(komp_los)
            komp = komp_los[:6]
            komp.sort()
            print(f"Wylosowane liczby to: {komp}")
            result = 0

            for i in gracz:
                for n in komp:
                    if i == n:
                        result += 1
            if 5 > result > 2:
                print(f"Gratulacje, trafiłeś {result} liczby!")
            elif result >= 5:
                print(f"Gratulacje, trafiłeś {result} liczb!")
            else:
                print(f"Spróbuj jeszcze raz, Twój wynik to: {result}.")


    except ValueError:
        print("Wpisz tylko liczby!")
    except Exception:
        print("Ups, coś poszło nie tak")

gra()
