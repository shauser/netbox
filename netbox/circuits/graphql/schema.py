from .types import *

# schema.py
import strawberry
from typing import List


@strawberry.type
class CircuitsQuery:
    circuit_list: List[CircuitTerminationType] = strawberry.django.field()


"""
class CircuitsQuery(graphene.ObjectType):
    circuit = ObjectField(CircuitType)
    circuit_list = ObjectListField(CircuitType)

    circuit_termination = ObjectField(CircuitTerminationType)
    circuit_termination_list = ObjectListField(CircuitTerminationType)

    circuit_type = ObjectField(CircuitTypeType)
    circuit_type_list = ObjectListField(CircuitTypeType)

    provider = ObjectField(ProviderType)
    provider_list = ObjectListField(ProviderType)

    provider_network = ObjectField(ProviderNetworkType)
    provider_network_list = ObjectListField(ProviderNetworkType)
"""
