from django.contrib import admin
from django.utils.text import slugify
from .models import Course, Provider, Location, ProvidersCourse, Feedback, FAQ, SiteSetting
import datetime

#admin.site.register(SingletonModel)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ["business_name"]
admin.site.register(SiteSetting,SiteSettingAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ["name"]
    #formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE()}
    #}

admin.site.register(Course,CourseAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
    def save_model(self, request, obj, form, change):
        if request.user.first_name:
            obj.added_by = request.user.first_name
        else :
            obj.added_by = request.user.username

        current_year = datetime.datetime.now().year  
        obj.slug=slugify("mbbs-abroad-"+obj.location_country+" "+str(current_year)+" from "+obj.name)
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProviderAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['location'].queryset = Location.objects.filter(location_type__iexact='Country')
        return form

admin.site.register(Provider,ProviderAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ["full_name",]

    def save_model(self, request, obj, form, change):
        if request.user.first_name:
            obj.added_by = request.user.first_name
        else :
            obj.added_by = request.user.username

        obj.slug=slugify("mbbs-in-"+obj.full_name)
        super().save_model(request, obj, form, change)

admin.site.register(Location,LocationAdmin)

class ProvidersCourseAdmin(admin.ModelAdmin):
    list_display = ["duration"]

admin.site.register(ProvidersCourse,ProvidersCourseAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["feedback_type","name","title"]

admin.site.register(Feedback,FeedbackAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ["question_text"]

admin.site.register(FAQ,FAQAdmin)