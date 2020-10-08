import re
import logging
from typing import Dict, Any

from locators.book_loctors import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    RATINGS: dict[Any, int] = dict(one=1, two=2, three=3, four=4)
    # {
        # 'one': 1,
        # 'two': 2,
        # 'there': 3,
        # 'four': 4
    # }

    def __repr__(self):
        return f'<Book {self.name}, ${self.price} ({self.rating} stars)'

    @property
    def name(self):
        logger.debug('Find book name....')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name: object = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book name')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}.')
        assert isinstance(item_link, object)
        return item_link

    @property
    def price(self):
        logger.debug('Finding book name...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '$([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book print, `{float_price}.')
        return float(matcher.group(1))

    @property
    def rating(self):
        logger.debug('Finding book rating..')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number

