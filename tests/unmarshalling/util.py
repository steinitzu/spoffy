def dict_obj_diff(dict_: dict, obj):
    for key, value in dict_.items():
        if isinstance(value, list):
            o_value = getattr(obj, key)
            for d_item, o_item in zip(value, o_value):
                if isinstance(d_item, dict):
                    dict_obj_diff(d_item, o_item)
                    continue
                assert d_item == o_item
            continue
        if isinstance(value, dict):
            obj_value = getattr(obj, key)
            if isinstance(obj_value, dict):
                assert value == obj_value
            else:
                dict_obj_diff(value, getattr(obj, key))
            continue
        assert getattr(obj, key) == value
