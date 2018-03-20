"""
Game Recommendation Site
"""

print("Welcome to our Game Recommendation Site.")

categories = ('horror', 'shooter', 'adventure', 'PVP')

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
        print('summary')
