from django.db.models import Model
from django.db.models import CharField

# Create your models here.

class Example(Model):
    name = CharField(max_length=45)
    lastname = CharField(max_length=45)

    def __str__(self) -> str:
        return f'{self.name} {self.lastname}'
