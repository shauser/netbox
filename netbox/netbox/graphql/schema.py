from typing import List

import strawberry
from circuits.graphql.schema import CircuitsQuery
# from dcim.graphql.schema import DCIMQuery
# from extras.graphql.schema import ExtrasQuery
# from extras.registry import registry
# from ipam.graphql.schema import IPAMQuery
# from tenancy.graphql.schema import TenancyQuery
# from users.graphql.schema import UsersQuery
# from virtualization.graphql.schema import VirtualizationQuery
# from wireless.graphql.schema import WirelessQuery


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query(
    CircuitsQuery,
    # DCIMQuery,
    # ExtrasQuery,
    # IPAMQuery,
    # TenancyQuery,
    # UsersQuery,
    # VirtualizationQuery,
    # WirelessQuery,
):
    pass


schema = strawberry.Schema(query=Query)
