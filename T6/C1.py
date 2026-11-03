def order_total(unit_price: int, quantity: int, delivery: int = 5) -> int:
    return unit_price * quantity + delivery


unit_price = int(input())
quantity = int(input())
delivery = int(input())
print(order_total(unit_price, quantity))
print(order_total(unit_price, quantity, delivery))
