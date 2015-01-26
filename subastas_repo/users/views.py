# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from allauth.account.models import EmailAddress, EmailConfirmation
# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import CreateUserForm, UserForm

# Import the customized User model
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateUserForm
    model = User
    template_name = 'subastas/admin/administrador_list_form.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.exclude(id=self.request.user.id)
        return context

    def form_valid(self, form):
        user = form.save()
        user.user_permissions.add(form.cleaned_data.get('perfil'))
        user.set_password(form.cleaned_data.get('password'))
        EmailAddress.objects.create(user=user, email=user.username, verified=True)

        return super(UserCreateView, self).form_valid(form)

    # send the user back to their own page after a successful create
    def get_success_url(self):
        return reverse("home")
