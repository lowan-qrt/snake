# Made by Nathan M. and Lowan Q.
# On December 2025
# Helping functions

def hideCursor(booleanValue):
    """
    Set up the visibility of the cursor
    Args:
        booleanValue : boolean
    """
    import ctypes   
    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]
    ci = _CursorInfo()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
    ci.visible = booleanValue
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

def occOfItem(array,value):
    """
    Return the number of occurences of an item 
    Attributes:
        array (array): 
        value (void)
    """
    cpt = 0
    for element in array:
        if element.name == value:
            cpt += 1
    return cpt

def validInput(type:str ,floor:int,ceil:int,message:str,default):   
    """
    Make an input errorless

    Attributes:
        type (str) : the type of the wanted input
        floor (int): the minimal value (the minimal length in str case)
        ceil (int): the maximal value (the maximal length in str case)
        message (str) : The text to print in the input
        default (str/int) : the value by default
    """
    
    while True:
        match(type):
            case 'int':
                value = input(str(message+'(default value: '+ str(default))+'): ') or default
                try:
                    value = int(value)
                except ValueError:
                    print('Valid int, please')
                    continue
                if floor <= value <= ceil:
                    return value
                else:
                    print(f'Valid range, please,{floor}-{ceil}')
            case 'str':
                value = input(str(message+'(default value: '+ str(default))+'): ') or default
                try:
                    value = str(value)
                except ValueError:
                    print('Valid string, please')
                    continue
                if floor <= len(value) <=ceil:
                    return value
                else :
                    print(f'Valid length, please, {floor}-{ceil}')