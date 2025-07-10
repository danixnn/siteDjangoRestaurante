from django.db import models
import uuid
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.
class Base(models.Model):
    criados = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Menu(Base):
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 800, 'height': 600, 'crop': True}})
    prato = models.CharField('Nome do Prato', max_length=80)
    descricao = models.CharField('Descrição do Prato', max_length=200)
    valor = models.DecimalField('Valor do produto', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.prato

class Servicos(Base):
    ICONES_CHOICES = (
        ('ti-face-smile', 'Smile'),
        ('ti-thought', 'Nuvem'),
        ('ti-truck','Caminhão'),
    )
    icone = models.CharField('Icone', max_length=15, choices=ICONES_CHOICES)
    servico = models.CharField('Serviço', max_length=80)
    descricao = models.CharField('Descrição Serviço', max_length=200)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Reserva(Base):
    nome = models.CharField('Nome', max_length=80)
    telefone = models.CharField('Telefone', max_length=20)
    pessoas = models.IntegerField('Quantidade de Pessoas')
    date = models.DateField('Data da reserva')
    time = models.TimeField('Hora da reserva')
    Base.ativo = False

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Nome {self.nome} Telefone {self.telefone} Quantidade {self.pessoas} Data {self.date} Horario {self.time}'

class Sub(Base):
    email = models.EmailField('Email do sub')

    class Meta:
        verbose_name = 'Sub'
        verbose_name_plural = 'Subs'

    def __str__(self):
        return self.email
