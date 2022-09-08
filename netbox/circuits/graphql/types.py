from typing import List

import strawberry
from circuits import filtersets, models
from dcim.graphql.mixins import CabledObjectMixin
from extras.graphql.mixins import CustomFieldsMixin, TagsMixin
from strawberry import auto

from netbox.graphql.types import NetBoxObjectType, ObjectType, OrganizationalObjectType

__all__ = (
    "CircuitTerminationType",
    "CircuitType",
    "CircuitTypeType",
    "ProviderType",
    "ProviderNetworkType",
)


@strawberry.django.type(models.CircuitTermination)
class CircuitTerminationType(
    CustomFieldsMixin, TagsMixin, CabledObjectMixin, ObjectType
):
    # filterset_class = filtersets.CircuitTerminationFilterSet
    created: auto
    last_updated: auto
    # custom_field_data
    # tags:
    # cable:
    # cable_end:
    mark_connected: auto
    # circuit: auto
    term_side: auto
    # site
    # provider_network
    port_speed: auto
    upstream_speed: auto
    xconnect_id: auto
    pp_info: auto
    description: auto
    # changelog:
    # custom_fields:


@strawberry.django.type(models.Circuit)
class CircuitType(NetBoxObjectType):
    # filterset_class = filtersets.CircuitFilterSet
    pass


@strawberry.django.type(models.CircuitType)
class CircuitTypeType(OrganizationalObjectType):
    # filterset_class = filtersets.CircuitTypeFilterSet
    pass


@strawberry.django.type(models.Provider)
class ProviderType(NetBoxObjectType):
    # filterset_class = filtersets.ProviderFilterSet
    pass


@strawberry.django.type(models.ProviderNetwork)
class ProviderNetworkType(NetBoxObjectType):
    # filterset_class = filtersets.ProviderNetworkFilterSet
    pass
