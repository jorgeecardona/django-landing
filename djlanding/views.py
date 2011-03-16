# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from models import UserForm

DEFAULT_TEMPLATE = settings.DJLANDING_DEFAULT_TEMPLATE if hasattr(settings, 'DJLANDING_DEFAULT_TEMPLATE') else 'landing/index.html'

def index(request, success_template=''):
    template = DEFAULT_TEMPLATE
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            context = {
                'user_form': user_form,
                'email': user.email}
        else:
            context = {
                'user_form': user_form}
        if success_template:
            template = success_template
    else:
        user_form = UserForm()
        context = {
            'user_form': user_form}

    return render_to_response(
        template, RequestContext(request, context))
