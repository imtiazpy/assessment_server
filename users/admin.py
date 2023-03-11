from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import CustomUser



class UserCreationForm(forms.ModelForm):
    """
    This is a form for creating a user with email, name, and type fields. It has methods for cleaning and saving the form. The clean_password2 method validates that the password entered twice by the user matches or not and raises a validation error if the passwords do not match. The save method overrides the default save method to set the user's password and save the user instance. It returns the saved user instance.
    """

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'type', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords didn't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data)['password1']

        if commit:
            user.save()
        return user
    

class UserChangeForm(forms.ModelForm):
    """
    This is a Django form used for changing user information. It displays fields for email, password (read-only), name, user type, and account status.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name', 'type', 'is_active', 'is_superuser')


class UserAdmin(BaseUserAdmin):
    """
    This is a class that defines the admin interface for the CustomUser model. It sets the add_form, change_form, list_display, list_filter, fieldsets, add_fieldsets, search_fields, ordering, and filter_horizontal attributes to customize the admin interface. The add_fieldsets attribute defines the fields to be displayed when adding a new user. The class inherits from BaseUserAdmin.
    """

    add_form = UserCreationForm
    change_form = UserChangeForm

    list_display = ('id', 'email', 'type', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ('type', 'is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        ('User Info', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'avatar', 'type')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        ('Custom User', {
            'classes': ('wide', ),
            'fields': ('email', 'name', 'type', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'name')
    ordering = ('email', )
    filter_horizontal = ()


# Register the UserAdmin
admin.site.register(CustomUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)