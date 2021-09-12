from datetime import date
from requests import het, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rates(code):
    content = response.split ("<Valute ID=")
    d,m,i = map(int, content[0].split('"')[-4].split("."))

    for i in content:
        if code.upper () in i:
            print (date(year=y, month=m, day=d), end=",")
            return float (i.replace ("/","").split ("<Value>")[-2].replace (",","."))
        if __name__=="__main__":
            print (currency_rates("USD"))
        print (currence_rates("EUR"))
