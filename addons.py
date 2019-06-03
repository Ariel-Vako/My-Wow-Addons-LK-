from requests_donwload import download, Hastracker, ProgressTracker
from progressbar import DataTransferBar
import pandas as pd
import os.path

print('Ingrese dirección de archivo WoW.exe: ')
wow = input()
addons_path = os.path.dirname(wow) + 'Interface/Addons/'
if os.path.isfile(wow) and os.path.isdir(addons_path):
    print('Comenzando descarga con urllib...')
    df_addons = pd.read_csv('Addons.csv')

    for addon in df_addons:
        url =''