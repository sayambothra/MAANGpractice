import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    print(res)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},check the api')
    return res

def pwnded_api_check(password):
    #check password if it exists in API reponse
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(first5_char)
    # print(first5_char,tail)
    # print(response)
    return get_password_leaks_count(response,tail)

# def read_res(response):
    #print(response.text) #returns how many times the first5_char of our password are being used
def get_password_leaks_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h ==hash_to_check:
            return count
    return 0
def main(args):
    for password in args:
        count=pwnded_api_check(password)
        if count:
            print(f'{password} was found {count} times .... you should change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'


#main(sys.argv[1:])
if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))