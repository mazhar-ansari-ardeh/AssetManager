from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewStockForm, EditStockForm
from .models import Category, Stock


def stocks(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    stocks = Stock.objects.all()

    if category_id:
        stocks = stocks.filter(category_id=category_id)

    if query:
        stocks = stocks.filter(Q(name__icontains=query) | Q(ticker__icontains=query))

    return render(request, 'stock/stocks.html', {
        'stocks': stocks,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def ticker(request, ticker):
    stocks = Stock.objects.filter(Q(created_by=request.user) & Q(ticker=ticker))

    return render(request, 'stock/ticker.html', {
        'stocks': stocks,
    })


def detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'stock/detail.html', {
        'stock': stock,
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewStockForm(request.POST, request.FILES)

        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_by = request.user
            stock.save()

            return redirect('stock:detail', pk=stock.id)
    else:
        form = NewStockForm()

    return render(request, 'stock/form.html', {
        'form': form,
        'title': 'New stock',
    })


@login_required
def edit(request, pk):
    stock = get_object_or_404(Stock, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditStockForm(request.POST, request.FILES, instance=stock)

        if form.is_valid():
            form.save()

            return redirect('stock:detail', pk=stock.id)
    else:
        form = EditStockForm(instance=stock)

    return render(request, 'stock/form.html', {
        'form': form,
        'title': 'Edit stock',
    })


@login_required
def delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk, created_by=request.user)
    stock.delete()

    return redirect('dashboard:index')
