def unpack_methods(src_obj, destination_dict):
    method_names = list(filter(lambda func_name: '__' not in func_name, dir(src_obj)))
    for func in method_names:
        destination_dict[func] = getattr(src_obj, func)
