import strawberry
from strawberry import auto
from django.contrib.contenttypes.models import ContentType
from extras.graphql.mixins import (
    ChangelogMixin,
    CustomFieldsMixin,
    JournalEntriesMixin,
    TagsMixin,
)

__all__ = (
    "BaseObjectType",
    "ObjectType",
    "OrganizationalObjectType",
    "NetBoxObjectType",
)

#
# Base types
#


class BaseObjectType:
    """
    Base GraphQL object type for all NetBox objects. Restricts the model queryset to enforce object permissions.
    """

    id: auto


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
