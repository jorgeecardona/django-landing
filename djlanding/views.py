# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import UserEmailForm


def index(request):

    if request.method == 'POST':
        user_form = UserEmailForm(request.POST)
        if user_form.is_valid():
            user_email = user_form.save()
            context = {
                'email': user_email.email}
        else:
            context = {
                'user_form': user_form}
    else:
        user_form = UserEmailForm()
        context = {
            'user_form': user_form}

    return render_to_response(
        'landing/index.html', RequestContext(request, context))
