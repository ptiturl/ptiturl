from django.shortcuts import render, redirect

# Create your views here.

from .models import Url
def urlRedirect(request, slugs):
    try:
        data = Url.objects.get(uri=slugs)
    except Exception:
        return redirect(f"/error/u/{slugs}")
    else:
        if data.is_enable:
            return redirect(data.url)
        else:
            return redirect(f"/error/d/{slugs}")
