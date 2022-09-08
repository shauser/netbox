import typing

import strawberry
import strawberry_django
from extras import filtersets, models

from netbox.graphql.base_types import BaseObjectType

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
    "ChangelogMixin",
    "ConfigContextMixin",
    "CustomFieldsMixin",
    "ImageAttachmentsMixin",
    "JournalEntriesMixin",
    "TagsMixin",
)


class ConfigContextMixin:

    """
    config_context = GenericScalar()

    """

    @strawberry_django.field
    def config_context(self, info) -> typing.Dict:
        return self.get_config_context()


class CustomFieldsMixin:
    """
    custom_fields = GenericScalar()

    def resolve_custom_fields(self, info):
        return self.custom_field_data
    """

    pass


class ImageAttachmentsMixin:
    """
    image_attachments = graphene.List('extras.graphql.types.ImageAttachmentType')

    def resolve_image_attachments(self, info):
        return self.images.restrict(info.context.user, 'view')
    """

    pass


class JournalEntriesMixin:
    """
    journal_entries = graphene.List('extras.graphql.types.JournalEntryType')

    def resolve_journal_entries(self, info):
        return self.journal_entries.restrict(info.context.user, 'view')
    """

    pass


class TagsMixin:
    """
    tags = graphene.List('extras.graphql.types.TagType')

    def resolve_tags(self, info):
        return self.tags.all()
    """

    pass


@strawberry.django.type(models.ObjectChange)
class ObjectChangeType(BaseObjectType):
    # filterset_class = filtersets.ObjectChangeFilterSet
    pass


class ChangelogMixin:
    """
    changelog = graphene.List('extras.graphql.types.ObjectChangeType')

    """

    @strawberry_django.field
    def changelog(self) -> typing.List[ObjectChangeType]:
        content_type = ContentType.objects.get_for_model(self)
        object_changes = ObjectChange.objects.filter(
            changed_object_type=content_type, changed_object_id=self.pk
        )
        return object_changes.restrict(info.context.user, "view")


@strawberry.django.type(models.ConfigContext)
class ConfigContextType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.ConfigContextFilterSet
    pass


@strawberry.django.type(models.CustomField)
class CustomFieldType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.CustomFieldFilterSet
    pass


@strawberry.django.type(models.CustomLink)
class CustomLinkType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.CustomLinkFilterSet
    pass


@strawberry.django.type(models.ExportTemplate)
class ExportTemplateType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.ExportTemplateFilterSet
    pass


@strawberry.django.type(models.ImageAttachment)
class ImageAttachmentType(BaseObjectType):
    # filterset_class = filtersets.ImageAttachmentFilterSet
    pass


@strawberry.django.type(models.JournalEntry)
class JournalEntryType(ChangelogMixin, CustomFieldsMixin, TagsMixin, BaseObjectType):
    # filterset_class = filtersets.JournalEntryFilterSet
    pass


@strawberry.django.type(models.Tag)
class TagType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.TagFilterSet
    pass


@strawberry.django.type(models.Webhook)
class WebhookType(ChangelogMixin, BaseObjectType):
    # filterset_class = filtersets.WebhookFilterSet
    pass
