#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

    tax = 0.15

    #calcul sous total
    sous_total = 0
    for item in data:
        sous_total = item[INDEX_QUANTITY] * item[INDEX_PRICE]
    
    #calcul taxes
    taxes = 0
    taxes = sous_total * tax
    total = 0
    total = sous_total + taxes

    facture = name + \name

	return ""










def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
