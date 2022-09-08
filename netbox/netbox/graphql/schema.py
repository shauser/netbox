import strawberry
from typing import List
from circuits.graphql.schema import CircuitsQuery


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query(CircuitsQuery):
    pass


schema = strawberry.Schema(query=Query)
