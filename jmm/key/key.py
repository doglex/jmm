"""
返回私人token
"""
from os import path


def get_token(filename=path.join(path.dirname(path.realpath(__file__)), "token.key")):
    with open(filename, "rt") as f:
        return f.readline().strip()


if __name__ == '__main__':
    ans = get_token()
    print(ans)
