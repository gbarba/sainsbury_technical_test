# -*- coding: utf-8 -*-
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import argparse
import simplejson
import requests
# I use Decimal because floats are buggy
from decimal import Decimal
from lxml import html


def _scrap_product_list(html_str):
    """Get the content of product list page and yield a dictionary for each
    product"""
    html_tree = html.fromstring(html_str)
    for product_tree in html_tree.cssselect('div#productLister '
            '> ul.productLister > li div.productInner'):
        link_tree, = product_tree.cssselect('div.productInfo > h3 a')
        title = link_tree.text.strip()
        product_url = link_tree.get('href')

        price_tree, = product_tree.cssselect('div.pricing > p.pricePerUnit')
        unit_price = Decimal(price_tree.text.strip().replace(u'£', '').replace(
            '&pound', ''))

        product_response = requests.get(product_url)
        size = int(product_response.headers['content-length']) / 1000.
        product_html_tree = html.fromstring(product_response.content)

        product_descriptions = []
        description_tree = product_html_tree.xpath(
            '//div[@id="information"]/productcontent/htmlcontent/'
            'h3[@class="productDataItemHeader"][string() = "Description"]/'
            'following-sibling::div[@class="productText"][1]/p')
        if description_tree:
            product_descriptions += [p.text.strip().replace('\n', '')
                for p in description_tree if p.text and p.text.strip()]

        storage_tree = product_html_tree.xpath(
            '//div[@id="information"]/productcontent/htmlcontent/'
            'h3[@class="productDataItemHeader"][string() = "Storage"]/'
            'following-sibling::div[@class="productText"][1]/p')
        if storage_tree:
            product_descriptions += [p.text.strip().replace('\n', '')
                for p in storage_tree if p.text and p.text.strip()]

        yield {
            'title': title,
            'size': '%.fkb' % size,
            'unit_price': unit_price,
            'description': ' - '.join(product_descriptions),
            }


def scrap_html(html_str):
    """Parse <html_str> and return a JSON with the found products and a total
    of their unit prices

    Return: {
        "results": [{
                "title": "Product title",
                "size": "Product page size, in kb",
                "unit_price": unit.price (float),
                "description": "Description"
            }, {
            ...
            }
        ],
        "total": sum-of-unit.price (float)
    }
    """
    products_list = []
    total = Decimal(0)
    for product_item in _scrap_product_list(html_str):
        products_list.append(product_item)
        total += product_item['unit_price']

    return {
        'results': products_list,
        'total': total,  # if it must to be
        }


def scrap(url, indent_output=False):
    """Gets <url> content pointing to a Sainsbury's groceries product list and
    parse it (see scrap_html documentation to know the returned format).
    """
    return simplejson.dumps(scrap_html(requests.get(url).content),
        use_decimal=True,
        sort_keys=True,
        indent=4 * ' ' if indent_output else None)


def main():
    parser = argparse.ArgumentParser(prog='scrap-groceries')
    parser.add_argument('url',
        help="The URL to Sainsbury's groceries product list to be scrapped")
    parser.add_argument('--pretty', '-p', dest='pretty_output',
        action='store_true')

    options = parser.parse_args()
    print scrap(options.url, indent_output=options.pretty_output)


if __name__ == '__main__':
    main()
