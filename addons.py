import requests
import pandas as pd
import os.path
import easygui
import time

print('\n')
print('Ubique la dirección de archivo WoW.exe \n')
time.sleep(3)

wow = easygui.fileopenbox()
addons_path = os.path.dirname(wow) + '/Interface/AddOns'
if os.path.isfile(wow) and os.path.isdir(addons_path):
    print('Comenzando descarga con Requests...\n')
    df_addons = pd.read_csv('Addons.csv')
    filepath = addons_path + '/'
    for url in df_addons['Url']:
        r = requests.get(url, allow_redirects=True)
        filename = filename = r.url.split('/')[-1]
        pwd_addon = filepath + filename
        with open(pwd_addon, 'wb') as f:
            f.write(r.content)
