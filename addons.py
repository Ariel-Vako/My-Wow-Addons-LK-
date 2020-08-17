import requests
import pandas as pd
import os
import easygui
import zipfile
import getpass

user = getpass.getuser()
print('\nUbique la dirección de archivo WoW.exe... \n')
wow_directory = easygui.diropenbox(default=f'/home/{user}/Downloads')
addons_path = wow_directory + '/Interface/AddOns'
if os.path.isdir(addons_path):
	df_addons = pd.read_csv('Addons.csv')
	filepath = addons_path + '/'
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
				   'AppleWebKit/537.11 (KHTML, like Gecko) '
				   'Chrome/23.0.1271.64 Safari/537.11',
	 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	 'Accept-Encoding': 'none',
	 'Accept-Language': 'en-US,en;q=0.8',
	 'Connection': 'keep-alive'}
	for url in df_addons['Url']:
		try:
			r = str(requests.get(url, allow_redirects=True, headers=headers)) # https://github.com/kuhnertdm/wow-addon-updater/blob/master/SiteHandler.py
			filename= r.find('file__name full')
			filename = r.url.split('/')[-1]
			print(f'Descargando {filename}...\n')
			pwd_addon = filepath + filename + '.zip'
			with open(pwd_addon, 'wt') as f:
				f.write(r.content)
			r.close()
			with zipfile.ZipFile(pwd_addon, "r") as zip_ref:
				zip_ref.extractall(filepath)
			os.remove(pwd_addon)
		except Exception:
			print('No se encontró archivo descargable. Saltando al siguiente...')
	os.remove(filepath + 'SlideBar')
