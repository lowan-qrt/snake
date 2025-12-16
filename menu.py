import os

def lobby():
    """
    Display the main menu, prompt the player for an option, and return the
    corresponding action.

    Returns:
        callable: A callable function to execute for the selected option.
        bool: True if the player chooses to start the game.
        None: None if the input is interrupted (Ctrl+C).
    """
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
            os.system('cls')
            print('\n\t/!\\ This option is disable.')
            return lobby
        else:
            os.system('cls')
            return options[playerSelect][1]
    except ValueError:
        os.system('cls')
        print('\n\t/!\\ You have to select a number.')
        return lobby
    except KeyboardInterrupt:
        return None

# 3. Scores
def readScores():
    """
    Read and display the saved high scores from the score file.

    If the file does not exist or is empty, an informative message is shown.
    """
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
    """
    Delete the high score file to reset all saved scores.

    Displays an error message if the file does not exist.
    """
    try:
        os.remove('assets/highscore.txt')
        print('Scores are reset.')
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

# 7. Quit
def quit():
    """
    Signal the application to stop execution.

    Returns:
        bool: False to indicate program termination.
    """
    return False

def readFile(file_path):
    """
    Read and display the content of a text file.

    Args:
        file_path (str): Path to the file to read.

    Displays an error message if the file does not exist.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print('\n' + content)
    except FileNotFoundError:
        print('\n\t/!\\ The resource is not found.\n')

def main():
    """
    Main program loop handling menu navigation and action execution.

    Continuously displays the lobby until the player quits or starts the game.

    Returns:
        bool: True if the game should start.
        None: If the program exits.
    """
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