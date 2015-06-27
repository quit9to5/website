from django.shortcuts import render, render_to_response, RequestContext,  HttpResponseRedirect
from django.contrib import messages
from .models import information
from .forms import ContactForm, SignupForm
# Create your views here.

def index(request):

    form = SignupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for Making a request, we will get back to you soon')


    return render_to_response("our_form/form.html",locals(),context_instance=RequestContext(request))


def aboutus(request):

    return render_to_response("our_form/aboutus.html",locals(),context_instance=RequestContext(request))

def contact(request):
    title = 'Contact US'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = setting.EMAIL_HOST_USER
        to_email = [from_email, 'vivacity.legend@gmail.com']
        contact_message = "%s: %s via %s"%(
                form_full_name,
                form_message,
                form_email)
        some_html_message = """
        <h1>Hello world from ourdhobi.com</h1>
        """
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                html_message=some_html_message,
                fail_silently=True)
    context = {
    "form": form,
    "title": title,
    }
    return render(request, "our_form/contact.html", context)
