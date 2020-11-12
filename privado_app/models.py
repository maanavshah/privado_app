from djongo import models


class Templates(models.Model):
    type = models.TextField()
    entity = models.TextField()
    customerId = models.TextField()
    law = models.TextField()
    fields = models.JSONField()
    objects = models.DjongoManager()


class UserTable(models.Model):
    email = models.TextField()
    phone = models.TextField()
    userId = models.TextField()
    objects = models.DjongoManager()
