from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from. forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51O6tADDxkJiNr58k4TCIGwe2zf8s3uN34HI67CQjSSLbIsJ5zcQpsDOyLFBmOIeD1vqGHkNYTbasO7WfHdHyzSrl00kjdX0Zqg',
        'client_secret': 'CLIENT_SECRET',
    }

    return render(request, template, context)
