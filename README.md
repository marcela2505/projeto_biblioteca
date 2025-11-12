# 📚 Biblioteca Virtual

Uma aplicação web desenvolvida em **Django** para gerenciamento de livros, usuários e empréstimos.  
Permite cadastrar livros, registrar empréstimos e devoluções, além de visualizar estatísticas e livros em destaque.

---

## 🚀 Funcionalidades

- 📖 **Cadastro de livros** (apenas administradores)
- 👥 **Cadastro de usuários**
- 🔐 **Login e autenticação**
- 📚 **Empréstimo e devolução de livros**
- 📊 **Página inicial com estatísticas**
  - Total de livros
  - Livros emprestados
  - Usuários cadastrados
  - Livros adicionados no mês atual
- 🌟 **Livros em destaque** (3 exibidos aleatoriamente na página inicial)

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/) (banco padrão do Django)
- HTML5, CSS3 e [Lucide Icons](https://lucide.dev/)

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
# ou
source venv/bin/activate  # (Linux/Mac)
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor
```bash
python manage.py runserver
```
Depois acesse:
👉 http://127.0.0.1:8000/

---

## 🧾 Observações
- Para cadastrar livros e gerenciar empréstimos, é necessário estar logado.
- Apenas usuários administradores podem adicionar novos livros.
- As estatísticas da página inicial são atualizadas automaticamente conforme o uso.

---

## 📷 Exemplo da Página Inicial
<img width="1353" height="636" alt="image" src="https://github.com/user-attachments/assets/591ea46f-b219-4978-a4b7-5a6f8220ed3f" />

---

## 📄 Licença
Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.
