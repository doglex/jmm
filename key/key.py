"""
返回私人token
"""


def get_token(filename="token.key"):
    with open(filename, "rt") as f:
        return f.readline().strip()


if __name__ == '__main__':
    ans = get_token()
    print(ans)
