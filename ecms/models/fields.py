from django.db import models
from ecms import forms


class TemplateFilePathField(models.FilePathField):
    """
    A field to select a template path.
    """
    def __init__(self, verbose_name=None, path='', **kwargs):
        defaults = dict(match=r'.*\.html$', recursive=True)
        defaults.update(kwargs)
        super(TemplateFilePathField, self).__init__(verbose_name, path=path, **defaults)

    def formfield(self, **kwargs):
        # Like the FilePathField, the formfield does the actual work
        defaults = {'form_class': forms.TemplateFilePathField}
        defaults.update(kwargs)
        return super(TemplateFilePathField, self).formfield(**defaults)