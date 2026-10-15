from pydantic import BaseModel, field_validator

FINAL_CONSUMER_VAT = '9999999999999'

# Tipo de identificación → texto en la pantalla Cambio
ID_TYPES = {
    'final': 'Consumidor Final',
    'cedula': 'Cédula',
    'ruc': 'RUC',
    'passport': 'Pasaporte',
}


class Customer(BaseModel):
    """Cliente de la factura (res.partner en Odoo)."""

    id: int = 0  # 0 = todavía no existe en Odoo: se crea al guardar
    vat: str  # número de identificación
    id_type: str = 'cedula'  # clave de ID_TYPES
    name: str = ''  # razón social
    email: str = ''
    street: str = ''  # dirección

    @field_validator('vat', 'name', 'email', 'street', mode='before')
    @classmethod
    def empty_if_false(cls, value):
        # Odoo devuelve False cuando un campo de texto está vacío
        return '' if value is False else value

    @property
    def is_final_consumer(self) -> bool:
        return self.vat == FINAL_CONSUMER_VAT
