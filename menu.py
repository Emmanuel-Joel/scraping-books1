import logging
from typing import List, Dict
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = """Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available books on the catalogue

Enter your choice:
"""


def print_best_books() -> None:
    logger.info('Finding best books by rating....')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price....')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info('Getting next book from generator of all books....')
    print(next(books_generator))


user_selection = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_selection[user_input]()
        else:
            print("Invalid command:..")
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program')





menu()