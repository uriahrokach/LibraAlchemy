import mongoengine as db


class Effect(db.Document):
    """
    An DB document model representing an alchemy effect.
    """
    name = db.StringField(required=True)
    materials = db.SortedListField(db.StringField(), max_length=2, required=True)
    technic = db.StringField(required=True)

    meta = {
        'index': ['name']
    }

    def __repr__(self):
        return f'Effect({self.name})'

    def json(self):
        return {
            'name': self.name,
            'materials': self.materials,
            'technic': self.technic,
        }


class Potion(db.Document):
    """
    An DB document model representing a potion.
    """
    name = db.StringField(required=True, unique=True)
    effects = db.SortedListField(db.ReferenceField(Effect), required=True)
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