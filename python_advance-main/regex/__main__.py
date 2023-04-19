import re


def test_search():
    pattern = r"\d{2}"
    source = "I'm 80 years old."

    result = re.search(pattern, source)
    print(result)


def test_match():
    pattern = r"\d{2}"
    source = "80 years old."

    result = re.match(pattern, source)
    print(result)


def test_fullmatch():
    pattern = r"\d{2}"
    source = "809"

    result = re.fullmatch(pattern, source)
    print(result)


def test_findall():
    pattern = r"\d{2}"
    source = "8 09 aaa  89 laskdjf"

    result = re.findall(pattern, source)
    print(result)


def test_finditer():
    pattern = r"\d{2}"
    source = "8 09 aaa  89 laskdjf"

    it = re.finditer(pattern, source)
    for rs in it:
        print(rs)


def test_compile():
    pattern_str = r"\d{2}"
    pattern = re.compile(pattern_str)
    print(pattern.fullmatch("99"))


test_compile()
