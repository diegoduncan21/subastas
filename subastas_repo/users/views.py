# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required

# Import the reverse lookup function
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render, redirect

# view imports
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from allauth.account.models import EmailAddress
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

    def get_queryset(self):
        return User.objects \
            .exclude(id=self.request.user.id) \
            .exclude(is_superuser=True)


@login_required
def create_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(form.cleaned_data.get('perfil'))
            user.set_password(form.cleaned_data.get('password'))
            EmailAddress.objects.create(user=user,
                                        email=user.username,
                                        verified=True)
            return redirect(reverse("users:list"))
    else:
        form = CreateUserForm()
    return render(request, 'users/user_form.html',
                  {'form': form})


def update_user(request, user_id):
    instance = User.objects.get(id=user_id)
    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=instance)
        if form.is_valid():
            user = form.save()
            user.groups.clear()
            user.groups.add(form.cleaned_data.get('perfil'))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            EmailAddress.objects.get_or_create(user=user,
                                               email=user.username,
                                               verified=True)
            return redirect(reverse("users:list"))
    else:
        form = CreateUserForm(instance=instance,
                              initial={'perfil': instance.groups.last()})
    return render(request, 'users/user_form.html',
                  {'form': form,
                   'instance': instance})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:list')
