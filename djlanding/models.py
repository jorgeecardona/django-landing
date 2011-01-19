from django.db import models
from django import forms


class UserEmail(models.Model):

    # Email
    email = models.CharField(max_length=500)

    # Creation time.
    created_datetime = models.DateTimeField(auto_now_add=True)


class UserEmailForm(forms.ModelForm):

    class Meta(object):
        model = UserEmail
        fields = ('email', )

    # email
    email = forms.EmailField()
