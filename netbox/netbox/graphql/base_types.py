import strawberry
from strawberry import auto

__all__ = ("BaseObjectType",)

#
# Base types
#


class BaseObjectType:
    """
    Base GraphQL object type for all NetBox objects. Restricts the model queryset to enforce object permissions.
    """

    id: auto
