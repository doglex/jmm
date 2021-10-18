import tushare as ts


def get_instance():
    from jmm.key.key import get_token
    instance = ts.pro_api(get_token())
    return instance


pro = get_instance()
