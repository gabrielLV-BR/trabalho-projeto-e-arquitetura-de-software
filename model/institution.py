# Institution
# Estado
# Cidade
# IES
# Sigla
# Organização
# Categoria Administrativa

from enum import Enum
from peewee import TextField, IntegerField, PrimaryKeyField
from model.base import BaseModel

class AdministrativeCategory(Enum):
    PUBLIC = 1
    PRIVATE = 2
    SPECIAL = 3

    def parse(category: str):
        category = category.strip().lower()

        match category:
            case 'public' | 'publica' | 'publico':
                return AdministrativeCategory.PUBLIC
            case 'private' | 'privada' | 'privado':
                return AdministrativeCategory.PRIVATE
            case 'special' | 'especial':
                return AdministrativeCategory.SPECIAL

        raise ValueError('Invalid category specified')


class Institution(BaseModel):
    id = PrimaryKeyField()
    ies = TextField(index=True)
    acronym = TextField()
    organization = TextField()
    category = TextField()
    category_type = IntegerField(index=True)

