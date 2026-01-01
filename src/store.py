"""Keeps orders in memory."""


class Store:
    def __init__(self):
        self.items = {}

    def get(self, key):
        return self.items.get(key)


class OrderStore(Store):
    def put(self, order):
        self.items[order.order_id] = order
