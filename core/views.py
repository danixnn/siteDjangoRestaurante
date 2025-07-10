from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Menu, Servicos, Sub
from .forms import SubForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = SubForm
    success_url = reverse_lazy('index.html')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.order_by('?')
        context['servicos'] = Servicos.objects.all()

        return context

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            if not Sub.objects.filter(email=email).exists():
                Sub.objects.create(email=email)
                messages.success(self.request, 'Email criado com sucesso!')
                return self.form_valid(form)
            else:
                messages.info(self.request, 'O email já está subscrito!')
                return self.render_to_response(self.get_context_data(form=form))
        except:
            messages.error(self.request, 'Ocorreu um erro!')
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro no email!')
        return super().form_invalid(form)

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['menu'] = Menu.objects.all()

        return context