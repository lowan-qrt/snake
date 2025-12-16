import os

def lobby():
    print('\n\nSelect the option :\n')
    options = {
        1 : ['Play', True],
        2 : ['Rules', lambda: readFile('assets/snake_rules.txt')],
        3 : ['Historical', readScores],
        4 : ['Reset historical', resetScores],
        5 : ['Once upon a time...', lambda: readFile('assets/history.txt')],
        6 : ['Credits', lambda: readFile('assets/credits.txt')],
        7 : ['Quit', None]
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

# 3. Scores
def readScores():
    try:
        with open("assets/highscore.txt", "r", encoding="utf-8") as f:
            nb_lines = sum(1 for _ in f)
            if nb_lines == 0:
                print('\n\tThere is no score.')
            else:
                with open('assets/highscore.txt', 'r', encoding='utf-8') as f:
                    content = f.read()
                print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ There is no score.\n')

# 4. Reset scores
def resetScores():
    try:
        os.remove('assets/highscore.txt')
        print('Scores are reset.')
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 7. Quit
def quit():
    return False

def readFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

def main():
    while True:
        chosenAction = lobby()
        if chosenAction is None:
            quit()
            return None
        elif chosenAction == True: # launch the game
            return True
        else:
            try:
                chosenAction()
            except FileNotFoundError:
                print('\n\t/!\\ The ressource is not found.\n')