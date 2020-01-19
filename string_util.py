import re


def fix_title(title):
    title = remove_punct(title)
    title = remove_multiple_spaces(title)
    return title


def remove_punct(string):
    string = re.sub(r"[']+", '', string)
    return re.sub(r"[-:_!,/\[\].()#?;&\n]+", ' ', string).strip()


def remove_multiple_spaces(string):
    return re.sub(r'\s+', ' ', string).strip()
