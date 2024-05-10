import tweepy
import schedule
import time
import random
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger()

# Chaves de acesso
consumer_key = 'UBSbRAcjl4zYV84uUSbE4gbP6'
consumer_secret = 'rQE9sF0cjKhbJOwvytz5Dl1STIKn3kYijnKsrqaLubWRFYaytv'
access_token = '1788786763428720640-UmlUZujy3oDuNDgXLwqUamLjxNMZmt'
access_token_secret = 'oWWNO9WKuw1uh9lqwDEy8XDOn19CMC9U78rQrcWu73iKr'

# Autenticação
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Lista de estilos de arte
art_styles = [
    "Realismo",
    "Impressionismo",
    "Cubismo",
    "Surrealismo",
    "Abstracionismo",
    "Expressionismo",
    "Pop Art",
    "Arte Renascentista",
    "Arte Barroca",
    "Arte Contemporânea"
]

# Função para postar sobre um estilo de arte aleatório
def post_art_styles():
    try:
        # Escolhe um estilo de arte aleatório
        style = random.choice(art_styles)
        
        # Texto do tweet
        tweet = f"Hoje vamos falar sobre o estilo de arte {style}! #arte #{style.replace(' ', '')}"
        
        # Faz a postagem no Twitter
        api.update_status(tweet)
        
        logger.info(f"Tweet enviado: {tweet}")
    except tweepy.TweepError as e:
        logger.error(f"Erro ao postar no Twitter: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")

# Posta um tweet no momento em que o código é rodado
post_art_styles()

# Agenda a postagem para ser executada diariamente às 12:00
schedule.every().day.at("12:00").do(post_art_styles)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(3600)  # Verifica a programação a cada 1 hora
