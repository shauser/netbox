import strawberry
from django.contrib.contenttypes.models import ContentType
from extras.graphql.types import (
    ChangelogMixin,
    CustomFieldsMixin,
    JournalEntriesMixin,
    TagsMixin,
)
from strawberry import auto

from netbox.graphql.base_types import BaseObjectType

__all__ = (
    "ObjectType",
    "OrganizationalObjectType",
    "NetBoxObjectType",
)

#
# Base types
#


class ObjectType(ChangelogMixin, BaseObjectType):
    """
    Base GraphQL object type for unclassified models which support change logging
    """

    pass


class OrganizationalObjectType(
    ChangelogMixin, CustomFieldsMixin, TagsMixin, BaseObjectType
):
    """
    Base type for organizational models
    """

    pass


class NetBoxObjectType(
    ChangelogMixin, CustomFieldsMixin, JournalEntriesMixin, TagsMixin, BaseObjectType
):
    """
    GraphQL type for most NetBox models. Includes support for custom fields, change logging, journaling, and tags.
    """

    pass


#
# Miscellaneous types
#


class ContentTypeType:
    class Meta:
        model = ContentType
        fields = ("id", "app_label", "model")
