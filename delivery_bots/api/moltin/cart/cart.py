import httpx

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.errors.exceptions import MoltinError

CART_BASE_URL = 'https://api.moltin.com/v2/carts'


async def add_product_to_cart(
    catalog_product_id: str,
    catalog_product_quantity: int,
    cart_id: str,
) -> httpx.Response:
    """Add catalog product to Moltin cart.

    - A cart can contain a maximum of 100 unique items.
    - The cart currency is set when the first item is added to the cart.
    - The product being added to the cart requires a price in the same currency as the other items in the cart.
      The API returns a 400 error if a price is not defined in the correct currency.

    Args:
        catalog_product_id: id of the product to add to the user's cart;
        catalog_product_quantity: the amount of product added to the cart;
        cart_id: elasticpath cart id (example, id of telegram user).

    Returns:
        object: the collection of cart items.

    Usage example:
        cart_response = await add_product_to_cart(
            catalog_product_id='fpw42e4c-ewe7-4f1c-23a0-074kgo42cbda',
            catalog_product_quantity=5,
            cart_id='1252124',
        )

    Raises:
        MoltinError: Raises an httpx.HTTPStatusError exception.
    """
    headers = await get_headers()
    payload = {
        'data': {
            'id': catalog_product_id,
            'type': 'cart_item',
            'quantity': catalog_product_quantity,
        },
    }
    async with httpx.AsyncClient(base_url=CART_BASE_URL) as client:
        response = await client.post(
            url=f'/{cart_id}/items',
            headers=headers,
            json=payload,
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response
