#!/usr/bin/env python
# IGComment v1.0
# Author: https://github.com/thelinuxchoice/igcomment

import requests
username=input('Username: ')
password=input('Password: ')
mediaid=input('MediaID: ')
message=input('Message: ')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
csrftoken = requests.get('https://www.instagram.com').cookies['csrftoken']
login_req = sess.post('https://www.instagram.com/accounts/login/ajax/', headers={
	'origin': 'https://www.instagram.com',
	'pragma': 'no-cache',
	'referer': 'https://www.instagram.com/accounts/login/',
	'user-agent': user_agent,
	'x-csrftoken': csrftoken,
	'x-requested-with': 'XMLHttpRequest'
}, data={
	'username': username,
	'password': password,
	'queryParams': '{}'
})

print(login_req.text)

if '"authenticated": true' in login_req.text:
	print('Login successfuly!')


payload = {
		'comment_text' : message,
		'replied_to_comment_id=' : ''
		}

post_req = sess.post('https://www.instagram.com/web/comments/{}/add/'.format(mediaid), headers={
	    'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'www.instagram.com',
            'Referer': 'https://www.instagram.com/',
	    'User-Agent': user_agent,
	    'X-CSRFToken': login_req.cookies['csrftoken'],
	    'csrftoken': login_req.cookies['csrftoken'],
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'close' }, cookies={
	    'mid': login_req.cookies['mid'],
	    'mcd': login_req.cookies['mcd'],
	    'csrftoken': login_req.cookies['csrftoken'],
	    'shbid': login_req.cookies['shbid'],
	    'ds_user_id': login_req.cookies['ds_user_id'],
	    'sessionid': login_req.cookies['sessionid'],
	    'rur': login_req.cookies['rur'],
	    'shbts': login_req.cookies['shbts'] 	

}, data=payload)

print(post_req.text)
