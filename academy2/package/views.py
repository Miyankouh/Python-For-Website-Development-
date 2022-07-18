from django.shortcuts import render
from django.views import View

from package.models import Package
# Create your views here.

class PricingView(View):

    def get_context_data(self):
        packages = Package.objects.filter(is_enable=True)
        return dict(packages=packages)
    

    def get(self, request, *args, **kwargs):
        return render(request, 'package/pricing_page.html', self.get_context_data())