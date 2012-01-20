from .models import User

TASTYPIE_INSTALLED = True
try:
    from tastypie.resources import ModelResource
    from tastypie.authentication import Authorization
except:
    TASTYPIE_INSTALLED = False

if TASTYPIE_INSTALLED:
    class UserResource(ModelResource):
        " Resource to add an user to the list."

        class Meta(object):
            queryset = User.objects.all()
            resource_name = 'landing/users'
            fields = ['email']
            authorization = Authorization()
            allowed_methods = ['post']
            always_return_data = True
