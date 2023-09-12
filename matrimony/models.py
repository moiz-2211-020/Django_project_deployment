from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
#define the media_route in settings file in core folder
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Religion(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    

class Sect(models.Model):
    name = models.CharField(max_length=100)
    #the many to one relationship b/w sect and religion
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name="sects")
    def __str__(self) :
        return self.name

class Caste(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name
    

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    #we want that the hobby class looks like hobbies in the admin panel so for that purpose we will create this meta class and do the following stuff
    class Meta:
        verbose_name_plural= "Hobbies"


    
    def __str__(self) :
        return self.name
    
    
class FatherProfile(models.Model):
    name = models.CharField(max_length=100)
    occupation= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self) :
        return self.name
        







class profile(models.Model):
    Gender_choice= [('M','Male'),('F','Female')]
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    profile_pic=models.ImageField(null=True,blank=True)
    gender=models.CharField(max_length=1,choices=Gender_choice)
    occupation= models.CharField(max_length=100,null=True,blank=True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(max_length=1,default=False)
    #here related_name = profile means that it create a list with the name profile in Religion model
    #CASCADE: When an object referenced by a ForeignKey or OneToOneField is deleted, the referencing object is also deleted. This ensures that there are no orphaned objects referencing a non-existing object.
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name="profile",null=True) 
    sect= models.ForeignKey(Sect, on_delete=models.CASCADE,related_name="sect",null=True)
    caste= models.ForeignKey(Caste, on_delete=models.CASCADE,related_name="caste",null=True)
    #many to many relationship, in many to many relationship we will not use cascade because we dont need to deletethe whole tabble 
    hobby = models.ManyToManyField(Hobby,related_name= "profiles")
    father = models.OneToOneField(FatherProfile,on_delete=models.CASCADE, related_name="dependence",null=True)



    #for the update meesage in the terminal.what we can do is 

    #this syntax will remain same from function defining too super() function and our logic will be written betwwn them
    def save(self,*args,**kwargs):
        print(f'profile is updated for {self.name}') 

        super().save(*args, **kwargs)
    

     #the purpose of this function is to show profile by name instead of profile id
    def __str__(self) -> str:

        return self.name
