from django.db import models
from westeros import settings


class CommonModel(models.Model):
    """
    Common Model : Basic model for all models
    """
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    class Meta:
        abstract = True

    # whenever model saved, update the modified date
    def save(self, update_fields=None, **kwargs):
        if update_fields is not None:
            update_fields.append("date_modified")
        super(CommonModel, self).save(update_fields=update_fields, **kwargs)
