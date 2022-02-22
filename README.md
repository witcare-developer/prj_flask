# Prj Flask

## Para instalar dependencias
1 - pip install -r requirements.txt

## Configuração de Variáveis de ambiente 
1 - export FLASK_APP=app : Fazer isso no diretório onde está o app.py
2 - a partir disso digitar flask shell para ter acesso a comandos relativos a aplicação.
2 - Criar o database : flask shell-> from app import db -> db.create_all()