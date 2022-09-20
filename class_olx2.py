from bs4 import BeautifulSoup


class Olx:
    def __init__(self, html):
        self.doc = BeautifulSoup(html, "html.parser")
        self.info_flat = []

    def find_title(self, flat):
        return flat.find('strong').getText()


    def find_location(self, flat):
        flat = flat.findAll('small', class_='breadcrumb x-normal')
        for element in flat:
            location = element.find('span')
            if location:
                return location.getText().replace(',', ':')


    def find_price(self, flat):
        return flat.find('p', class_='price').strong.text


    def find_sell_rent(self, flat):
        return flat.find('p').getText().strip().replace('Mieszkania »', '')

    def find_link(self, flat):
        return flat.find('h3', class_="lheight22 margintop5").a['href']


    def find_price_by_arrangement(self, flat):
        flat = flat.find('span', class_='normal inlblk pdingtop5 lheight16 color-2')
        if flat:
            return flat.getText()


    def znajdz_mieszkania(self):
         return self.doc.find_all('div', class_="offer-wrapper")

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


