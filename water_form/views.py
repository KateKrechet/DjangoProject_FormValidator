from django.shortcuts import render
from django.shortcuts import redirect
from water_form.form_list import *


# Create your views here.
def index(req):
    return render(req, 'index.html')


def forma(req):
    if req.POST:
        # показываем, что не заполнено, если нажали отправить, а форма не заполнена
        anketa = Water(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['surname']
            k3 = anketa.cleaned_data['mail']
            k4 = anketa.cleaned_data['tel']
            k5 = anketa.cleaned_data['adr']
            k6 = anketa.cleaned_data['time']
            k7 = anketa.cleaned_data['volume']
            print(k1, k2, k3, k4, k5, k6, k7)
            info = {'k1': k1, 'k2': k2, 'k3': k3, 'k4': k4, 'k5': k5, 'k6': k6,
                    'k7': k7}

            return render(req, 'info.html', context=info)
        else:
            print('neok')

    else:
        anketa = Water()
    data = {'form': anketa}
    return render(req, "order_water.html", context=data)


def order(req):
    return render(req, 'info.html')
