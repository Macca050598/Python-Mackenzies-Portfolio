from django.contrib import admin

from .models import Tag, Project, ProjectImage

class ProjectImageInLine(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "link"
    )
    inlines = [
        ProjectImageInLine
    ]
    #Specify how we can search through the project
    search_fields = (
        "title",
        "description"
    )
    #Have the trailing ',' so it's treated as a tupple (tupple is a way of storing multiple items in a single variable)
    list_filter = ("tags",)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
