import itertools

from django import forms
from django.utils.text import slugify

from .models import Blog

class AddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'category',
            'body',
        )

    def save(self):

        instance = super(AddForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        max_length = Blog._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        #to make the slug unique we add a cunter to append
        for x in itertools.count(1):
            if not Blog.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)
            
            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()

        return instance