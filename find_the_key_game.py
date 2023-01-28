from random import randint
from math import sqrt
import secrets

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)
player_x = 0
player_y = 0
player_found_key = False
steps = 0
hot = ['Dajesz dajesz dobrze Ci idzie', 'Ciełooooo!', 'Nieźle, oby tak dalej', 'Elegancko', 'Tak trzym']
cold = ['Zimno!!!', 'Nie tędy droga', 'Gdzie leziesz?', 'Zawracaj pacanie!!']
wall = ['Walnąłeś w ścianę!!', 'Nieźle przydzwoniłeś', 'Ojojoj, główka boli?', 'Ręka noga mózg na ścianie...!']

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)


while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach określonych jako [W/A/S/D]: ')

    move = input('Dokąd idziesz? ')
    match move.lower():

        case 'w':
            player_y += 1
            if player_y > GAME_HEIGHT:
                print(secrets.choice(wall))
                player_y = GAME_HEIGaHT

        case 's':
            player_y -= 1
            if player_y < 0:
                print(secrets.choice(wall))
                player_y = 0

        case 'a':
            player_x -= 1
            if player_x < 0:
                print(secrets.choice(wall))
                player_x = 0

        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print(secrets.choice(wall))
                player_x = GAME_WIDTH

        case 'q':
            print('Koniec gry')
            quit()

        case '':
            print('Nie wiem do kąd idziesz')
            continue

    if player_x == key_x and player_y == key_y:
        print("UDAŁO SIĘ!!! Klucz jest twój!!")
        print(f'Wykonano {steps} ruchów.')
        quit()

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print(secrets.choice(hot))
    else:
        print(secrets.choice(cold))

    distance_before_move = distance_after_move

    print(player_x, player_y)