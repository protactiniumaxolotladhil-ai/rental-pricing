from datetime import date
from decimal import Decimal


def rental_days(start: date, end: date) -> int:
    return (end - start).days + 1


def rental_cost(daily_rate: Decimal, start: date, end: date) -> Decimal:
    days = (end - start).days + 1
    subtotal = daily_rate * Decimal(str(days))
    if days >= 7:
        subtotal *= Decimal("0.90")
    return subtotal.quantize(Decimal("0.01"))


def create_order(customer_id: str, items= None) -> dict:
    if items is None:
        items = []
    return {
        "customer_id": customer_id,
        "items": items,
    }


def add_item(order: dict, item: str) -> None:
    order["items"].append(item)
