from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import sys
import re


INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content, resp.encoding


def load_inspection_page():
    with open('inspection_page.html', 'r') as content:
        encoded_content = content.read()
        return encoded_content, 'utf-8'


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, "html5lib", from_encoding=encoding)
    return parsed


def extract_data_listings(parsed):
    id_finder = re.compile(r'PR[\d]+~')
    return parsed.find_all('div', id=id_finder)


if __name__ == "__main__":
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        html, encoding = load_inspection_page()
    else:
        html, encoding = get_inspection_page(**kwargs)

    doc = parse_source(html, encoding)
    doc.prettify(encoding=encoding)
    listings = extract_data_listings(doc)
    print len(listings)
    print listings[0].prettify()
