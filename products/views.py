from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def payment(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    order_qs = order.objects.filter (user= request.user, ordered=False)
    order_total = order_qs[0].get_totals()
    totalcents = float(order_total * 100);
    total = round(totalcents, 2)
    if request.method ==  'POST':
        charge = stripe.Charge.create(amount=total,
            currency='inr',
            description=order_qs,
            source=request.POST['stripeToken'])
        print(charge)
    return render(request, 'checkout/payment.html', {"key": key, "total": total})