from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import ClassePersonagem, Jogador, Inimigo, Item
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'pages/inicio.html')

@login_required
def escolha_classe(request):
    classes = ClassePersonagem.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        classe_id = request.POST.get('classe_id')
        classe_escolhida = ClassePersonagem.objects.get(id=classe_id)

        jogador, created = Jogador.objects.get_or_create(user=request.user)
        jogador.nome = nome
        jogador.classe = classe_escolhida
        jogador.save()

        return redirect('inicio')  # Redireciona para a página inicial ou qualquer outra página relevante

    return render(request, 'pages/escolha_classe.html', {'classes': classes})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('escolha_classe')  # substitua 'inicio' pelo nome da URL para onde você quer redirecionar após o registro
    else:
        form = SignUpForm()
    return render(request, 'pages/signup.html', {'form': form})
    
def personagem(request, classe_id):
    classe = ClassePersonagem.objects.get(id=classe_id)
    return render(request, 'pages/tela_personagem.html', {'classe': classe})
# def escolha_classe(request):
#     classes = Jogador.objects.all()
#     if request.method == 'POST':
#         classe_id = request.POST.get('classe_id')
#         classe_escolhida = Jogador.objects.get(id=classe_id)
#         # Aqui você pode associar a classe escolhida ao jogador
#         # jogador.classe = classe_escolhida
#         # jogador.save()
#         return redirect('inicio')  # Redireciona para uma página de sucesso ou outra página relevante
    
    # return render(request, 'pages/escolha_classe.html', {'classes': classes})



# def criar_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('alguma_url_de_sucesso')
#     else:
#         form = ItemForm()
#     return render(request, 'seu_template.html', {'form': form})

