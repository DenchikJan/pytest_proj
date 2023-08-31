def get_val(collection: dict, key, default='git'):
    if len(collection) == 0 or key not in collection.keys():
        return default
    else:
        return collection[key]