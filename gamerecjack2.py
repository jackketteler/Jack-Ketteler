"""
Game Recommendation Site
"""

print("Welcome to our Game Recommendation Site.")

categories = ('horror', 'shooter', 'adventure', 'PVP')


def prompt(ask):
    return input('{}? '.format(ask))


def loop():
        
    print('Which genre do you like?')
    print(categories)

    ans = input()

    if ans == 'horror':
        print('You should consider checking out the game Outlast')
        print('Would you like a summary?')
        wantSummary = input()
        if wantSummary == 'yes':
            print('summary')

    elif ans == 'shooter':
        print('You should consider checking out the game Wolfenstein')
        print('would you like a summary of the game?')
        wantSummary = input()
        if wantSummary == 'yes':
            print('This game sticks you into a world where the Nazis won WW2. Its a crazy world and you play as a Jewish man named Williiam J. Blaskowicz. He hates Nazis and he is on a mission to get rid of all Nazis in the world. He gains some allies on the way and kicks some serious ass. The games story is weird an dunexpected which always leaves you wanting to see what may happen next.')

    elif ans == 'adventure':
        print('You should consider checking out the game Uncharted 4')
        print('Would you like a summary of the game?')
        wantSummary = input()
        if wantSummary == 'ywa':
            print('summary')

    if prompt('again') == 'yes':
        loop()



loop()
