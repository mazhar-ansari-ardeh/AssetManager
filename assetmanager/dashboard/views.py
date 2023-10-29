from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.shortcuts import render

from stock.models import Stock


@login_required
def index(request):
    stocks = (Stock.objects.filter(created_by=request.user).values('ticker')
              .annotate(value=Sum(F('quantity') * F('purchase_price'))).order_by())

    return render(request, 'dashboard/index.html', {
        'stocks': stocks,
    })
