import main

def test_calculate_average_price():
    products = [
        {'name': 'Product 1', 'price': 100, 'stock': 1},
        {'name': 'Product 2', 'price': 200, 'stock': 2},
        {'name': 'Product 3', 'price': 300, 'stock': 3}
    ]
    result = main.calculate_average_price(products)
    assert result == 200, f'Expected 200, got {result}'


def test_calculate_total_value():
    products = [
        {'name': 'Product 1', 'price': 100, 'stock': 1},
        {'name': 'Product 2', 'price': 200, 'stock': 2},
        {'name': 'Product 3', 'price': 300, 'stock': 3}
    ]
    result = main.calculate_total_value(products)
    assert result == 1400, f'Expected 1400, got {result}'


def test_filter_products_by_stock():
    products = [
        {'name': 'Product 1', 'price': 100, 'stock': 1},
        {'name': 'Product 2', 'price': 200, 'stock': 2},
        {'name': 'Product 3', 'price': 300, 'stock': 3}
    ]
    result = main.filter_products_by_stock(products, 2)
    assert len(result) == 2, f'Expected 2 products, got {len(result)}'
    assert all(product['stock'] >= 2 for product in result), 'Not all products meet the minimum stock requirement'


def test_manage_inventory_sum_price():
    products = [
        {'name': 'Product 1', 'price': 100, 'stock': 1},
        {'name': 'Product 2', 'price': 200, 'stock': 2},
    ]

    def sum_price(products):
        return sum(product['price'] for product in products)

    result = main.manage_inventory(products, sum_price)
    assert result == 300, f'Expected sum of prices to be 300, got {result}'


def test_manage_inventory_filter_low_stock():
    products = [
        {'name': 'Product 1', 'price': 100, 'stock': 1},
        {'name': 'Product 2', 'price': 200, 'stock': 2},
        {'name': 'Product 3', 'price': 300, 'stock': 5},
    ]

    def filter_low_stock(products, threshold):
        return [product for product in products if product['stock'] < threshold]

    result = main.manage_inventory(products, filter_low_stock, 3)
    assert len(result) == 2, f'Expected 2 products, got {len(result)}'
    assert result[0]['name'] == 'Product 1', f'Expected first product to be "Product 1", got {result[0]["name"]}'
