# Usa la imagen oficial de Python 3.11.9 slim
FROM python:3.11.9-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables de entorno (opcional, puedes manejar en Render)
# ENV TELEGRAM_BOT_TOKEN=tu_token_aqui
# ENV OPENAI_API_KEY=tu_openai_key_aqui

# Comando para ejecutar el bot
CMD ["python", "main.py"]
