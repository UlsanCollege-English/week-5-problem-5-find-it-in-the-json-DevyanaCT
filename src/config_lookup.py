def find_key(data, key):
    """
    Depth-first left-to-right search for the first occurrence of key.
    Return the value, or None if not found.
    Works for dicts, lists, and tuples.
    """

    if data is None:
        return None

    if isinstance(data, dict):
        if key in data:
            return data[key]
        for value in data.values():
            result = find_key(value, key)
            if result is not None:
                return result
        return None

    # Handle list or tuple
    if isinstance(data, (list, tuple)):
        for element in data:
            result = find_key(element, key)
            if result is not None:
                return result
        return None

    # Other types cannot contain the key
    return None
