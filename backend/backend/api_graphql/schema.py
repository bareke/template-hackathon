
from graphene import ObjectType
from graphene.relay import Node
from .data.example.types import ExampleNode
from graphene_django.filter import DjangoFilterConnectionField

# Schema definition


class Query(ObjectType):
    example = Node.Field(ExampleNode)
    all_examples = DjangoFilterConnectionField(ExampleNode)


class Mutation(ObjectType):
    pass
