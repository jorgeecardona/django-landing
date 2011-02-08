# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import UserForm


def index(request):
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
    else:
        user_form = UserForm()
        context = {
            'user_form': user_form}

    return render_to_response(
        'landing/index.html', RequestContext(request, context))
