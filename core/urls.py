from django.urls import path

from .views import IndexView, MenuView, ServicoView, ContatoView, ReservaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('servicos/', ServicoView.as_view(), name='servicos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('reserva/', ReservaView.as_view(), name='reserva'),
]