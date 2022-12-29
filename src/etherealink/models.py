from tortoise import fields, models


class URL(models.Model):
    id = fields.IntField(pk=True)
    url_key = fields.CharField(40, unique=True, index=True)
    admin_key = fields.CharField(40+1+10, unique=True, index=True)
    target_url = fields.CharField(255, index=True)
    clicks_left = fields.IntField(null=True)
    expiry = fields.DatetimeField(null=True)
