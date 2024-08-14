#!/usr/bin/env python3
"""Main file for testing get_page"""

from web import get_page

url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
print(get_page(url))
