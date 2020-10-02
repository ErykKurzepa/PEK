from django.shortcuts import render
from Contact import forms


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
            info = '<div class="alert alert-dark" role="alert">Thanks for reaching out to me! I will answer asap!</div>'
        else:
            info = '<div class="alert alert-dark" role="alert">Something was wrong in your request, email was not send!</div>'
        form = forms.ContactForm()
        return render(request, 'Contact/index.html', {'form': form, 'info': info})
    else:
        form = forms.ContactForm()
        return render(request, 'Contact/index.html',{'form': form})


