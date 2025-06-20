import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    """Создает цену в страйпе."""

    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product_data={"name": "Платеж за курс"},
    )
    return price


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="subscription",
    )
    return session.get("id"), session.get("url")
