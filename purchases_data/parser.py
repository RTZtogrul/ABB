from requests_html import HTMLSession
from PurchaseDoc import PurchaseDoc
import datetime
import re


def render_js(fiscal_id):
    url = 'https://monitoring.e-kassa.gov.az/#/index?doc=' + fiscal_id
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    text = r.html.text[22134:len(r.html.text) - 3780]
    try:
        assert text != ''
        return text
    except AssertionError:
        return render_js(fiscal_id)


def parse(user_FIN, fiscalID):
    store_name = (re.findall(r'(?:TS adı:)(.*?)(?:\n)', render_js(fiscalID), re.MULTILINE)[0]).strip()
    store_address = (re.findall(r'(?:TS ünvanı:)(.*?)(?:\n)', render_js(fiscalID), re.MULTILINE)[0]).strip()
    date = datetime.datetime.strptime(re.findall(r'(?:Tarix:)(?:\n)(.*?)(?:\n)', render_js(fiscalID),
                                                          re.MULTILINE)[0], '%d.%m.%Y').date()
    time = datetime.datetime.strptime(re.findall(r'(?:Saat:)(?:\n)(.*?)(?:\n)', render_js(fiscalID),
                                                          re.MULTILINE)[0], '%H:%M:%S').time()
    products = re.findall(r'(.*?)(?:\*ƏDV: 18%\n)\((?:.*?)\)(?:\n)(\d+\.\d*)\n(\d+\.\d*)', render_js(fiscalID),
                                   re.MULTILINE)
    total_price = float(re.findall(r'(?:Cəmi\n)(.*?)(?:\n)', render_js(fiscalID), re.MULTILINE)[1])

    total_payed = float(re.findall(r'(?:Nağdsız:\n)(.*?)(?:\n)', render_js(fiscalID), re.MULTILINE)[0]) + \
                           float(re.findall(r'(?:Nağd:\n)(.*?)(?:\n)', render_js(fiscalID), re.MULTILINE)[0])

    discount = total_price - total_payed

    return PurchaseDoc(user_FIN, store_name, store_address, date, time, products, total_price, discount, total_payed)


def write_to_db():
    pass
