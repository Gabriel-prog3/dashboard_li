from django.shortcuts import render
from .models import Clima, Consumo, Generacion
from .utils import get_plot

# Create your views here.


def index(request):

    qs = Clima.objects.all()
    x = [x.id for x in qs]
    y = [y.temp for y in qs]
    chart = [get_plot(x, y, y, "temperatura (°C)")]
    y = [y.rad for y in qs]
    chart.append(get_plot(x, y, y, "Radiación (w/m2)"))
    qs = Consumo.objects.all()
    y = [(x.p1 + x.p2 + x.p3 + x.p4 + x.p5 + x.p6 + x.p7 + x.p8) / 8 for x in qs]
    qs = Generacion.objects.all()
    y2 = [y.p_inv for y in qs]
    chart.append(
        get_plot(
            x,
            y,
            y2,
            "generacion-uso",
            size=(13, 3),
            label_1="Generación",
            label_2="Demanda",
        )
    )
    max_p_inv = max(y2)
    return render(
        request,
        "main.html",
        {
            "chart": chart[0],
            "chart1": chart[1],
            "chart2": chart[2],
            "max_p_inv": max_p_inv,
        },
    )
