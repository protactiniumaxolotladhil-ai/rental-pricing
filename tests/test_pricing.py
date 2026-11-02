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
    
    
def test_rental_days_same_day():
    assert rental_days(date(2026, 6, 1), date(2026, 6, 1)) == 1


def test_rental_days_exactly_seven():
    assert rental_days(date(2026, 5, 1), date(2026, 5, 7)) == 7
    
    
    def test_two_orders_keep_own_items():
        order_a = create_order("C4 ")
        order_b = create_order("C5")
        add_item(order_a, "Ladder")
        add_item(order_b, "Drill")
        assert order_a["items"] == ["Ladder"]
        assert order_b["items"] == ["Drill"]