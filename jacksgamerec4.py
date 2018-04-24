"""
Game Recommendation Site
"""

print("Welcome to our Game Recommendation Site.")

categories = ('horror', 'shooter', 'adventure', 'battle royale')


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
            print('Outlast is a game set in an insane asylum that is haunted and full of these weird creatures and crazy people roaming the halls. The whole atmosphere adds to the game making it feel realistic and leaves you right on the edge of your seat. With a solid 5 hour campaign for the price of $10 it is worth checking out, escpecially if you arent too sure its your type of genre.')

    elif ans == 'shooter':
        print('You should consider checking out the game Wolfenstein')
        print('would you like a summary of the game?')
        wantSummary = input()
        if wantSummary == 'yes':
            print('This game sticks you into a world where the Nazis won WW2. Its a crazy world and you play as a Jewish man named Williiam J. Blaskowicz. He hates Nazis and he is on a mission to get rid of all Nazis in the world. He gains some allies on the way and kicks some serious ass. The games story is weird an dunexpected which always leaves you wanting to see what may happen next.')

    elif ans == 'adventure':
        print('You should consider checking out the game God of War')
        print('Would you like a summary of the game?')
        wantSummary = input()
        if wantSummary == 'yes':
            print('While the God of War series isnt EXACTLY adventure the latest in the series takes a more open world root where you get to explore and loot chests in Midgard and other Norse mythology realms. Its really cool and a fun twist to the series that keeps you wanting more.')

    elif ans == 'battle royale':
        print('You should consider checking out the game Fortnite')
        print('Would you like a summary of the game?')
        wantSummary = input()
        if wantSummary == 'yes':
            print('Fortnite is a game where you can play solo or with friends in a giant 100 person free for all. This game is exceptionally fun and for a free game, you should definitly check it out. With constant updates being added to the game almost everyday, there is not much to get bored of.')
            

        

    if prompt('again') == 'yes':
        loop()

        


loop()
