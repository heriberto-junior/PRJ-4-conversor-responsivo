# Usar imagem Python slim (pequena)
FROM python:3.11-slim

# Instalar COBOL
RUN apt-get update && apt-get install -y \
    gnucobol \
    libcob4 \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY coin.cob .
COPY cotacao.txt .
COPY app.py .
COPY requirements.txt .

# Compilar COBOL
RUN cobc -x -free -static -o coin coin.cob

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Definir variáveis de ambiente
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Comando para iniciar
CMD exec python3 -m flask --app app run --host=0.0.0.0 --port=$PORT
