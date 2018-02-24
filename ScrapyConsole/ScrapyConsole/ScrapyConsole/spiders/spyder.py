    #Archivo donde se agrega toda la configuración de donde se va a traer la información

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ScrapyConsole.items import ScrapyconsoleItem

class ScrapyConsole(CrawlSpider):
    # Nombre del spyder
    name = 'spyderVariable'
    # Variable contadora para determinar el número de paginas a recolectar
    item_count = 0
    # Dominio sobre el cual se va a buscar la información. No se sale de este dominio una 
    # vez configurado
    allowed_domain = ['profesores.virtual.uniandes.edu.co']
    # Url desde donde empieza a realizar la busqueda
    start_urls = ['https://profesores.virtual.uniandes.edu.co/',
                  'https://profesores.virtual.uniandes.edu.co/profesores-2017-20/']
    
    rules = {
        # Se definen las reglas de navegación para la realización del scraping
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@href="https://profesores.virtual.uniandes.edu.co/profesores-2017-20/"]'))),
        # Listado de URL de profesores a extraer
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h3[1]/a')),
                            callback = 'parse_item', follow = False)
    }
    
    def parse_item(self, response):
        # Importo la lista de campos definidos en items.py
        profesor_item = ScrapyconsoleItem()
        # Información del profesor
        profesor_item['name'] = response.xpath('normalize-space(//h2/text())').extract_first()
        profesor_item['position'] = response.xpath('//h2/span/text()').extract_first()
        self.item_count += 1
        if self.item_count > 100:
            raise CloseSpider('item_exceeded')
        yield profesor_item
        