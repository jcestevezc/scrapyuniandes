# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyconsoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Archivo donde se agregan todos los campos que se van a traer del scraping
    # Ejemplo: nombre, dependencia, correo.
    
    #--------------------------------------------
    # Campos de los profesores
    #--------------------------------------------
    name = scrapy.Field()
    position = scrapy.Field()
    #name = scrapy.Field()
    #name = scrapy.Field()
    #name = scrapy.Field()
    #name = scrapy.Field()
    
    pass
