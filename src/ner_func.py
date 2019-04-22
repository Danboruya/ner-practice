import re


def extract_ne(src_str, knp, fstring_flag=False, detail_flag=False):
    _knp = knp
    tagged_str = src_str
    result = _knp.parse(src_str)

    if fstring_flag:
        for t in result.tag_list():
            print(t.fstring)

    if detail_flag:
        for x in result.tag_list():
            print(x.fstring)

    for tag in result.tag_list():
        if "NE:" in tag.fstring:
            if "NE:ARTIFACT" in tag.fstring:
                tagged_ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(0).split("><")[0] + ">"
                ne_phrase = tagged_ne_phrase.split(":")[2][:-1]
            elif "NE:ORGANIZATION" in tag.fstring:
                tagged_ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(0).split("><")[0] + ">"
                ne_phrase = tagged_ne_phrase.split(":")[2][:-1]
            else:
                tagged_ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(0)
                ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(2)

            tagged_str = tagged_str.replace(ne_phrase, tagged_ne_phrase)

    return tagged_str
