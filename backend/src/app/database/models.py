import mongoengine as db


class Reaction(db.Document):
    """
    A DB document representing a reaction between two materials and a technic.
    """
    materials = db.SortedListField(db.StringField(), max_length=2, required=True)
    technic = db.StringField(required=True)

    def __repr__(self):
        return f'Reaction({self.technic} - {",".join(self.materials)})'

    def json(self):
        return {
            'materials': self.materials,
            'technic': self.technic,
        }


class Effect(db.Document):
    """
    An DB document model representing an alchemy effect.
    """
    name = db.StringField(required=True)
    reactions = db.ListField(db.ReferenceField(Reaction), required=True)
    enhance = db.BooleanField(default=False, null=True)
    enhance_description = db.StringField(default='', null=True)

    meta = {
        'index': ['name']
    }

    def __repr__(self):
        return f'Effect({self.name})'

    def json(self):
        return {
            'name': self.name,
            'reactions': [material.json() for material in self.reactions],
            'enhance': self.enhance,
            'enhanceDescription': self.enhance_description
        }


class PotionType(db.Document):
    """
    An DB document model representing an alchemy effect.
    """
    name = db.StringField(required=True)
    effects = db.SortedListField(db.ReferenceField(Effect), max_length=2, required=True)
    description = db.StringField(required=True)

    meta = {
        'index': ['name']
    }

    def __repr__(self):
        return f'PotionType({self.name})'

    def json(self):
        return {
            'name': self.name,
            'effects': [effect.json() for effect in self.effects],
            'description': self.description
        }


class Potion(db.Document):
    """
    An DB document model representing a potion.
    """
    name = db.StringField(required=True, unique=True)
    effects = db.ListField(db.ReferenceField(Effect), required=True)
    types = db.ListField(db.ReferenceField(PotionType), required=False)
    description = db.StringField(required=True)

    meta = {
        'index': ['name']
    }

    def __repr__(self):
        return f'Potion({self.name})'

    def json(self):
        return {
            'name': self.name,
            'effects': [effect.name for effect in self.effects],
            'description': self.description,
        }
