from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Testimonials, Works,Profilpic
from django.core.exceptions import ValidationError

class WorkForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['img_string','title','tag','poper','project_link','description']
        widgets = {
            'img_string': forms.TextInput(attrs={'class': 'h-full-width imgsting','id':'sampleInput','placeholder':'pls choose an image to get the img_string...'}),
            'title': forms.TextInput(attrs={'class': 'h-full-width','placeholder':'title','id':'sampleInput'}),
            'tag':forms.TextInput(attrs={'class': 'h-full-width','placeholder':'tag','id':'sampleInput'}),
            'poper':forms.TextInput(attrs={'class': 'h-full-width','placeholder':'#model1 or 2...','id':'sampleInput'}),
             'project_link':forms.TextInput(attrs={'class': 'h-full-width','placeholder':'https://www.worklink.com','id':'sampleInput'}),
            'description':forms.Textarea(attrs={'class': 'h-full-width','placeholder':'description','id':'exampleMessage'})
        }
        
        def validatea(self):
            link =  self.cleaned_data.get('project_link')
            if not 'http' in link:
                raise ValidationError('The link must start with http')
            return link

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['img_string','Full_Name','Job_Title','Comments']
        widgets = {
            'img_string':forms.TextInput(attrs={'class': 'h-full-width imgsting','id':'sampleInput','placeholder':'pls choose an image to get the img_string...'}),
            'Full_Name':forms.TextInput(attrs={'class': 'h-full-width','placeholder':'john doe','id':'sampleInput'}),
            'Job_Title':forms.TextInput(attrs={'class': 'h-full-width','placeholder':'e.g CEO,Google','id':'sampleInput'}),
            'Comments':forms.Textarea(attrs={'class': 'h-full-width','placeholder':'comment','id':'exampleMessage'})
        }
        # def validatea(self):
        #     img =  self.cleaned_data.get('img_string')
        #     if img == '':
        #         raise ValidationError('pls choose an image to get the img_string value')

class Profilep(forms.ModelForm):
    class Meta:
        model = Profilpic
        fields = ['img_string']
        widgets = {'img_string':forms.TextInput(attrs={'class': 'h-full-width imgsting2','id':'sampleInput','placeholder':'pls choose an image to get the img_string...'}),}