from bs4 import BeautifulSoup



class Otodom:
    def __init__(self, html):
        self.doc = BeautifulSoup(html, "html.parser")
        self.info_flat = []

    def find_title(self, flat):
        return flat.find('h3', class_='css-1oq8pdj es62z2j24').getText()

    def find_location(self, flat):
        flat = flat.findAll('p', class_='css-80g06k es62z2j23')
        for element in flat:
            return element.find('span').getText().replace(',', '')

    def find_price(self, flat):
        return flat.find('p', class_='css-5kmdsl es62z2j19').getText().replace('\xa0', '.')

    def find_sell_rent(self, flat):
        return flat.find('p', class_='css-80g06k es62z2j23').text.split()[2].replace(':', '')

    def find_link(self, flat):
        return flat.find('a')["href"]
        # return flat.find('a').aside.picture.source['srcset']

    def find_price_by_arrangement(self, flat):
        return flat.find('span', class_='normal inlblk pdingtop5 lheight16 color-2')


    def znajdz_mieszkania(self):
        return self.doc.find_all('li', class_='css-7mmxt5 es62z2j30')

    def collect_info_flat(self):
        mieszkania = self.znajdz_mieszkania()


        for mieszkanie in mieszkania:
            title = self.find_title(mieszkanie)
            location = self.find_location(mieszkanie)
            price = self.find_price(mieszkanie)
            sell_rent = self.find_sell_rent(mieszkanie)
            link = self.find_link(mieszkanie)
            price_by_arrangement = self.find_price_by_arrangement(mieszkanie)
            info = [title, location, price, sell_rent, link, price_by_arrangement]
            self.info_flat.append(info)

    def flats_info(self):
        return self.info_flat


class Wynajem(Otodom):
    def __init__(self, html):
        self.doc = BeautifulSoup(html, "html.parser")
        self.info_flat = []










