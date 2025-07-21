from django import forms
from django.core.mail.message import EmailMessage
from .models import Reserva
from datetime import datetime

class SubForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'{nome}\n{email}\n{mensagem}'

        mail = EmailMessage(
            subject=f'Mensagem do Restaurante de {nome}',
            body=conteudo,
            from_email=email,
            to=['teste@gmail.com', ],
            headers={'Reply-To': email}
        )
        mail.send()

class ReservaForm(forms.ModelForm):

    CHOICES_PESSOAS = [
        ('', 'Pessoas'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5+')
    ]

    nome = forms.CharField(label='Nome', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=14)
    pessoas = forms.ChoiceField(label='Pessoas',choices=CHOICES_PESSOAS,required=True)
    date = forms.DateField(label='Data', input_formats=['%d/%m/%Y'])
    time = forms.TimeField(label='Horas', input_formats=['%I:%M %p'])

    def clean(self):
        cleaned_data = super().clean()

        rdata = cleaned_data.get('date')
        rhora = cleaned_data.get('time')

        now = datetime.now()

        if rdata and rhora:
            res = datetime.combine(rdata, rhora)

            if res <= now:
                raise forms.ValidationError(
                    'Data ou horario invalidos'
                )

        return cleaned_data

    class Meta:
        model = Reserva
        fields = ['nome', 'telefone', 'pessoas', 'date', 'time']
