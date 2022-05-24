from tank import Tank
from random import choice
tanks = {'a':Tank('Alice'), 'b':Tank('Bob'), 'c':Tank('Carol'), 'd':Tank('Wild Cat'), 'e':Tank('Steel dragon')}
alive_tanks = len(tanks)
players = ['a', 'b', 'c', 'd', 'e']

while alive_tanks > 1:

    print (' ' * 30)

    for tank_name in sorted(tanks.keys()):
        print (f'{tank_name} - ' + str(tanks[tank_name]))

    first = choice(players)
    second = choice(players)

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]

    except KeyError + tank.name:
        print('No such tank! ' + tank.name)
        continue

    if not first_tank.alive or not second_tank.alive:
        print ('One of those tanks is dead!')
        continue

    print(' ' * 30)
    print ('*' * 30)

    first_tank.fire_at(second_tank)

    if not second_tank.alive:
        alive_tanks -= 1

    print ('*' * 30)

    for tank in tanks.values():
        if tank.alive:
            print (tank.name + ' Its the winner!')
            break

    