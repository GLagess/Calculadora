Projeto Calculadora Django

Um portal web de calculadora avançada com autenticação de usuários, armazenamento de histórico de operações e interface responsiva.

Tecnologias

Python 3.13

Django 5.2

SQLite (banco de dados padrão)

HTML5, CSS3 (Flex e Grid Layout)

Funcionalidades

Autenticação de usuários:

Página de login

Página de cadastro (usuário e senha)

Logout

Calculadora com operações básicas:

Adição (+), subtração (-), multiplicação (×) e divisão (÷)

Botão de limpar (C)

Botão de resultado (=)

Histórico de operações:

Armazena expressão, resultado e data/hora no banco

Exibe os 10 cálculos mais recentes do usuário

Perfil por usuário:

Cada usuário vê apenas seu próprio histórico

Estrutura de Pastas

projeto_calculadora/       # Raiz do projeto
├── calculadora/           # Aplicativo Django
│   ├── forms.py           # Formulário customizado de registro
│   ├── models.py          # Modelo Operacao (FK para User)
│   ├── views.py           # Lógica de login, registro e calculadora
│   ├── urls.py            # Rotas do app
│   ├── templates/         # Templates HTML
│   │   └── calculadora/
│   │       ├── login.html
│   │       ├── registrar.html
│   │       └── calculos.html
│   └── static/            # Arquivos estáticos
│       └── calculadora/
│           └── css/
│               └── calculos.css
├── projeto_calculadora/    # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── manage.py              # CLI do Django
└── venv/                  # Ambiente virtual

Instalação e Execução

Clonar o repositório

git clone  https://github.com/GLagess/Calculadora.git
cd projeto_calculadora

Criar e ativar ambiente virtual

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Instalar dependências

pip install --upgrade pip
pip install django

Configurar banco e criar superusuário

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Executar o servidor de desenvolvimento

python manage.py runserver

Acessar no navegador

Login: http://127.0.0.1:8000/

Cadastro: http://127.0.0.1:8000/registrar/

Calculadora (após login): http://127.0.0.1:8000/calculadora/

Admin: http://127.0.0.1:8000/admin/

