import os
from slugify import slugify
from dotenv import load_dotenv
from woocommerce import API

load_dotenv()

wcapi = API(
    url=os.getenv("WC_URL"),
    consumer_key=os.getenv("WC_CONSUMER_KEY"),
    consumer_secret=os.getenv("WC_CONSUMER_SECRET"),
    version='wc/v3'
)

class Termek:
    def __init__(self, sorszam, megnevezes, szelet, mertekegyseg, egysegar, kategoria,
                valtozat, idenyjellegu, burkolhato, ostya, glutenmentes, laktozmentes,
                paleo, termekleiras, megjegyzes, atveheto, atveheteo_alt):

        self.sorszam = int(sorszam)
        self.megnevezes = megnevezes
        self.szelet = int(szelet) if szelet != '' else None
        self.mertekegyseg = mertekegyseg
        self.egysegar = int(egysegar)
        self.kategoria = kategoria
        self.valtozat = valtozat.split(',') if valtozat != '' else None
        self.idenyjellegu = True if idenyjellegu == 'Idényjellegű' else False
        self.burkolhato = True if burkolhato == 'Igen' else False
        self.ostya = True if ostya == 'Igen' else False
        self.glutenmentes = True if glutenmentes == 'Igen' else False
        self.laktozmentes = True if laktozmentes == 'Igen' else False
        self.paleo = True if paleo == 'Paleo' else False
        self.termekleiras = termekleiras.capitalize() if termekleiras != '' else None
        self.megjegyzes = megjegyzes if megjegyzes != '' else None
        self.atveheto = int(atveheto) if atveheto != '' else None
        self.atveheteo_alt = atveheteo_alt if atveheteo_alt != '' else None
        self.rovid_leiras = self.termekleiras[0:37] if self.termekleiras else None

        if  self.rovid_leiras != None and len(self.rovid_leiras) < len(self.termekleiras):
            self.rovid_leiras += '...'

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(self.sorszam, self.megnevezes, self.szelet, self.mertekegyseg, self.egysegar, self.kategoria,
            self.valtozat, self.idenyjellegu, self.burkolhato, self.ostya, self.glutenmentes, self.laktozmentes, self.paleo, self.termekleiras, self.rovid_leiras, 
            self.megjegyzes, self.atveheto, self.atveheteo_alt)

lines = open('termekek.tsv', mode='r', encoding='utf-8').readlines()[1:]

termekek = []

for line in lines:
    item = line.split('\t')
    termek = Termek(item[0], item[1], item[2], item[3], item[4], item[5], item[6], 
                    item[7], item[8], item[9], item[10], item[11], item[12], 
                    item[13], item[14], item[15], item[16])
    termekek.append(termek)

print(termekek[26])

"""for termek in termekek:
    product_data = {
        "name": termekek.megnevezes,
        "slug": slugify(termekek.megnevezes),
        "type": "variable", # TODO: variable or simple
        "regular_price": termekek.egysegar,
        "description": termekek.termekleiras,
        "short_description": termekek.rovid_leiras,
        "sku": termekek.sorszam,
        "categories": [
            {
                "id": 34 # TODO: category id
            }
        ],
        "images": [
            {
                "src": "" # TODO image url
            }
        ],
        "attributes": [
            {
                # TODO attribute id
            }
        ]
    }

    variation_data = {
        "regular_price": termekek.egysegar, # TODO: price
        "sku": termekek.sorszam, # TODO: sku
        "attributes": [
            {
                # TODO attribute id
            }
        ]
    }

    product = wcapi.post('products', data).json()
    wcapi.post('products/{}/variations'.format(product['id']), variation_data).json()"""