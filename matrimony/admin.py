from django.contrib import admin
from .models import *


#for creating the list of profile in django admin
'''class ProfileAdmin(admin.ModelAdmin):
    #the feilds you wont to show on display , id is by default there and we can display it on admin page
    list_display=['id','name','age','gender','occupation','email']
     #for the hyperlink mean when you click on it it will open your profile
    list_display_links=['name','email']
    #for dispalying only male profile those who are married
    list_filter =  ['gender','is_married']
    # now for the search feild
    #we add the comma in the end beacause python will now treat it as a tuple without , its not considerd as tuple
    search_fields = ('occupation',)'''





# for registering your profile in django admin 
#admin.site.register(profile,ProfileAdmin)
admin.site.register(profile)
admin.site.register(Religion)
admin.site.register(Sect)
admin.site.register(Caste)

admin.site.register(FatherProfile)


class hobbyadmin(admin.ModelAdmin):
    list_display=['name','get_profiles']
    def get_profiles(self,obj):
        hobby_followers = ', '.join([profile.name for profile in obj.profiles.all()])
        return (hobby_followers)
        
    get_profiles.short_description="Followers"
       



admin.site.register(Hobby,hobbyadmin)


# Register your models here.
