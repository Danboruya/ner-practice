import re
import pyknp


def extract_ne(src_str, knp, fstring_flag=False, detail_flag=False):
    _knp = knp
    tagged_str = src_str
    result = _knp.parse(src_str)
    ne_phrase_list = []
    ne_dict = {}

    if fstring_flag:
        for t in result.tag_list():
            print(t.fstring)

    if detail_flag:
        for x in result.tag_list():
            print(x.fstring)

    for tag in result.tag_list():
        if "NE:" in tag.fstring:
            if "NE:ARTIFACT" in tag.fstring or "NE:ORGANIZATION" in tag.fstring:
                tagged_ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(0).split("><")[0] + ">"
                ne_phrase = tagged_ne_phrase.split(":")[2][:-1]
            else:
                tagged_ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(0)
                ne_phrase = re.search("<NE:(.*):(.*)>", tag.fstring).group(2)

            tagged_str = tagged_str.replace(ne_phrase, tagged_ne_phrase)
            ne_phrase_list.append(ne_phrase)
            ne_dict[ne_phrase] = tagged_ne_phrase

    return [tagged_str, src_str, ne_phrase_list, ne_dict]


def swap_ne_tag_with_only_tag(src_str, target_tag, tag):
    tagged_ne_phrase = re.search("<NE:{}:(.*)>".format(target_tag), src_str).group(0)
    ne_phrase = tagged_ne_phrase.split(":")[2][:-1]
    return src_str.replace(tagged_ne_phrase, "<NE:{}:{}>".format(str(tag), ne_phrase))


def swap_ne_tag_with_ne_and_tag(src_str, target_ne, _tag, ne_phrase_list):
    tagged_str = src_str
    if target_ne not in ne_phrase_list:
        tagged_str = tagged_str.replace(target_ne, "<NE:{}:{}>".format(_tag, target_ne))
    return tagged_str


def tester_1():
    # Simple
    knp = pyknp.KNP(option="-tab -dpnd",
                    rcfile='/usr/local/etc/knprc',
                    jumanrcfile='/usr/local/etc/jumanrc')
    test = "昨日ノーベル物理学賞について学んだ"
    tagged_test = extract_ne(test, knp, detail_flag=False)
    print(swap_ne_tag_with_only_tag(tagged_test[0], "ARTIFACT", "PRIZE"))


def tester_2():
    # Swap with ne
    knp = pyknp.KNP(option="-tab -dpnd",
                    rcfile='/usr/local/etc/knprc',
                    jumanrcfile='/usr/local/etc/jumanrc')
    test = "昨日ノーベル物理学賞について学んだ"
    test1 = "昨日英語の教科書を買った"
    tagged_test = extract_ne(test, knp, detail_flag=False)
    tagged_test1 = extract_ne(test1, knp, detail_flag=False)
    print(swap_ne_tag_with_ne_and_tag(tagged_test[0], "ノーベル物理学賞", "PRIZE", tagged_test[2]))
    print(swap_ne_tag_with_ne_and_tag(tagged_test1[0], "教科書", "EDUCATION", tagged_test1[2]))
    print(tagged_test[3])
