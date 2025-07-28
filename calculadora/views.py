from django.shortcuts           import render, redirect
from django.contrib.auth        import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views  import LogoutView
from .forms                     import RegistroForm
from .models                    import Operacao

def login_view(request):
    msg = ''
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('calculos')
        msg = 'Usuário ou senha inválidos'
    return render(request, 'calculadora/login.html', {'mensagem': msg})

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            return redirect('calculos')
    else:
        form = RegistroForm()
    return render(request, 'calculadora/registrar.html', {'form': form})

@login_required(login_url='login')
def calculos(request):
    expressao = request.POST.get('expressao', '')
    resultado = ''

    if request.method == 'POST':
        expr_py = (expressao
                   .replace('×', '*')
                   .replace('÷', '/')
                   .replace('−', '-'))
        try:
            resultado = str(eval(expr_py))
        except:
            resultado = 'Erro'
        Operacao.objects.create(
            usuario=request.user,
            expressao=expressao,
            resultado=resultado
)


    historico = Operacao.objects.filter(usuario=request.user) \
                            .order_by('-data_hora')[:10]


    operacoes = ['C', '÷', '×', '-', '+', '=']   # aqui o '-' é ASCII

    linhas_numeros = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        ['0','.',''],
    ]

    return render(request, 'calculadora/calculos.html', {
        'expressao':      expressao,
        'resultado':      resultado,
        'historico':      historico,
        'operacoes':      operacoes,
        'linhas_numeros': linhas_numeros,
    })