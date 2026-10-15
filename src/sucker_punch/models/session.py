from pydantic import BaseModel


class Session(BaseModel):
    """Usuario que entró a la app y su empresa en Odoo."""

    uid: int
    user_name: str
    company_name: str
    country_code: str = ''  # 'EC' con la localización de Ecuador
