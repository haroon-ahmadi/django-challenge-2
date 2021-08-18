import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, db_index=True)
    price = models.IntegerField(db_index=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name