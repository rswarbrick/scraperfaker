import urllib
import urllib2

def scrape (url, params=None):
    params_enc=None
    if (params):
        if (type (params) != type (dict())):
            raise Exception ("Invalid params. Expected dict")
        params_enc = urllib.urlencode (params)
    handle = urllib2.urlopen (url, params_enc)
    data = handle.read ()
    handle.close ()
    return data

