from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
# from sorl.thumbnail import ImageField, get_thumbnail


class Case(models.Model):
    # these are the attributes in the database, so basically these are the fileds of the database
    title = models.CharField(max_length=100)
    content = models.TextField()
    # we dont execute that .now funtion right now but we just want to pass the actual function as the default value
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    evidence_image = models.ImageField(
        upload_to='images/', blank=True, null=True, )

    def __str__(self):
        return self.title


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('evidence_image',)

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['evidence_image'].required = False
