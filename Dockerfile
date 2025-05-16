# Usa uma imagem leve com Python
FROM python:3.13-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para dentro da imagem
COPY . .

# Instala dependências do sistema (ex: para build do psycopg2, etc)
RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install --no-cache-dir -r requirements.txt

# Expõe a porta da aplicação
EXPOSE 5000

# Define a variável de ambiente para evitar buffering
ENV PYTHONUNBUFFERED=1

# Executa o servidor Flask
CMD ["python", "run.py"]
