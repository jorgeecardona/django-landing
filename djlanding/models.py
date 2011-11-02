import logging
from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.conf import settings
from greatape import MailChimp


class User(models.Model):

    # Email
    email = models.CharField(max_length=500)

    # Creation time.
    created_datetime = models.DateTimeField(auto_now_add=True)


def add_email_to_mailchimp(sender, instance, created, **kwargs):

    # Check first if the mailchimp key is present.
    if not hasattr(settings, 'DJLANDING_MAILCHIMP_API'):
        logging.info('MailChimp API not present')
        return
    mailchimp_api = settings.DJLANDING_MAILCHIMP_API

    # Check for mailchimp list.
    if not hasattr(settings, 'DJLANDING_MAILCHIMP_LIST'):
        logging.error('MailChimp List not defined')
        return
    mailchimp_list = settings.DJLANDING_MAILCHIMP_LIST

    # Subscribe user to list.
    mc = MailChimp(mailchimp_api)
    try:
        mc.listSubscribe(
            id=mailchimp_list,
            email_address=instance.email,
            merge_vars={'EMAIL': instance.email},
            double_optin=False)
    except Exception, e:
        logging.error(e)
        logging.error("Trying to add email: %s." % (instance.email, ))

post_save.connect(add_email_to_mailchimp, sender=User)


class UserForm(forms.ModelForm):

    class Meta(object):
        model = User
        fields = ('email', )

    # email
    email = forms.EmailField()
