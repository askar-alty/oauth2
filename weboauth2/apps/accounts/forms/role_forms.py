from django import forms as django_forms

from .. import models


class RoleCreationForm(django_forms.ModelForm):
    scope = django_forms.MultipleChoiceField(
        label='Права доступа в приложении',
        required=True,
        choices=models.Role.SCOPES_CHOICES,
        widget=django_forms.SelectMultiple
    )

    class Meta:
        model = models.Role
        fields = '__all__'


class RoleChangeForm(django_forms.ModelForm):
    scope = django_forms.MultipleChoiceField(
        label='Права доступа в приложении',
        required=True,
        choices=models.Role.SCOPES_CHOICES,
        widget=django_forms.SelectMultiple
    )

    class Meta:
        model = models.Role
        fields = '__all__'
