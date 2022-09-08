import typing

# schema.py
import strawberry

from .types import *


@strawberry.type
class CircuitsQuery:
    circuit: CircuitType = strawberry.django.field()
    circuit_list: typing.List[CircuitType] = strawberry.django.field()

    circuit_termination: CircuitTerminationType = strawberry.django.field()
    circuit_termination_list: typing.List[
        CircuitTerminationType
    ] = strawberry.django.field()

    circuit_type: CircuitTypeType = strawberry.django.field()
    circuit_type_list: typing.List[CircuitTypeType] = strawberry.django.field()

    provider: ProviderType = strawberry.django.field()
    provider_list: typing.List[ProviderType] = strawberry.django.field()

    provider_network: ProviderNetworkType = strawberry.django.field()
    provider_network_list: typing.List[ProviderNetworkType] = strawberry.django.field()
