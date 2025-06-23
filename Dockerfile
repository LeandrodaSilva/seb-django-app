# Use the official Python runtime image
FROM python:3.13

# Cria o diretório do app
RUN mkdir /app

# Define o diretório de trabalho
WORKDIR /app

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o requirements.txt (se existir) e instala dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . /app/

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
