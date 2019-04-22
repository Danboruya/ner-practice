import sys
import pyknp
import ner_func


def prompt():
    knp = pyknp.KNP(option="-tab -dpnd",
                    rcfile='/usr/local/etc/knprc',
                    jumanrcfile='/usr/local/etc/jumanrc')
    while True:
        print(">>> ", end="")
        line = input()
        print(ner_func.extract_ne(line, knp, detail_flag=False) + "\n")


def tester():
    knp = pyknp.KNP(option="-tab -dpnd",
                    rcfile='/usr/local/etc/knprc',
                    jumanrcfile='/usr/local/etc/jumanrc')
    line1 = "今年の人工知能学会の全国大会は2016年6月6日~9日まで北九州国際会議場で開催されます"
    line2 = "昨夜，太郎は夜9時に花子へ会いに行った"
    line3 = "佐藤は昨夜，国会議事堂まで個人情報保護法についての議論を見に行った"
    line4 = "藤本太郎喜左衛門将時能という名前の人がいるらしい"
    print(line1)
    print(ner_func.extract_ne(line1, knp, detail_flag=True) + "\n")
    print(line2)
    print(ner_func.extract_ne(line2, knp, detail_flag=True) + "\n")
    print(line3)
    print(ner_func.extract_ne(line3, knp, detail_flag=True) + "\n")
    print(line4)
    print(ner_func.extract_ne(line4, knp, detail_flag=True) + "\n")


def main(_args):
    if _args[0] != "prompt":
        tester()
    else:
        prompt()


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        args = args[1:]
    main(args)
