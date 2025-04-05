""" Image Stealer """
# Image getting mainly comes to two things
# 1.Getting image url by meta tags
# 2.Geting image by its size
from bs4 import BeautifulSoup
import requests
import random
import re
 
def description_grabber(soup):
    while True:
        # The Variable storing the returning image url
        ultimate_returning_description = ''
        break_it = False
        """ ============  Request ============ """
        # Soup Paased in
        soup = soup
        
        """
        ============================================================ CHECKING IF MEETA TAG PRESENTED THE =================================================
        ============================================================ IF ELSE, THEN CONTINUING ============================================================
        """
        metas = soup.findAll('meta')
        for meta in metas:
            if meta.get("property") != None:
                if 'og:description' in meta.get("property"):
                    ultimate_returning_description = meta.get('content')
                    break_it = True
        """
        ============================================================ CHECKING DESCRIPTION FROM THE TITLE =================================================
        ============================================================ IMAGE SIZE IF ELSE, THEN CONTINUING =================================================
        """
        if break_it == False:
            description = soup.title.text
            ultimate_returning_description = description
            break_it = True

        
        # Returning the image depending on the circumstance
        if break_it == False:
            return None

        if break_it == True:
            return ultimate_returning_description
