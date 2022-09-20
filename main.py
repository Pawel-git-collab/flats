import class_olx2
import class_otodom
import save_to_CSV
import requests

def main():
    olx_html = requests.get("https://www.olx.pl/nieruchomosci/mieszkania/wroclaw/")
    oto_dom_html = requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw")
    oto_dom_html_wynajem = requests.get("https://www.otodom.pl/wynajem/mieszkanie/wroclaw")
    parsers = [class_olx2.Olx(olx_html.content), class_otodom.Otodom(oto_dom_html.content), class_otodom.Wynajem(oto_dom_html_wynajem.content)]
    for parser in parsers:
        parser.collect_info_flat()
        parser.flats_info()
        save_to_CSV.save_to_CSV(parser.flats_info())


if __name__ == '__main__':
    main()

