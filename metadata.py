metadata = dict()

def save (key, value):
    metadata[key] = value
    fmt = "METADATA:\n  Key:   {0} ({1})\n  Value: {2} ({3})"
    print fmt.format (str(key), str(type(key)),
                      str(value), str(type(value)))

def get (key, default=None):
    if key in metadata:
        return metadata[key]
    return default
