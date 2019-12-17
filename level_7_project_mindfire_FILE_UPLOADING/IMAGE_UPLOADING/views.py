from django.shortcuts import render
from IMAGE_UPLOADING.models import ImageUploadModel
from IMAGE_UPLOADING import forms

# Create your views here.
def  message(request):
    return render(request,'IMAGE_UPLOADING/message.html')

def saveProfile(request):
    imageForm=forms.ImageUploadForm()
    print(request.method)
    print(imageForm)
    if request.method == "POST":
        print("HI")
        imageForm=forms.ImageUploadForm(request.POST,request.FILES)

        if imageForm.is_valid():
            print("HELLO")
            #imageModel=ImageUploadModel()
            #imageModel.name=imageForm.cleaned_data["name"]
            #imageModel.image=imageForm.cleaned_data["image"]
            #imageModel.save()
            imageForm.save()
            saved=True
            return message(request)


    return render(request,'IMAGE_UPLOADING/image_upload.html',{'form':imageForm})
