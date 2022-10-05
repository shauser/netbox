import graphene
from dcim.graphql.types import InterfaceType
from dcim.models import Interface
from ipam.graphql.types import FHRPGroupType, VLANType
from ipam.models import FHRPGroup, VLAN
from virtualization.graphql.types import VMInterfaceType
from virtualization.models import VMInterface


class IPAddressAssignmentType(graphene.Union):
    class Meta:
        types = (
            InterfaceType,
            FHRPGroupType,
            VMInterfaceType,
        )

    @classmethod
    def resolve_type(cls, instance, info):
        if type(instance) == Interface:
            return InterfaceType
        if type(instance) == FHRPGroup:
            return FHRPGroupType
        if type(instance) == VMInterface:
            return VMInterfaceType


class L2VPNAssignmentType(graphene.Union):
    class Meta:
        types = (
            InterfaceType,
            VLANType,
            VMInterfaceType,
        )

    @classmethod
    def resolve_type(cls, instance, info):
        if type(instance) == Interface:
            return InterfaceType
        if type(instance) == VLAN:
            return VLANType
        if type(instance) == VMInterface:
            return VMInterfaceType
