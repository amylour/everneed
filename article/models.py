from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Article(models.Model):
    """ Article create/manage model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="article_posts")
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(
        max_length=100, default='default alt', null=False, blank=False)
    excerpt = models.TextField(max_length=300, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(max_length=5000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """ Order posts by created on date """
        ordering = ["-created_on"]

    # Django magic method that returns a string rep of an object
    def __str__(self):
        return self.title
