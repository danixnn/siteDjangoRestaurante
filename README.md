# Site de um Restaurante usando o Django Framework
## Este site foi desenvolvido com foco no aprendizado do Django Framework, principalmente para o backend. Foi utilizado o template Savory, baixado no site [FreeHtml5](https://freehtml5.co/preview/?item=savory-free-website-template-for-restaurants-websites), e modificado de acordo com as necessidades do desenvolvedor.
## 🛠️ Construído com

O projeto utilizou duas principais ferramentas Python, o framework Django e o banco de dados PostgreSQL. O template Savory também foi empregado.

* [Django](https://www.djangoproject.com/) - O framework web usado
* [PosrgreSQL](https://www.postgresql.org/) - O banco de dados usado
* [Savory](https://freehtml5.co/preview/?item=savory-free-website-template-for-restaurants-websites) - Template usado

### 📋 Pré Requisitos
Foram utilizadas as seguintes versões: Python 3.13.5, Django 5.2.4 e PostgreSQL 17.5.

Para o funcionamento você deve ter as seguintes blibliotecas instaladas em seu ambiente:
* asgiref==3.9.1
* DateTime==5.5
* dj-static==0.0.6
* Django==5.2.4
* django-stdimage==6.0.2
* gunicorn==23.0.0
* packaging==25.0
* pillow==11.3.0
* psycopg2-binary==2.9.10
* pytz==2025.2
* setuptools==80.9.0
* sqlparse==0.5.3
* static3==0.7.0
* tzdata==2025.2
* zope.interface==7.2
* asgiref==3.9.1
* DateTime==5.5
* dj-static==0.0.6
* Django==5.2.4
* django-stdimage==6.0.2
* gunicorn==23.0.0
* packaging==25.0
* pillow==11.3.0
* psycopg2-binary==2.9.10
* pytz==2025.2
* setuptools==80.9.0
* sqlparse==0.5.3
* static3==0.7.0
* tzdata==2025.2
* zope.interface==7.2

## ⚙️ Como executar

Verifique se todos os requisitos estão instalados. No arquivo `settings.py`, certifique-se de que o `DEBUG` está como `True` e verifique as configurações do banco de dados (nome de usuário, senha, etc.).

Após a verificação, você pode executar o seguinte comando, que fará o Django iniciar um servidor local para testes:
```
python manage.py runserver
```
Coloque o IP gerado em algum navegador e será possivel observar o site em modo de teste.

## 📰 Explicando um pouco das telas e o que foi feito
* Index

Foram recuperados os dados do banco e apresentados na tela 3 pratos populares, 3 serviços, fatos curiosos(o numero de pratos) e na subscrição o usuario pode informar seu email e enviar onde será salvo no banco.

* Menu

Foram recuperados todos os pratos e apresentados nessa pagina.

* Serviços

Foram recuperados todos os serviços e apresentados nessa pagina.

* Contato

Foi feito um formulario para pegar dados do usuario atraves de um post.

* Reservas

Formulario para usuario reservar uma mesa no Restaurante.

* AcessoAdm

Página feita onde um usuario administrador tem a opção de baixar um `.csv` com a lista de emails subscritos e ver as reservas podendo `editar` ou `deletar` quando necessario.

* Django Admin

No Django Admin que já vem padrão, é possivel criar, editar e excluir dados de todos os modelos!

## 🎥 Confira o video

[Projeto Funcionado](https://www.youtube.com/watch?v=o-tWaSky4vk)
