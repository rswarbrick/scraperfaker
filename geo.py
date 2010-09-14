import re

postcode_pattern = '([a-zA-Z]{1,2}[1-9][0-9]?)[ ]*([1-9][a-zA-Z]{2})'
postcode_re = re.compile (postcode_pattern)

def gb_postcode_to_latlng (postcode):
    return (0,0)

def os_easting_northing_to_latlng (easting, northing):
    return (0,0)

def extract_gb_postcode (string):
    hit = postcode_re.search (string)
    if (not hit):
        return None
    return (hit.group (1) + ' ' + hit.group(2)).upper ()

