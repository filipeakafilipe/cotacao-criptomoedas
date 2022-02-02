# Desafio Técnico Back-end - Smarttbot
Monitoramento de cotações de criptomoedas

### Sobre
O projeto visa monitorar e obter os dados das cotações de criptomoedas, disponibilizadas pela Poloniex, e agregá-las em candlesticks e salvá-las em um banco de dados. A cada 1, 5 e 10 minutos, novos candlesticks, separados por sua frequência, serão salvos, das moedas Bitcoin, Ethereum e Solana, pareadas pelo dólar (USDT).

### Descrição do desafio
Dados os preços de execução (cotações) de uma criptomoeda reportados em tempo real através de uma API pública, você deve criar um sistema que irá processar estas cotações, agregá-las em candlesticks (com os dados de abertura, máxima, mínima e fechamento, e salvar estes candles em um banco de dados.
Você deve construir os candles de 1min, 5min e 10min. Os candles só precisam ser salvos no banco de dados uma vez que estejam completos (não precisam ser atualizados no banco de dados em tempo real). Por exemplo, a cada um minuto, o sistema irá salvar no banco de dados o último candle de 1min finalizado.
A API a ser consumida é obrigatoriamente a Poloniex Public API (mais especificamente o comando returnTicker ou o canal websocket Ticker Data). Assim, não utilize clientes de terceiros para consumir a API Poloniex, pois invalidará o seu teste. Você deverá desenvolver o seu próprio cliente.

### Instalação
##### Localmente
Para a instalação local precisamos de:
* Python 3
* pip3
* MySQL 

Passos:
* Configure um servidor MySQL, com base chamada smarttbot e configure a connection string no arquivo `src/infra/config/db_config.py`.
* Utilizando o comando `pip3 install -r requirements.txt` na raiz do projeto, instale suas dependências.
* No arquivo, `src/domain/modeld/valid_currencies.py`, estão presentes as criptomoedas e pares a serem monitorados.
* Na pasta raiz do projeto, utilize o comando `py run.py`, para iniciar o monitoramento das criptomoedas.
* Para rodar os testes, na raiz do projeto utilizar o comando `py -m unittest src.main.tasks.monitor_currencies_test`.

##### Docker
Para a instalação com o Docker precisamos de:
* Docker
* Docker Compose

Passos:
* Na pasta raiz do projeto, utilize o comando `docker-compose up`, para subir os containers da aplicação e banco de dados.

### Tecnologias utilizadas
* Clean Architecture
* Git
* Github
* Python 3.10.2
* MySQL
* Docker

### Considerações, dificuldades e pontos de melhoria
A maior dificuldade foi a falta de conhecimento sobre a linguagem, uma vez que muitos aspectos são diferentes dos quais estou acostumado. Entender como o Python funciona e suas nuances foi um grande desafio, mas compensador e divertido, ainda mais com o tema do desafio proposto, criptomoedas.
Encarar os módulos foi uma das partes mais complicadas, onde muitas vezes ocasionou, inesperadamente, o erro de ModuleNotFound. Ao invés de se utilizar DAO puro, foi tentado utilizar o ORM SQLAlchemy, mas por causa da classe Base e os módulos, acabava acarretando em um contexto diferente de onde as tabelas eram declaradas. Entender como a injeção de dependência, dentre outros conceitos, funcionam seria de grande valia para o projeto. Foi tentado também a criação de uma API, utilizando Flask, para expor os dados das criptomoedas monitoradas, mas não consegui rodar ao mesmo tempo a task de monitoramento. Uma possível solução, mas que não foi testada ou implementada, seria rodar em um container separado da aplicação onde a task roda. Foi utilizado no projeto o framework unittest, invés do pytest, onde também não consegui solucionar o erro dos módulos. Embora a principal aplicação tenha sido testada, ela possui diversos pontos de melhoria, como a utilização de alguma biblioteca de mocks, como do próprio unittest, e também o aumento da cobertura de testes e as fronteiras dos casos.
A aplicação possui diversos pontos de melhoria, assim como todo software. A arquitetura não favorece a inclusão e monitoramento de diversas criptomoedas, começando a ficar lenta com muitas moedas, embora seja funcional. Uma mudança eficaz para o projeto seria a utilização do canal de websocket, invés das requisições ao comando returnTicker. A classe de CurrenciesMonitoring poderia menos responsabilidades, assim como boas práticas, como SOLID, DRY e KISS, também poderiam ter sido melhor empregados.