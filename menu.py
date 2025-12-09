def lobby():
    print('\n\nSelect the option :\n')
    options = {
        1 : ['Play', True],
        2 : ['Rules', readRules],
        3 : ['Historical', readScores],
        4 : ['Once upon a time...', readHistory],
        5 : ['Credits', readCredits],
        6 : ['Quit', None]
    }

    for key, option in options.items():
        print(f'{key}. {option[0]}')

    try:
        playerSelect = int(input('\n\t> '))
        if playerSelect not in options:
            print('\n\t/!\\ This option is disable.')
            return lobby
        else:
            return options[playerSelect][1]
    except ValueError:
        print('\n\t/!\\ You have to select a number.')
        return lobby
    except KeyboardInterrupt:
        return None

# 1. Play
def readScores():
    try:
        with open('assets/highscore.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 2. Rules
def readRules():
    try:
        with open('assets/snake_rules.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 3. 

# 4. Once upon a time...
def readHistory():
    try:
        with open('assets/history.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 5. Credits
def readCredits():
    try:
        with open('assets/credits.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 6. Quit
def quit():
    print('\n\tEND OF THE GAME\n')

while True:
    chosenAction = lobby()
    if chosenAction is None:
        quit()
        break
    elif chosenAction == True: # launch the game
        break
    else:
        try:
            chosenAction()
        except FileNotFoundError:
            print('\n\t/!\\ The ressource is not found.\n')
