import re

def SimpleSymbols(val):
    match = re.search(r"[a-z](?!\+)|(?<!\+)[a-z]", val)

    if match:
        return False

    return True

