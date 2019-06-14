__source__ = 'https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un'

import requests
import re


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    # header.values() is a <class 'collections.abc.ValuesView'>
    # header.items() is a  <class 'collections.abc.ItemsView'>
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]
