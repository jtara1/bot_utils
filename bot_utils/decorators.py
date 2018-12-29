def ignore_exception(exception_class, ignore_it=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_class as err:
                if not ignore_it:
                    raise err

        return wrapper
    return decorator
