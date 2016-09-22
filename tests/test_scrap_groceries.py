# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import os.path
import sys
import unittest
from decimal import Decimal

try:
    from scrap_groceries import scrap_html
except ImportError:
    sys.path.insert(0, os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..'))
    from scrap_groceries import scrap_html

__all__ = ['suite']


class ScrapGroceriesTestCase(unittest.TestCase):
    'Test scrap_groceries'

    def test_html_scrapping(self):
        expected_result = {
            "results": [{
                    "title": "Sainsbury's Apricot Ripe & Ready x5",
                    "size": "39kb",
                    "unit_price": Decimal('3.50'),
                    "description": "Apricots",
                    }, {
                    "title": "Sainsbury's Avocado Ripe & Ready XL Loose 300g",
                    "size": "40kb",
                    "unit_price": Decimal('1.50'),
                    "description": "Avocados",
                    }, {
                    "title": "Sainsbury's Avocado, Ripe & Ready x2",
                    "size": "44kb",
                    "unit_price": Decimal('1.80'),
                    "description": ("Avocados - At home refrigerate for "
                        "freshness, prepare immediately prior to eating."),
                    }, {
                    "title": "Sainsbury's Avocados, Ripe & Ready x4",
                    "size": "40kb",
                    "unit_price": Decimal('3.20'),
                    "description": ("Avocados - At home keep refrigerated to "
                        "prevent over ripening. For best flavour, serve at "
                        "room temperature."),
                    }, {
                    "title": ("Sainsbury's Conference Pears, Ripe & Ready x4 "
                        "(minimum)"),
                    "size": "39kb",
                    "unit_price": Decimal('1.50'),
                    "description": "Conference",
                    }, {
                    "title": "Sainsbury's Golden Kiwi x4",
                    "size": "39kb",
                    "unit_price": Decimal('1.80'),
                    "description": (
                        "Gold Kiwi - At home, refrigerate for freshness."),
                    }, {
                    "title": "Sainsbury's Kiwi Fruit, Ripe & Ready x4",
                    "size": "40kb",
                    "unit_price": Decimal('1.80'),
                    "description": ("Kiwi - At home, refrigerate for "
                        "freshness. Wash before use. For best flavour, serve "
                        "at room temperature."),
                    },
                ],
            "total": Decimal('15.10'),
            }
        example_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'Ripe_ready_Sainsburys.html')
        with open(example_file_path, 'r') as f:
            scrap_result = scrap_html(f.read())

        self.maxDiff = None
        self.assertDictEqual(scrap_result, expected_result)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(ScrapGroceriesTestCase)


if __name__ == '__main__':
    suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
