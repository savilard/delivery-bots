from delivery_bots.bots.tgbot.cart.handlers import register_handler_cart
from delivery_bots.bots.tgbot.catalog_product_detail.handlers import (
    register_catalog_product_detail_handler,
)
from delivery_bots.bots.tgbot.checkout.customer_contacts.handlers import (
    register_handler_waiting_email,
)
from delivery_bots.bots.tgbot.checkout.delivery.handlers import (
    register_handler_delivery,
)
from delivery_bots.bots.tgbot.checkout.delivery_man.handlers import (
    register_handler_take_order_button,
)
from delivery_bots.bots.tgbot.checkout.location.handlers import (
    register_handlers_location,
)
from delivery_bots.bots.tgbot.menu.handlers import register_menu_handler
from delivery_bots.bots.tgbot.servises.filters.role import (
    CustomerFilter,
    DeliveryManFilter,
)
from delivery_bots.bots.tgbot.start.handlers import register_start_handler


def register_handlers(dp) -> None:
    """Registers bot handlers."""
    register_start_handler(dp)
    register_menu_handler(dp)
    register_catalog_product_detail_handler(dp)
    register_handler_cart(dp)
    register_handlers_location(dp)
    register_handler_waiting_email(dp)
    register_handler_delivery(dp)
    register_handler_take_order_button(dp)


def register_filters(dp) -> None:
    """Registers bot filters."""
    dp.filters_factory.bind(DeliveryManFilter)
    dp.filters_factory.bind(CustomerFilter)
