class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

    def average_price(self):
        if not self.__products:
            return 0
        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", 0, 1000.0)
    except ValueError as e:
        print("Возникла ошибка ValueError при попытке добавить продукт с нулевым количеством:", e)
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", 5, 180000.0)
    product2 = Product("Iphone 15", 8, 210000.0)
    product3 = Product("Xiaomi Redmi Note 11", 14, 31000.0)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print("Средняя цена в категории 'Смартфоны':", category1.average_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print("Средняя цена в пустой категории:", category_empty.average_price())
