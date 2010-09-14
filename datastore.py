def max_key_len (unique_keys, data, others):
    maxlen = max (map (len, data.keys ()))
    maxulen = max (map (len, unique_keys)) + 1
    maxolen = max (map (len, others))
    return max (maxlen, maxulen, maxolen)

def padded_print (key, width, value):
    if (type (width) != type (0)):
        raise Exception ("Non-integer width")
    fmt = '  {0:' + str(width+2) + '}'
    print fmt.format (key+':') + str(value)

def save (unique_keys, data, date=None, latlng=None):
    print "RECORD:"
    keylen = max_key_len (unique_keys, data,
                          ['Date', 'Unique Keys', 'LatLng'])

    padded_print ('Unique Keys', keylen, unique_keys)
    padded_print ('Date', keylen, date)
    padded_print ('LatLng', keylen, latlng)

    for k,v in data.items ():
        padded_print (k, keylen, v)

data = {}
data['name'] = 'Ruffles'
data['dog_id'] = '9812301'
data['breed'] = 'Alsation'
save(['dog_id'], data, date="2009-03-02",
     latlng=(-2.983333, 53.4))
                
