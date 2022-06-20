from django.contrib import admin
from .models import Course, Provider, Location, ProvidersCourse, Feedback, FAQ, SiteSetting

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
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(ProviderAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['location'].queryset = Location.objects.filter(location_type__iexact='Country')
        return form

admin.site.register(Provider,ProviderAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ["full_name"]

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