from django.shortcuts import render, redirect
from .context_data import get_common_context, get_page_context


def handle_post_request(request):
    pass
    # make_appointment = MakeAppointmentForm(request.POST)
    # contact_us = ContactUsForm(request.POST)
    # subscription = SubscriptionForm(request.POST)
    #
    # if make_appointment.is_valid():
    #     make_appointment.save()
    #     return redirect('/')
    # if contact_us.is_valid():
    #     contact_us.save()
    #     return redirect('/')
    # if subscription.is_valid():
    #     subscription.save()
    #     return redirect('/')


def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'index.html', context=data)

def about(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'about.html', context=data)

def menu(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'menu.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'contact.html', context=data)