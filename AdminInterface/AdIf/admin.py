from django.contrib import admin
from AdIf.models import Movie,Customer

# Register your models here.
#----------------change the order of model view------------------#
class MovieAdmin(admin.ModelAdmin):

    fields=['release_year','title','length']

    #------------add attribute search-----------------#
    search_fields=['title']

    #------------add filter-----------#
    list_filter=['release_year']

    #-----add more attribute to list display----#
    list_display=['title','release_year','length']

    #---------edit a list in ListView itself--------_#
    list_editable=['length']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Customer)
