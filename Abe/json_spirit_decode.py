import re
# import io

def replacer(match):
    s = match.group()
    return chr(int(s[2:], 16))

def decode(data):
    try:
        regexp = re.compile(r'\\u(\w{4})')
        return regexp.sub(replacer, data)
    except ValueError:
        return '<Decode error>'

# with io.open('msg-json-bad.txt', 'rb') as f:
#     data = f.read()
#     print decode(data)
#
# with io.open('msg-json.txt', 'rb') as f:
#     data = f.read()
#     print decode(data)