# import requests  # Con Request Wowace da error <403>
import pandas as pd
import os
import easygui
import zipfile
import getpass
from selenium import webdriver


# Ruta addons
user = getpass.getuser()
print('\nUbique la dirección de archivo WoW.exe... \n')
wow_directory = easygui.diropenbox(default=f'/home/{user}/Downloads')
addons_path = wow_directory + '/Interface/AddOns'

# Driver setup
path = '/home/contac/PycharmProjects/My-Wow-Addons-LK-/chromedriver_linux64/chromedriver'
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : f'{addons_path}'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(path, chrome_options=chrome_options)

if os.path.isdir(addons_path):
	df_addons = pd.read_csv('Addons.csv')
	filepath = addons_path + '/'
	for url in df_addons['Url']:
		try:
			driver.get(url)
			filename = [f for f in os.listdir(filepath) if f.find('.zip')>0][0]
			with zipfile.ZipFile(filepath + filename, "r") as zip_ref:
				zip_ref.extractall(filepath)
			os.remove(filepath + filename)
		except Exception:
			print('No se encontró archivo descargable. Saltando al siguiente...')
	os.remove(filepath + 'SlideBar')
