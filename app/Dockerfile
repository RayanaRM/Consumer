# Use a imagem base Python
FROM python:3.8

# Copie o código fonte da aplicação para o diretório /app no container
COPY . /app

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale as dependências da aplicação
RUN pip install -r requirements.txt
 
# Exponha a porta em que a aplicação vai rodar
EXPOSE 80

# Comando para iniciar a aplicação quando o container for iniciado
CMD ["python", "app.py"]
