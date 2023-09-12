from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import profile



#now we will create our custom exception

def raise_exception(email):
    #we use lower so if some try to insert hotmail in caps it will show in correct

    if email.split("@")[1].split(".")[0].lower()=="hotmail" and email.split(".")[1]== "com":
        raise ValidationError("the email is incorrect")
   
    #return ValidationError("the email is incorrect")






class Profileform(forms.Form):
    name = forms.CharField()
    #we use the email validaton provided by django so if we get any inaccurate email form will automatically raise error
    email = forms.CharField(validators=[EmailValidator,raise_exception])
    contact_num = forms.IntegerField()
    verify_email= forms.CharField(validators=[EmailValidator,raise_exception])
    message = forms.CharField(widget=forms.Textarea)
   
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        cleaned_data["email"] = cleaned_data.get("email").lower()
        contact_num = cleaned_data.get("contact_num")
        message = cleaned_data.get("message")
        cleaned_data["verify_email"]= cleaned_data.get("verify_email").lower()

        if cleaned_data.get("email")!= cleaned_data.get("verify_email"):
            raise ValidationError("Email not match")
        return (cleaned_data)
    
class NewProfile(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
        
        #exclude = ["name"]

