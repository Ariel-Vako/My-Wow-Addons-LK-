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
    for url in df_addons['Url']:
        # Get the header first
        h = requests.head(url, allow_redirects=True)
        header = h.headers
        # header.values() is a <class 'collections.abc.ValuesView'>
        # header.items() is a  <class 'collections.abc.ItemsView'>
        filepath = addons_path + '/'
        filename = df_addons['Nombre'] + df_addons['Versión'] + header.get('Content-Encoding')
        r = requests.get(url, allow_redirects=True)
        with open(filepath + filename, 'wb') as f:
            f.write(r.content)
