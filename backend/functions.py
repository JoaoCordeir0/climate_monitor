import requests
from bs4 import BeautifulSoup

#
# Executa a requisição no site do climatempo para retornar as informações em HTML
#
def execRequest():
    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/554/saojoaodaboavista-sp', headers=headers).content
    return BeautifulSoup(response, 'html.parser')

#
# Define o template em HTML no qual o conteúdo tratado será inserido
#
def HTMLtemplate(content):
    return f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Monitor de clima</title>
                <link rel="icon" href="../static/imgs/favicon.ico">
                <link rel="stylesheet" href="../static/css/style.css">
            </head>
            <body>
                <div class="container">
                    <p class="location"><img width="20" src="../static/imgs/location.png"> São João da Boa Vista</p>
                    {content}
                    <p class="credits"> Dev by João Victor Cordeiro </p>
                </div>
            </body>
        </html>
    """

#
# Faz o tratamento das informações que serão exibidas
#
def getClime(body):
    text = str(body.find(class_='-gray -line-height-24 _center'))

    icons = str(body.find(class_='col-md-6 col-sm-12 _flex _space-between _margin-t-sm-20')).replace('data-src="/dist/', 'src="https://climatempo.com.br/dist/')    
    
    temp = str(body.find(class_='variables-list')).replace('data-src="/dist/', 'src="https://climatempo.com.br/dist/').replace('src="/dist/', 'src="https://climatempo.com.br/dist/')
    
    return text + icons + temp

#
# Reescreve o HTML da index que será exibida para o usuário
#
def generateIndexHTML():
    with open('frontend/template/index.html', 'w+', encoding='utf8') as file:
        file.write(
            HTMLtemplate(
                getClime(
                    execRequest()
                )
            )
        )



