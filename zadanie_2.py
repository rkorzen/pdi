

def zlicz_znaki(text):
    return 1

assert zlicz_znaki("") == 0
assert zlicz_znaki("ala ma kota") == 11
assert zlicz_znaki("ala <ma> kota") == 13
assert zlicz_znaki("<a>") == 2
assert zlicz_znaki("<<a>>") == 3
assert zlicz_znaki("a<a<a>>") == 6
assert zlicz_znaki("a<a<b>a>a") == 9

