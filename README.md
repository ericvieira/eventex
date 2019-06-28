# Eventex

Sistema de Eventos encomendados pela Morena

[![Build Status](https://travis-ci.org/ericvieira/eventex.svg?branch=master)](https://travis-ci.org/ericvieira/eventex)


## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.


``` console 
git clone git@github.com:ericvieira/wttd.git wttd 
cd wttd
python -m venv .wttd
source .wttd/bin/activate 
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instancia no heriku
2. envie as conf para o heroku
3. Defina uma SECRET_KEY segura para instancia
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o codigo para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force

```