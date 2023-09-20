from django.contrib import admin
from .models import Article 
from django_summernote.admin import SummernoteModelAdmin


# decorator to register article model and article admin class with admin site
def mark_articles_deleted(modeladmin, request, queryset):
    queryset.update(is_deleted=True)


mark_articles_deleted.short_description = "Mark selected articles as deleted"


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin): 
    actions = [mark_articles_deleted]
    list_display = ('title', 'slug', 'created_on', 'is_deleted')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'is_deleted')
    djrichtextfield_fields = ('content')

    # Needed to ensure deleted articles do not show in search results
    def is_deleted(self, obj):
        # add a method for article deletion to display the 'is_deleted'
        #  field value in the list view
        return obj.is_deleted

    is_deleted.boolean = True  # Display 'is_deleted' as a checkbox

    # credit -> https://docs.djangoproject.com/en/dev/ref/contrib/
    # admin/#django.contrib.admin.ModelAdmin.readonly_fields
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and obj.is_deleted:
            # set additional fields as read-only when 'is_deleted' is True
            readonly_fields += ('title', 'slug', 'content', 'status')
        return readonly_fields

