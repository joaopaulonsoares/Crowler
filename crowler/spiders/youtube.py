import scrapy


class youtube(scrapy.Spider):
    # Dar o nome
    name = 'youtube'

    # Definir urls que vai crawlear
    start_urls = ['https://www.youtube.com/']

    def parse(self, response):
        # print(response.body)

        # Obter no navegador
        #   1 - Acesse o site
        #   2 - Aperte f12
        #   3 - Selecione a ferramenta para selecionar um local
        #   4 - Clique em copy as selector
        #   5 - Cole o resultado dentro de response.css(' AQUI ')
        titulo = response.css('h3 ::text').extract()
        for video in titulo:
            print(video)

        # print(titulo)

# Pesquisar sobre o robots.txt
# Pesquisar sobre css selector
# https://doc.scrapy.org/en/latest/intro/tutorial.html
# Para rodar: scrapy crawl <classe>
