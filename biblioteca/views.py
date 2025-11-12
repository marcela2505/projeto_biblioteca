from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Emprestimo
from .forms import LivroForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import Random

def home(request):
    # Total de livros cadastrados
    total_livros = Livro.objects.count()

    # Livros emprestados (ainda não devolvidos)
    total_emprestimos = Emprestimo.objects.filter(data_devolucao__isnull=True).count()

    # Usuários cadastrados
    total_usuarios = User.objects.count()

    # Livros adicionados no mês atual
    hoje = date.today()
    livros_mes = Livro.objects.filter(
        data_cadastro__year=hoje.year,
        data_cadastro__month=hoje.month
    ).count()

    # Livros em destaque (3 livros aleatórios)
    livros_destaque = Livro.objects.order_by(Random())[:3]

    return render(request, "biblioteca/home.html", {
        "total_livros": total_livros,
        "total_emprestimos": total_emprestimos,
        "total_usuarios": total_usuarios,
        "livros_mes": livros_mes,
        "livros_destaque": livros_destaque,
    })

def lista_livros(request):
    query = request.GET.get('q')
    if query:
        livros = Livro.objects.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    else:
        livros = Livro.objects.all()
    return render(request, 'biblioteca/lista_livros.html', {'livros': livros, 'query': query})


# ✅ Somente administradores podem acessar/adicionar livros
@login_required(login_url="/contas/login/")
def adicionar_livro(request):
    if not request.user.is_staff:
        messages.warning(request, "⚠️ Você não tem permissão para cadastrar livros.")
        return redirect("home")

    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "📚 Livro cadastrado com sucesso!")
            return redirect("lista_livros")
    else:
        form = LivroForm()

    return render(request, "biblioteca/adicionar_livro.html", {"form": form})


# ✅ Qualquer usuário logado pode registrar um empréstimo
@login_required(login_url="/contas/login/")
def emprestimos(request):
    if request.method == "POST":
        livro_id = request.POST.get("livro")
        if livro_id:
            livro = Livro.objects.filter(id=livro_id, disponivel=True).first()
            if livro:
                # o nome do usuário logado é adicionado automaticamente
                Emprestimo.objects.create(livro=livro, nome_usuario=request.user.username)
                livro.disponivel = False
                livro.save()
                messages.success(request, f"📖 Empréstimo registrado por {request.user.username}.")
                return redirect("emprestimos")
            else:
                messages.error(request, "❌ Livro inválido ou já emprestado.")
    livros = Livro.objects.filter(disponivel=True)
    emprestimos = Emprestimo.objects.select_related("livro").all().order_by("-data_emprestimo")
    return render(request, "biblioteca/emprestimos.html", {"livros": livros, "emprestimos": emprestimos})


# ✅ Registro de novos usuários (sem atribuir usuário logado)
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Conta criada com sucesso! Faça login para continuar.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "biblioteca/registro.html", {"form": form})

@login_required
def devolver(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if request.method == 'POST':
        # marca data de devolução
        if not emprestimo.data_devolucao:
            emprestimo.data_devolucao = date.today()
            emprestimo.save()

            # atualiza disponibilidade do livro
            livro = emprestimo.livro
            livro.disponivel = True
            livro.save()

            messages.success(request, f'Livro "{livro.titulo}" devolvido com sucesso.')
        else:
            messages.info(request, 'Este empréstimo já foi devolvido.')

    return redirect('emprestimos')
