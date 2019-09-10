import requests

def getFFdata():

    payload = {'user_account[email]': 'houangm@gmail.com','user_account[password]': 'Germany5'}

    with requests.Session() as s:
        p = s.post('https://filmfreeway.com/login',data=payload)
        r = s.get('https://filmfreeway.com/submissions/my_submissions?project=&q=&per_page=500') 

