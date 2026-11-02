# Rental Pricing

A Python 3.14 project for calculating rental costs and managing customer rental orders.

## Specifications

- **Rental Duration**: Rentals are charged per calendar day, counting both the start and end dates inclusively (a same-day rental is 1 day).
- **Cost Calculation**: The cost is the daily rate times the number of days, handled using `decimal.Decimal` and rounded to 2 decimal places.
- **Discounts**: Rentals of 7 days or more receive a 10% discount.
- **Orders**: Each new order starts with an empty item list.
