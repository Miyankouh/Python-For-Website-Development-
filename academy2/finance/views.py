from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from finance.forms import ChargeWalletForm
from finance.utils.zarinpal import zpal_payment_checker, zpal_request_handler


class ChargeWalletView(View):
    form_class = ChargeWalletForm
    template_name = 'finance/charge_wallet.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            payment_link, authority = zpal_request_handler(
                settings.ZARRINPAL['merchant_id'], form.cleaned_data['amount'],
                "Wallet charge", 'test@gmail.com', None, settings.ZARRINPAL['gateway_callback_url'] 
            )
            if payment_link is not None:
                return redirect(payment_link) 

        return render(request, self.template_name, {'form': form})


class VerifyView(View):
    template_name = 'finance/callback.html'

    def get(self,request, *args, **kwargs):
        authority = request.GET.get('Authority')
        is_paid, ref_id = zpal_payment_checker(
            settings.ZARRINPAL['merchant_id'],
            1000, # amount
            authority
        )
        return render(request, self.template_name, {'is_paid': is_paid, 'ref_id': ref_id})