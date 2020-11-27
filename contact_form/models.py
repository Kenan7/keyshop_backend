from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=12)
    message = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        return super(ContactForm, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Contact Forms"
