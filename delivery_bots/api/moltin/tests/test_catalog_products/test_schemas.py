import pytest
from delivery_bots.api.moltin.catalog_products.schemas import CatalogProduct


@pytest.fixture
def catalog_product_response():
    return {
        'type': 'product',
        'id': '9eda5ba0-4f4a-4074-8547-ccb05d1b5981',
        'name': 'Crown',
        'slug': 'crown',
        'sku': 'CWLP100BLK',
        'manage_stock': True,
        'description': 'Abstract, sculptural, refined and edgy with a modern twist. Its symmetrical, spoked structure'
        ' generates a clever geometric presence, which works well in a contemporary environment.',
        'price': [
            {
                'amount': 47500,
                'currency': 'USD',
                'includes_tax': True,
            },
        ],
        'status': 'live',
        'commodity_type': 'physical',
        'meta': {
            'timestamps': {
                'created_at': '2017-06-19T14:58:42+00:00',
                'updated_at': '2018-04-10T09:12:05+00:00',
            },
            'display_price': {
                'with_tax': {
                    'amount': 47500,
                    'currency': 'USD',
                    'formatted': '$475.00',
                },
                'without_tax': {
                    'amount': 47500,
                    'currency': 'USD',
                    'formatted': '$475.00',
                },
            },
            'stock': {
                'level': 500,
                'availability': 'in-stock',
            },
            'variation_matrix': [],
        },
        'relationships': {
            'files': {
                'data': [
                    {
                        'type': 'file',
                        'id': '7cc08cbb-256e-4271-9b01-d03a9fac9f0a',
                    },
                ],
            },
            'categories': {
                'data': [
                    {
                        'type': 'category',
                        'id': 'a636c261-0259-4975-ac8e-77246ec9cfe0',
                    },
                ],
            },
            'main_image': {
                'data': {
                    'type': 'main_image',
                    'id': '7cc08cbb-256e-4271-9b01-d03a9fac9f0a',
                },
            },
        },
    }


def test_product_schema(catalog_product_response):
    """Test moltin product schema."""
    catalog_product = CatalogProduct(**catalog_product_response)
    assert catalog_product.type == 'product'
    assert catalog_product.id == '9eda5ba0-4f4a-4074-8547-ccb05d1b5981'
    assert catalog_product.meta.display_price.with_tax.amount == 47500
