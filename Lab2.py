Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... from operator import itemgetter
... 
... 
... class Book:
...     """Книга"""
...     def __init__(self, id, title, price, shop_id):
...         self.id = id
...         self.title = title
...         self.price = price
...         self.shop_id = shop_id
... 
... 
... class BookShop:
...     """Книжный магазин"""
...     def __init__(self, id, name):
...         self.id = id
...         self.name = name
... 
... 
... # Книжные магазины
... shops = [
...     BookShop(1, 'Магазин "Книги для всех"'),
...     BookShop(2, 'Магазин "Большая книга"'),
...     BookShop(3, 'Магазин "Книжный рай"'),
... ]
... 
... # Книги
... books = [
...     Book(1, 'Мастер и Маргарита', 500, 1),
...     Book(2, '1984', 400, 1),
...     Book(3, 'Улисс', 600, 2),
...     Book(4, 'Маленький принц', 300, 2),
...     Book(5, 'Война и мир', 800, 3),
... ]
... 
... def main():
...     """Основная функция"""
... 
...     # Соединение данных один-ко-многим 
...     one_to_many = [(b.title, b.price, s.name) 
...                    for s in shops 
...                    for b in books 
...                    if b.shop_id == s.id]
... 
...     print('Список всех связанных книг и книжных магазинов:')
...     res_1 = sorted(one_to_many, key=itemgetter(2))
...     for item in res_1:
...         print(item)
... 
...     print('\nСписок книжных магазинов с суммарной стоимостью книг:')
...     res_2_unsorted = []
...     # Перебираем все книжные магазины
...     for s in shops:
...         # Список книг в магазине
...         s_books = list(filter(lambda i: i[2] == s.name, one_to_many))
...         # Если магазин не пустой
...         if len(s_books) > 0:
...             # Цены на книги в магазине
            s_prices = [price for _, price, _ in s_books]
            # Суммарная стоимость книг в магазине
            s_prices_sum = sum(s_prices)
            res_2_unsorted.append((s.name, s_prices_sum))

    # Сортировка по суммарной стоимости
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for item in res_2:
        print(item)


if __name__ == '__main__':
    main()
