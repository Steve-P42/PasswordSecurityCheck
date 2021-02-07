#   Welcome to this code, I hope you'll enjoy it
# author: Steve
# creation date: 2021-02-07 12:29:57
# purpose: PasswordSecurityCheck
# status: in progress
# %% we will be using the website's pwnedpasswords.com API
#    it uses k-anonymity, so you only have to give it the first 5 letters of the hash
#    and then you get back the matching hashes, all of them, so they can't know your
#    specific search, which is pretty smart
# %% Imports
import requests
import hashlib
import sys



# %%

def api_data_request(query_chars):
    pw_url = 'https://api.pwnedpasswords.com/range/' + query_chars

    api_response = requests.get(pw_url)
    if api_response.status_code != 200:
        raise RuntimeError(f'Error fetching: {api_response.status_code}, check API and try again.')
    return api_response


print(api_data_request('00000'))


# %%

# %% useful links:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# https://passwordsgenerator.net/sha1-hash-generator/