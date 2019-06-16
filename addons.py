import requests
import pandas as pd
import os
import easygui
import time
import zipfile

print('\n')
print('Ubique la dirección de archivo WoW.exe \n')
time.sleep(1)

wow = easygui.fileopenbox()
addons_path = os.path.dirname(wow) + '/Interface/AddOns'
if os.path.isfile(wow) and os.path.isdir(addons_path):
    print('Comenzando descarga con Requests...\n')
    df_addons = pd.read_csv('Addons.csv')
    df_addons = df_addons[:-1]
    filepath = addons_path + '/'
    for url in df_addons['Url']:
        r = requests.get(url, allow_redirects=True)
        filename = filename = r.url.split('/')[-1]
        print(f'Descargando {filename}...\n')
        pwd_addon = filepath + filename
        with open(pwd_addon, 'wb') as f:
            f.write(r.content)
        r.close()
        with zipfile.ZipFile(pwd_addon, "r") as zip_ref:
            zip_ref.extractall(filepath)
        os.remove(pwd_addon)
    os.remove(filepath + 'SlideBar')
