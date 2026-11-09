def reconcile_orders(products, events):
    quantities = {}
    for product in products:
        quantities[product] = 0
    rejected = 0

    for action, product, amount in events:
        if action == 'ORDER':
            quantities[product] += amount
        elif quantities[product] >= amount:
            quantities[product] -= amount
        else:
            rejected += 1
    
    result = []
    for quantity in quantities:
        result.append(quantities[quantity])
    return result, rejected


if __name__ == "__main__":
    n = int(input())
    products = input().split()
    m = int(input())
    events = []
    for event_number in range(m):
        action, product, amount = input().split()
        events.append((action, product, int(amount)))
    quantities, rejected = reconcile_orders(products, events)
    print('Quantities:', *quantities)
    print('Rejected:', rejected)