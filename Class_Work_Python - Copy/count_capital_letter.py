import re
def count_capital_letter(text):
    pattern = re.compile(r'[A-Z]')
    return (f' len(pattern.findall(text))')

print(count_capital_letter("Alice And Bob Are Good Friend"))

