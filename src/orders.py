"""An order and its lifecycle."""

import audit
from store import OrderStore


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "open"

    def advance(self):
        if self.status == "open":
            self.status = "paid"
