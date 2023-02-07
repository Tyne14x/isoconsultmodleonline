from django.contrib.auth.forms import UserCreationForm


class RegisterFrom(UserCreationForm):
    class Meta(UserCreationForm):
        fields = UserCreationForm.Meta.fields