from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    edition = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255)
    year = models.IntegerField()
    authors = models.ManyToManyField('Author')
    publishing_company = models.ForeignKey('PublishingCompany')
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    website = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)


class PublishingCompany(models.Model):

    name = models.CharField(max_length=255)
    website = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name
