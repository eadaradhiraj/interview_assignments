#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, urllib, sys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException


class Mango(object):
    # creating a class for mango.com
    def __init__(self,country='DE'):
        # lambda function to create soup of html code
        self._Soup = lambda htm: BeautifulSoup(htm, 'html.parser')
        #set country
        self.country = country
        # static string variable with URL
        self._URL = 'http://shop.mango.com/'+self.country
        # static variable with lcoation of chromedriver
        self._chromedriver = "./chromedriver"
        # get products info when object is created
        self._products = self._getproducts()

    def _gethtmlwjs(self, url):
        # get html source code of the webpage using chromedriver
        try:
            os.environ["webdriver.chrome.driver"] = self._chromedriver
            driver = webdriver.Chrome(self._chromedriver)
            driver.get(url)

            try:
                el = driver.find_element_by_class_name('select-size-js')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == 'WÃ¤hlen Sie bitte Ihre GrÃ¶ÃŸe aus':
                        option.click()
                        break
            except NoSuchElementException:
                pass

            htmsrc = driver.page_source
            driver.quit()
            return htmsrc
        except NoSuchWindowException:
            sys.exit('The window closed unexpectedly.')

    def _gethtml(self, url):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
            con = urllib.request.urlopen(req)
            html = con.read()
            return html
        except Exception as e:
            sys.exit("Error in gethtml function " + str(e))

    def _get_item_details(self,product_link):
        itm = {}

        soup = self._Soup(self._gethtmlwjs(product_link))
        itm['name'] = (soup.find('div', {'itemprop': 'name'}).h1.text.lstrip().rstrip())
        rate = soup.find('span', {'itemprop': 'price'}).text.rstrip()
        itm['price'] = rate[0:-1]
        itm['currency'] = rate[-1]
        itm['description'] = list(filter(None, soup.find('div', {'class': 'panel_descripcion'}).text.split('\n')))
        itm['pflegetipps'] = list(filter(None, soup.find('div', {
            'class': 'composicion productExtra__compositionContainer productExtra__infoContainer'}).text.split(
            '\n')))

        itm['sizes'] = [e.text for e in soup.findAll('option')[1:]]
        itm['Konstenfreie Ruckgabe'] = list(
            filter(None, soup.find('div', {'id': 'fichaInfoEnvio'}).text.split('\n')))
        itm['Konstenloser Versand'] = list(
            filter(None, soup.find('div', {'id': 'fichaInfoDevoluciones'}).text.split('\n')))

        compl_look_items = soup.findAll('div', {'class': 'look-product completa_product span3'})
        compl_look = []
        for ech in compl_look_items:
            compl_look.append({'name': ech.h2.text.strip(), 'url': ech.a['href'], 'price': ech.find('div', {
                'class': 'look-product-price completa_product_price row-fluid fullLook__priceContainer'}).text.strip()})

        itm['Komplete Look'] = compl_look

        itm['colour'] = soup.find('p', {'itemprop': 'color'}).text
        itm['country'] = self.country

        return itm

    def _getproducts(self):
        # loads the products and categories into a dictionary data structure
        soup = self._Soup(self._gethtmlwjs(self._URL))
        proddic = {}

        # proddic['damen']=proddic['herren']=proddic['violeta']=proddic['kinder']=[]
        damen = []
        herren = []
        violeta = []
        kinder = []
        for link in soup.findAll('a', href=True):
            lnk = link['href']
            if "accessoires" in lnk or "artikel" in lnk:
                if 'damen' in lnk:
                    damen.append(lnk)
                elif 'herren' in lnk:
                    herren.append(lnk)
                elif 'violeta' in lnk:
                    violeta.append(lnk)
                elif 'kinder' in lnk:
                    kinder.append(lnk)

        damen_product_links = {}
        for lnk in damen[0:1]:
            soup = self._Soup(self._gethtmlwjs(lnk))
            damen_product_links[lnk.split('/')[-1]] = [e['href'] for e in soup.find_all('a', {'class': "product-list-link product-list-link-js"})]

        herren_product_links = {}
        for lnk in herren[0:1]:
            soup = self._Soup(self._gethtmlwjs(lnk))
            herren_product_links[lnk.split('/')[-1]] = [e['href'] for e in soup.find_all('a', {'class': "product-list-link product-list-link-js"})]

        violeta_product_links = {}
        for lnk in violeta[0:1]:
            soup = self._Soup(self._gethtmlwjs(lnk))
            violeta_product_links[lnk.split('/')[-1]] = [e['href'] for e in soup.find_all('a', {'class': "product-list-link product-list-link-js"})]

        kinder_product_links = {}
        for lnk in kinder[0:1]:
            soup = self._Soup(self._gethtmlwjs(lnk))
            kinder_product_links[lnk.split('/')[-1]] = [e['href'] for e in soup.find_all('a', {'class': "product-list-link product-list-link-js"})]

        damen_items = {}
        for key, value in damen_product_links.items():
            key_items = []
            for product_link in value[0:1]:
                key_items.append(self._get_item_details(product_link))
            damen_items[key] = key_items

        herren_items = {}
        for key, value in herren_product_links.items():
            key_items = []
            for product_link in value[0:1]:
                key_items.append(self._get_item_details(product_link))
            herren_items[key] = key_items

        kinder_items = {}
        for key, value in kinder_product_links.items():
            key_items = []
            for product_link in value[0:1]:
                key_items.append(self._get_item_details(product_link))
            kinder_items[key] = key_items

        violeta_items = {}
        for key, value in violeta_product_links.items():
            key_items = []
            for product_link in value[0:1]:
                key_items.append(self._get_item_details(product_link))
            violeta_items[key] = key_items

        return ({'damen':damen_items,'herren':herren_items,'kinder':kinder_items,'violeta':violeta_items})

    def _dict2json(self, nm):
        import json
        # converting the dictionary of lists into a json format
        with open(nm, 'w') as f:
            f.write(json.dumps(self._products))

    def display(self):
        # To print the result in a dictionary format
        print(self._products)

    def getjson(self, nm):
        # To create a csv file of the results
        self._dict2json(nm)
 
 
 if __name__ == '__main__':
    Mango('DE').getjson('res.json')
