import pytest
import ujson

from delivery_bots.api.moltin.catalog_products.schemas import (
    CatalogProduct,
    DisplayPrice,
    Meta,
    Stock,
    TaxPrice,
)


@pytest.fixture
def classic_tomato_pizza():
    return CatalogProduct(
        type='product',
        id='ce9b47f7-58ee-43f7-9712-c6ee6bd6e24b',
        status='live',
        name='Classic Tomato',
        slug='classic-tomato',
        sku='classic-tomato-001',
        description='Crushed Tomato Sauce, Basil, Romano, Olive Oil, Mozzarella',
        meta=Meta(
            display_price=DisplayPrice(
                with_tax=TaxPrice(amount=1295, currency='USD', formatted='$12.95'),
                without_tax=TaxPrice(amount=1295, currency='USD', formatted='$12.95'),
            ),
            stock=Stock(availability='in-stock', level=500),
        ),
    )


@pytest.fixture
def buffalo_chicken_pizza():
    return CatalogProduct(
        type='product',
        id='ce9b47f7-65ee-44f7-5214-c6ee6bd6e24b',
        status='live',
        name='Buffalo Chicken',
        slug='buffalo-chicken',
        sku='buffalo-chicken-001',
        description='Cheddar Mozzarella Blend, Roasted Red Onion, Hickory Smoked Bacon, Buttermilk Ranch Drizzle',
        meta=Meta(
            display_price=DisplayPrice(
                with_tax=TaxPrice(amount=1995, currency='USD', formatted='$19.95'),
                without_tax=TaxPrice(amount=1995, currency='USD', formatted='$19.95'),
            ),
            stock=Stock(availability='in-stock', level=500),
        ),
    )


@pytest.fixture
def catalog_products_response(classic_tomato_pizza, buffalo_chicken_pizza):
    return ujson.dumps(
        {
            'data': [classic_tomato_pizza.dict(), buffalo_chicken_pizza.dict()],
        },
    )


@pytest.fixture
def catalog_product_detail_response(classic_tomato_pizza):
    return ujson.dumps(
        {
            'data': classic_tomato_pizza.dict(),
        },
    )


@pytest.fixture
def headers():
    return {
        'Authorization': 'Bearer 212LJ3k0i2382364HIUEjfeJB98yvH',
        'Content-Type': 'application/json',
    }
