
def i(string):
    if string[::-1] == string:
        return True
    elif string[::-1] != string:
        return False
    
string = input('введите слово: ')

i(string)
