import os
import datetime
from django.db import models
from django.core.cache import cache
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.mail import send_mail, BadHeaderError

class Location(models.Model):
    Location_Types=(('City','City'),('Country','Country'),('State','State'))
    location_type = models.CharField(max_length=50, choices = Location_Types)
    full_name = models.CharField(max_length=255, unique=True, null=False, default='Jasola Vihar New Delhi')
    postal_code = models.CharField(max_length=6)
    flag_url = models.URLField(max_length = 255, default='', null=True, blank=True)
    slug = models.SlugField(max_length=450,null=True,blank=True)
    description = HTMLField(null=True, blank=True)

    meta_keywords = models.CharField(max_length=255, null=True, blank=True, default='_')
    meta_description = models.CharField(max_length=255, null=True, blank=True, default='_')
    IsActive = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug=slugify("mbbs-in-"+self.full_name)
        super(Location,self).save(*args,**kwargs)
    
class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    short_description = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=255, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=450,null=True,blank=True)
    IsActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Course,self).save(*args,**kwargs)

class Provider(models.Model):
    Contact_Types=(('Admission','Admission'),('Support','Support'))
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    short_description = HTMLField(null=True, blank=True)
    url = models.URLField(max_length = 200, default='https://example.com')    
    logo_url = models.URLField(max_length = 200, default='https://example.com/abc.jpg')
    slug = models.SlugField(max_length=250,null=True,blank=True)

    fb_url = models.URLField(max_length = 200, default='https://facebook.com')
    insta_url = models.URLField(max_length = 200, default='https://instagram.com')
    linkedin_url = models.URLField(max_length = 200, default='https://linkedin.com')
    twitter_url = models.URLField(max_length = 200, default='https://twitter.com')
    
    contact_type = models.CharField(max_length=50, choices=Contact_Types)
    contact_number = models.CharField(max_length=16, default='+91 962 883 3068')
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True, blank=True)
    location_country = models.CharField(max_length=100, null=False, blank=False)
    is_featured = models.BooleanField(default=False)

    IsActive = models.BooleanField(default=True)
    last_modified = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        current_year = datetime.datetime.now().year  
        self.slug=slugify("mbbs-abroad-"+self.location_country+" "+str(current_year)+" from "+self.name)
        super(Provider,self).save(*args,**kwargs)

class ProvidersCourse(models.Model):
    Currency=(('USD','USD'),('INR','INR'))
    Type=(('FullTime','Full Time'),('PartTime','Part Time'))
    Mode=(('Distance','Distance'),('Regular','Regular'))

    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE)

    duration = models.CharField(max_length=16)
    average_cost_to_stay = models.CharField(max_length=20)
    average_cost_to_stay_currency = models.CharField(max_length=5, choices=Currency)
    recognitions= models.CharField(max_length=150)
    description = HTMLField(null=True, blank=True)
    type = models.CharField(max_length=100, choices=Type)
    mode = models.CharField(max_length=100, choices=Mode)    
    fee = models.CharField(max_length=20)
    fee_currency = models.CharField(max_length=5, choices=Currency)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)

    meta_keywords = models.CharField(max_length=255, null=False, blank=False)
    meta_description = models.CharField(max_length=255, null=False, blank=False)
    IsActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.duration

class FAQ(models.Model):
    question_text = models.CharField(max_length=500, null=False, blank=False)
    answer_text = models.CharField(max_length=1000, null=False, blank=False)
    IsActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.question_text

   
class Feedback(models.Model):
    FeedbackType=(('Standard','Standard'),('In-Writing','In-Writing'),('Audio','Audio'),('Video','Video')) 
    
    feedback_type = models.CharField(max_length=50, choices=FeedbackType)
    name = models.CharField(max_length=150, null=False, blank=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    photo_path = models.ImageField(upload_to = 'FeedBacks/photo', null=True, blank=True)
    rating =  models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    feedback = models.CharField(max_length=850, null=True, blank=True, help_text="for Standard type, simple message")
    feedback_path = models.ImageField(upload_to = 'FeedBacks/doc_img', null=True, blank=True, help_text="for in-writing image/photo")
    feedback_url = models.URLField(null=True, blank=True, help_text="for youtube/other video/audio link")  
    feedback_date = models.DateTimeField(auto_now_add=True, blank=True)    
    
    def __str__(self):
        return self.name

class SingletonModel(models.Model):
    
        class Meta:
                abstract = True

        def delete(self, *args, **kwargs):
                pass
                
        def set_cache(self):
                cache.set(self.__class__.__name__, self)

        def save(self, *args, **kwargs):
                self.pk = 1
                super(SingletonModel, self).save(*args, **kwargs)
                self.set_cache()
        
        @classmethod
        def loadd(cls):
                if cache.get(cls.__class__.__name__) is None:
                        obj, created = cls.objects.get_or_create(pk=1)
                        if not created:
                                obj.set_cache()
                return cache.get(cls.__class__.__name__)
        
        @classmethod
        def loadddd(self):
                if cache.get(self.__class__.__name__) is None:
                        obj, created = self.objects.get_or_create(pk=1)
                        if not created:
                                obj.set_cache()
                return cache.get(self.__class__.__name__)
        
        @classmethod
        def load(cls):
                #obj, created = cls.objects.get_or_create(pk=1)
                #return obj
                if cache.get(cls.__name__) is None:
                        obj, created = cls.objects.get_or_create(pk=1)
                        if not created:
                                obj.set_cache()
                return cache.get(cls.__name__)               
                

class SiteSetting(SingletonModel):
    business_name = models.CharField(max_length=255, default='My Business Name')
    business_description = models.CharField(max_length=500, default='Business Description')
    mobile = models.CharField(max_length=16, default='+91 962 883 3068')
    mobile2 = models.CharField(max_length=16, null=True, blank=True)
    mobile3 = models.CharField(max_length=16, null=True, blank=True)
    whatsapp = models.CharField(max_length=16, null=True, blank=True)
    tollfree = models.CharField(max_length=16, default='18008890382')
    email = models.EmailField(default='support@example.com')
    logo_url = models.URLField(max_length = 200, default='https://example.com/abc.jpg')
    favicon_url = models.URLField(max_length = 200, default='https://example.com/abc.jpg')
    featured_video_url = models.URLField(max_length = 200, default='https://youtube.com')

    fb_url = models.URLField(max_length = 200, default='https://facebook.com')
    insta_url = models.URLField(max_length = 200, default='https://instagram.com')
    linkedin_url = models.URLField(max_length = 200, default='https://linkedin.com')
    twitter_url = models.URLField(max_length = 200, default='https://twitter.com')
    youtube_url = models.URLField(max_length = 200, default='https://youtube.com')

    banner_title = models.CharField(max_length=255, default='Banner Title')
    banner_description = models.CharField(max_length=500, default='Banner Description')
    banner1_title = models.CharField(max_length=255, default='Banner1 Title')
    banner1_description = models.CharField(max_length=500, default='Banner1 Description')
    banner2_title = models.CharField(max_length=255, default='Banner2 Title')
    banner2_description = models.CharField(max_length=500, default='Banner2 Description')

    business_HO_address = models.CharField(max_length=150, default='Business HO Address')
    business_HO_city = models.CharField(max_length=75, default='Business HO City')

    meta_title = models.CharField(max_length=255, default='Meta Title')
    meta_keywords = models.CharField(max_length=500, default='Meta Keywords')
    meta_description = models.CharField(max_length=500, default='Meta Description')
    meta_author = models.CharField(max_length=255, default='Meta Author')
    meta_website = models.CharField(max_length=255, default='Meta Website')
    meta_robots = models.CharField(max_length=255, default='index, follow')

    gtm_code = models.CharField(max_length=16, default='NA', help_text = "google tag manager code")
    ga_code = models.CharField(max_length=16, default='NA', help_text = "google analytics code")
    go_code = models.CharField(max_length=16, default='NA', help_text = "google optimizer code")

    fb_page_id = models.CharField(max_length=16, default='NA', help_text = "PageId : FB Messanger Chat Plugin")

    smtp_host = models.CharField(max_length=50, null=True, blank=True, default='smtp.gmail.com')
    smtp_port = models.CharField(max_length=6, null=True, blank=True, default=587)
    use_tls = models.BooleanField(default=True)
    fail_silently = models.BooleanField(default=True)
    host_user = models.CharField(max_length=70, null=True, blank=True)
    host_password = models.CharField(max_length=70, null=True, blank=True)
        



