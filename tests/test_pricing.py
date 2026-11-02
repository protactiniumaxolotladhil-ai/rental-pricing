"""Tests for the rental pricing rules in README.md."""

from datetime import date
from decimal import Decimal

from rental_pricing.pricing import add_item, create_order, rental_cost, rental_days


def test_rental_days_inclusive():
    start = date(2026, 5, 1)
    end = date(2026, 5, 3)
    assert rental_days(start, end) == 3


def test_create_order_isolated_items():
    order1 = create_order("C1")
    add_item(order1, "Tent")
    order2 = create_order("C2")
    assert order1["items"] == ["Tent"]
    assert order2["items"] == []


def test_rental_cost_seven_days_discount():
    cost = rental_cost(Decimal("20.00"), date(2026, 5, 1), date(2026, 5, 7))
    assert cost == Decimal("126.00")


def test_rental_cost_single_day():
    assert rental_cost(Decimal("20.00"), date(2026, 5, 1), date(2026, 5, 1)) == Decimal("20.00")


def test_add_item_to_order():
    items = []
    order = create_order("C3", items)
    add_item(order, "Sleeping Bag")
    assert order["items"] == ["Sleeping Bag"]
