#   Welcome to this code, I hope you'll enjoy it
# author: Steve
# creation date: 2021-02-07 12:29:57
# purpose: PasswordSecurityCheck from terminal
# status: in progress
# %% we will be using the website's pwnedpasswords.com API
#    it uses k-anonymity, so you only have to give it the first 5 letters of the hash
#    and then you get back the matching hashes, all of them, so they can't know your
#    specific search, which is pretty smart
#
#    run the python file in the IDE or the exe file in the dist folder
#
#    in case of execution in terminal - some code needs to be un(commented)
#    > python main.py <password_to_check>

# %% ################ Imports ####################
# main functionality for API requests and hashing
import requests
import hashlib
# for the optional terminal call with pw as arguments
import sys
# for the optional window termination countdown:
import time
# for coloring the output on the terminal:
from colorama import init
from termcolor import colored


# ################### Functions ####################
# this function is responsible for fetching the hashed password tails that match your pw-tail
def api_data_request(query_chars):
    pw_url = 'https://api.pwnedpasswords.com/range/' + query_chars

    api_response = requests.get(pw_url)
    if api_response.status_code != 200:
        raise RuntimeError(f'Error fetching: {api_response.status_code}, check API and try again.')

    # print(api_response.text)
    # in the response.text you get all the tails: #hacked, like this:
    # EDAFA574EEB5A77322D4C6150FAA4A41816:1
    # EE38120FCCCD99F6F5CF32812C15CA2B1FB:34
    # EE606898F30C5C473736BFDAC262955137F:3

    return api_response


# this one counts the number of times the pw has been leaked
def get_pw_leaks_count(hashes, hash_to_check):
    split_hashes = (line.split(':') for line in hashes.text.splitlines())
    for hsh, count in split_hashes:
        if hsh == hash_to_check:
            return count
    return 0


# the following function requires the following steps:
# first you encode the pw in utf-8: b'hello'
# then you create a sha1 HASH object out of it: <sha1 HASH object @ 0x0380CE10>
# hexdigest creates: 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
# contains only hex digits, can be sent securely over mail
# then convert to upper case: 'AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'

# this function prepares the password for the request and also calls the counting fct
def pwned_api_check(password):
    # prepare the password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # save first 5 chars and tail:
    first5chars, tail = sha1password[:5], sha1password[5:]
    # print('first5chars:', first5chars, 'tail:', tail)
    # print('sha1password:', sha1password)

    # pass the 5 chars to the request function:
    response = api_data_request(first5chars)

    # print('response:', response)
    # print('tail:', tail)
    # <Response [200]>
    return get_pw_leaks_count(response, tail)
    # you need to pass the tail because that's what you get from the API!


# required initialization for colorama:
init()


# #### IDE-execution version: (one or the other has to be commented out to work) #####
def main(password):

    count = pwned_api_check(password)

    if int(count) == 1:
        print(colored(f'The password "{password}" was found {count} time! It would be smart to change your password.',
              'red'))
    elif int(count) > 1:
        print(colored(f'The password "{password}" was found {count} times! You should change your PW immediately!!!',
              'red'))
    else:
        print(colored(f'"{password}" was NOT found. Carry on!', 'green'))
    return 'done!'


# asking for user input, aka the password to be checked
x = input('Your password to check: ')
main(x)


# displaying information about when the window of the exe is closing
# comment this out if you are using the file through an IDE
time.sleep(3)

for i in range(10, 0, -1):
    print(colored(f'Window will close in {i} seconds.', 'white', 'on_red'), end='\r', flush=True)
    time.sleep(1)

print('                                                           ')
print(colored('There is no spoon.', 'white', 'on_red'))
time.sleep(1)


# #### terminal-call version: (one or the other has to be commented out to work) ######
# def main(args):
#     for password in args:
#         count = pwned_api_check(password)
#
#         if int(count) == 1:
#             print(colored(f'The password "{password}" was found {count} time! It would be smart to change your password.',
#               'red'))
#         elif int(count) > 1:
#             print(colored(f'The password "{password}" was found {count} times! You should change your PW immediately!!!',
#               'red'))
#         else:
#             print(colored(f'"{password}" was NOT found. Carry on!', 'green'))
#     return 'done!'
#
#
# if __name__ == '__main__':
#     # call with all the passed passwords
#     # and exit so it prints 'done!'
#     sys.exit(main(sys.argv[1:]))


# %% useful links:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# https://passwordsgenerator.net/sha1-hash-generator/
# https://pypi.org/project/colorama/
# https://www.pyinstaller.org/
#   - either create a bundle via:           pyinstaller main.py
#   - or create a standalone executable:    pyinstaller --onefile main.py
# will be created in the dist folder
