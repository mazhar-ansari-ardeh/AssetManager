from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import Asset
from .forms import AssetForm


def allAssets(request):
    global user
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = User.objects.get(pk=user_id)
    assets = Asset.objects.filter(owner=user)  # Retrieve assets belonging to the current user
    return render(request, "assets/assets.html", {"assets": assets})


def detail(request, id):
    asset = get_object_or_404(Asset, pk=id)
    return render(request, "assets/detail.html", {"asset": asset})


# AssetForm = modelform_factory(Asset, exclude=[])


def new(request):
    global user

    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user_id')
            if user_id is not None:
                user = User.objects.get(pk=user_id)
            asset = form.save(commit=False)
            asset.owner = user
            asset.save()
            return redirect("assets")
    else:
        form = AssetForm()
    return render(request, "assets/new.html", {"form": form})
