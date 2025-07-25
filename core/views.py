from django.views.generic import TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib import messages

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Menu, Servicos, Sub, Reserva
from .forms import SubForm, ContatoForm, ReservaForm

from django.views.generic.edit import DeleteView, UpdateView
import csv


class IndexView(FormView):
    template_name = 'index.html'
    form_class = SubForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.order_by('?')
        context['servicos'] = Servicos.objects.order_by('?')
        context['n_pratos'] = Menu.objects.count()

        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if not Sub.objects.filter(email=email).exists():
            Sub.objects.create(email=email)
            messages.success(self.request, 'Email inscrito com sucesso!')
            return super().form_valid(form)
        else:
            messages.info(self.request, 'O email já está subscrito!')
            return self.render_to_response(self.get_context_data(form=form))


    def form_invalid(self, form):
        messages.error(self.request, 'Erro no email!')
        return super().form_invalid(form)

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.all()

        return context

class ServicoView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicoView, self).get_context_data(**kwargs)
        context['servicos'] = Servicos.objects.all()

        return context

class ContatoView(FormView):
    template_name = 'contact.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(ContatoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar mensagem!')
        return super(ContatoView, self).form_invalid(form)

class ReservaView(FormView):
    template_name = 'reserva.html'
    form_class = ReservaForm
    success_url = reverse_lazy('reserva')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        telefone = form.cleaned_data['telefone']
        pessoas = form.cleaned_data['pessoas']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']

        print('------------------------------------')
        print(nome, telefone, pessoas, date, time)
        print('------------------------------------')

        form.save()

        messages.success(self.request, 'Reserva enviada, aguarde ligação!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ocorreu algum erro! Verifique os campos!')
        return super().form_invalid(form)

class AcessoAdmView(TemplateView):
    template_name = 'acessoadm.html'

    def get_context_data(self, **kwargs):
        context = super(AcessoAdmView, self).get_context_data(**kwargs)
        context['reserva'] = Reserva.objects.all().order_by('date', 'time')

        return context


class DownloadEmailsView(View, LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = "lista_emails.csv"'

        writer = csv.writer(response)

        writer.writerow(['ID','Email'])

        emails = Sub.objects.all().order_by('id')

        for email in emails:
            writer.writerow([
                email.id,
                email.email
            ])

        return response

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('acessoadm')
    template_name = 'confirmar_exclusao.html'

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ['pessoas','date', 'time']
    success_url = reverse_lazy('acessoadm')
    template_name = 'confirmar_edicao.html'