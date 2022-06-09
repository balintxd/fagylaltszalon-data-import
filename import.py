from slugify import slugify

class Termek:
    def __init__(self, sorszam, megnevezes, szelet, mertekegyseg, egysegar, katekoria,
                valtozat, idenyjellegu, burkolhato, ostya, glutenmentes, laktozmentes,
                paleo, termekleiras, megjegyzes, atveheto, atveheteo_alt):
        self.sorszam = sorszam
        self.megnevezes = megnevezes
        self.szelet = szelet
        self.mertekegyseg = mertekegyseg
        self.egysegar = egysegar
        self.katekoria = katekoria
        self.valtozat = valtozat
        self.idenyjellegu = idenyjellegu
        self.burkolhato = burkolhato
        self.ostya = ostya
        self.glutenmentes = glutenmentes
        self.laktozmentes = laktozmentes
        self.paleo = paleo
        self.termekleiras = termekleiras
        self.megjegyzes = megjegyzes
        self.atveheto = atveheto
        self.atveheteo_alt = atveheteo_alt

        self.rovid_leiras = self.termekleiras[0:40]
        if len(self.rovid_leiras < self.termekleiras):
            self.rovid_leiras += '...'

lines = open('termekek.tsv', mode='r', encoding='utf-8').readlines()[1:]

termekek = []

for line in lines:
    item = line.split('\t').strip()
    termek = Termek(item[0], item[1], item[2], item[3], item[4], item[5], item[6], 
                    item[7], item[8], item[9], item[10], item[11], item[12], 
                    item[13], item[14], item[15])
    termekek.append(termek)

for termek in termekek:
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
wcapi.post('products/{}/variations'.format(product['id']), variation_data).json()