import strawberry
from strawberry import auto
from extras import filtersets, models
from extras.graphql.mixins import CustomFieldsMixin, TagsMixin
from netbox.graphql.types import BaseObjectType, ObjectType

__all__ = (
    "ConfigContextType",
    "CustomFieldType",
    "CustomLinkType",
    "ExportTemplateType",
    "ImageAttachmentType",
    "JournalEntryType",
    "ObjectChangeType",
    "TagType",
    "WebhookType",
)


@strawberry.django.type(models.ConfigContext)
class ConfigContextType(ObjectType):
    # filterset_class = filtersets.ConfigContextFilterSet
    pass


@strawberry.django.type(models.CustomField)
class CustomFieldType(ObjectType):
    # filterset_class = filtersets.CustomFieldFilterSet
    pass


@strawberry.django.type(models.CustomLink)
class CustomLinkType(ObjectType):
    # filterset_class = filtersets.CustomLinkFilterSet
    pass


@strawberry.django.type(models.ExportTemplate)
class ExportTemplateType(ObjectType):
    # filterset_class = filtersets.ExportTemplateFilterSet
    pass


@strawberry.django.type(models.ImageAttachment)
class ImageAttachmentType(BaseObjectType):
    # filterset_class = filtersets.ImageAttachmentFilterSet
    pass


@strawberry.django.type(models.JournalEntry)
class JournalEntryType(CustomFieldsMixin, TagsMixin, ObjectType):
    # filterset_class = filtersets.JournalEntryFilterSet
    pass


@strawberry.django.type(models.ObjectChange)
class ObjectChangeType(BaseObjectType):
    # filterset_class = filtersets.ObjectChangeFilterSet
    pass


@strawberry.django.type(models.Tag)
class TagType(ObjectType):
    # filterset_class = filtersets.TagFilterSet
    pass


@strawberry.django.type(models.Webhook)
class WebhookType(ObjectType):
    # filterset_class = filtersets.WebhookFilterSet
    pass
