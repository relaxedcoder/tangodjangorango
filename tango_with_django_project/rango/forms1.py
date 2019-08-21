from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, Userprofile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter Category Name")
    # views = forms.IntegerField(initial=0, help_text="Views")
    # likes = forms.IntegerField(initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ["name"]


class PageForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter Page Name ")
    url = forms.URLField(max_length=200, help_text="Please enter Page URL")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ("category",)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', "email", "password")

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('website', 'picture')
