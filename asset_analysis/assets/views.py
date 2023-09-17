from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.db.models import Sum, F
from .models import Stock
from .forms import StockForm


def allAssets(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('welcome')
    user = User.objects.get(pk=user_id)
    assets = (Stock.objects.filter(owner=user).values('title').annotate(value=Sum(F('quantity')*F('price'))).order_by())
    print(assets)
    return render(request, "assets/assets.html", {"assets": assets})


def detail(request, id):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('welcome')
    asset = get_object_or_404(Stock, pk=id)
    return render(request, "assets/detail.html", {"asset": asset})

def detailByTitle(request, title):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('welcome')
    stocks = get_list_or_404(Stock, title=title)
    print(stocks)
    return render(request, "assets/detailsByTitle.html", {"stocks": stocks})

# AssetForm = modelform_factory(Asset, exclude=[])


def new(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect('welcome')

    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user_id')
            if user_id is not None:
                user = User.objects.get(pk=user_id)
            asset = form.save(commit=False)
            asset.owner = user
            asset.save()
            return redirect("assets")
    else:
        form = StockForm()
    return render(request, "assets/new.html", {"form": form})
