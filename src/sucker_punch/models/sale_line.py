from pydantic import BaseModel, model_validator

from .product import Product


class SaleLine(BaseModel):
    """Una línea de la factura: un producto, su cantidad y su precio unitario.

    El precio arranca con el de Odoo; con F2 se cambia solo para esta factura.
    """

    product: Product
    quantity: float = 1.0
    price: float = 0.0

    @model_validator(mode='after')
    def product_price(self):
        if 'price' not in self.model_fields_set:
            self.price = self.product.price
        return self

    @property
    def subtotal(self) -> float:
        return self.quantity * self.price

    @property
    def tax(self) -> float:
        return self.subtotal * self.product.tax_percent / 100
