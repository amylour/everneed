from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def error_view(request):
    """ 500 Internal Server Error """
    return render(request, "500.html")
