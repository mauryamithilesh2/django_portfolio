from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage   # it is for pdf download which save in statuic folder
from .forms import ClientForm
def home_view(request):
    certificates=[
        {
         "title":"Summer_Internship",
          'path':'images/summerintern.png',
          },
        {
          "title":"Personal And Profesional Development",
          "path":"images/aspirem1.png",
         },
        {
        "title":"Figma_wireFraming",
         "path":"images/figma.png"
        },
        {
        "title":"Django FullStack development",
         "path":"images/fullstack.jpg"
        },
        {
        "title":"Microsoft Excell",
         "path":"images/excell2019.png"
        },
        {
        "title":"Geo-Data sharing and CyberSecurity",
         "path":"images/isrocyber.png"
        },
        {
        "title":"Basic cloud computing(Udemy)",
         "path":"images/cloud.jpg"
        }
        ]
    # form attributes import from models
    form=ClientForm

# for access project 
    project_list=[{"title":"DriveMart",
         "path":"images/drivemart.png",},{
         "title":"TempTeller",
         "path":"images/tempteller.png",},
         {"title":"Crudify",
         "path":"images/",},{
         "title":"Portfolio",
         "path":"images/portfolio.png",}]
    
    experiences=[{"Company":"SoftPro India,Lucknow","position":"Intern as Both client and server side"},{"Company":"","position":""},{"Company":"","position":""},{ "Company":"","position":""}]
    return render(request,'home.html',{"certificates":certificates,'form':form,"project_list":project_list,"experiences":experiences})












def resume_view(request):
    resume_path="resumefolder/Resume_N.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response = HttpResponse(resume_file.read(),content_type="application/pdf")
            response['content-Disposition']='attachment';filename="Resume_N.pdf"
            return response
    else:
        return HttpResponse("Not available")    
    





