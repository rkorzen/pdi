

def zlicz_znaki(text, *, incr="<", decr=">"):
    wynik = 0
    factor = 1
    for znak in text:
        if znak == incr:
            factor += 1
            continue
        elif znak == decr:
            factor -= 1
            continue
        wynik += factor
    return wynik

assert zlicz_znaki("") == 0
assert zlicz_znaki("ala ma kota") == 11
assert zlicz_znaki("ala <ma> kota") == 13
assert zlicz_znaki("<a>") == 2
assert zlicz_znaki("<<a>>") == 3
assert zlicz_znaki("a<a<a>>") == 6
assert zlicz_znaki("a<a<b>a>a") == 9

# assert zlicz_znaki("a[a[b]a]a", "[", "]") == 9
assert zlicz_znaki("a[a[b]a]a", incr="[", decr="]") == 9
