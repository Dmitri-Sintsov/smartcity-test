from functools import wraps


def required_keys(lst):
    def decorator(f):
        @wraps(f)
        def wrapped(data):
            data_keys_set = set(data.keys())
            if len(set(lst) - data_keys_set) > 0:
                return None
            result = f(data)
            return result
        return wrapped
    return decorator
