from circuits import filtersets, models
import strawberry
from strawberry import auto
from typing import List

__all__ = ("CircuitTerminationType",)


@strawberry.django.type(models.CircuitTermination)
class CircuitTerminationType:
    id: auto
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


"""
class CircuitType(NetBoxObjectType):

    class Meta:
        model = models.Circuit
        fields = '__all__'
        filterset_class = filtersets.CircuitFilterSet


class CircuitTypeType(OrganizationalObjectType):

    class Meta:
        model = models.CircuitType
        fields = '__all__'
        filterset_class = filtersets.CircuitTypeFilterSet


class ProviderType(NetBoxObjectType):

    class Meta:
        model = models.Provider
        fields = '__all__'
        filterset_class = filtersets.ProviderFilterSet


class ProviderNetworkType(NetBoxObjectType):

    class Meta:
        model = models.ProviderNetwork
        fields = '__all__'
        filterset_class = filtersets.ProviderNetworkFilterSet
"""
