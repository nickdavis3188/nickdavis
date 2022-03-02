import mimetypes
import os
from django.shortcuts import render
from .forms import WorkForm,TestimonialForm,Profilep
from .models  import Profilpic,Works,Testimonials
from django.http.response import HttpResponse
# Create your views here.

# index route
def index(req):
    if req.method == 'GET':
        profile_picture = Profilpic.objects.all()
        work_done = Works.objects.all()
        testimonial = Testimonials.objects.all()
        my_context = {
            'profile_pic':profile_picture,
            'work_done':work_done,
            'testimonial':testimonial
        }
        return render(req,'portfolio/index.html',my_context)

# work route

def work(req):
    if req.method == 'GET':
        my_forms = WorkForm()
        profile = Profilep()
        context_i = {
            'form':my_forms,
            'form2':profile
        }
        return render(req,'portfolio/workUpload.html',context_i)
    else:
        profile = Profilep()
        my_forms = WorkForm(req.POST or None)
        if my_forms.is_valid():
            my_forms.save()
            my_forms = WorkForm()
            context_e = {
                'form':my_forms,
                'form2':profile,
                'msg':'upload successfull',
                'isSuccess':True
            }
            return render(req,'portfolio/workUpload.html',context_e)

# testimonie route
def testimonie(req):
    if req.method == 'GET':
        my_forms = TestimonialForm()
        context_i = {
            'form':my_forms
        }
        return render(req,'portfolio/testimonie.html',context_i)
    else:
        my_forms = TestimonialForm(req.POST or None)
        if my_forms.is_valid():
           testimone =  my_forms.save()
           context_e = {
                'Name':testimone.Full_Name,
                
            }
           return render(req,'portfolio/success.html',context_e)


# profilepic route
def profilePic(req):
     if req.method == 'POST':
        my_profile = Profilep(req.POST or None)

        if my_profile.is_valid():
            exist_data = Profilpic.objects.all()
            print(exist_data)
            if exist_data:
                exist_data.delete()
                my_profile.save()

                my_form = WorkForm()

                my_profile2 = Profilep()

                context_e2 = {
                    'form':my_form,
                    'form2':my_profile2,
                    'msg2':'upload successfull',
                    'isSuccess2':True
                }
                return render(req,'portfolio/workUpload.html',context_e2)
            else:
                my_profile.save()

                my_form2 = WorkForm()

                my_profile3 = Profilep()

                context_e4 = {
                    'form':my_form2,
                    'form2':my_profile3,
                    'msg2':'upload successfull',
                    'isSuccess2':True
                }
                return render(req,'portfolio/workUpload.html',context_e4)

# download cv router
def download_file(req):
    filename="Davis'sResume.pdf"
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = BASE_DIR + '/cv/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
 