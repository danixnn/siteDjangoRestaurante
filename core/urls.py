from django.urls import path

from .views import IndexView, MenuView, ServicoView, ContatoView, ReservaView, AcessoAdmView, DownloadEmailsView, DownloadReservasView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('servicos/', ServicoView.as_view(), name='servicos'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('reserva/', ReservaView.as_view(), name='reserva'),
    path('acessoadm/', AcessoAdmView.as_view(), name='acessoadm'),
    path('download/emails', DownloadEmailsView.as_view(), name='download_emails'),
    path('download/reservas', DownloadReservasView.as_view(), name='download_reservas'),
]