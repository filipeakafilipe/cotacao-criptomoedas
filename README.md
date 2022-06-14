Monitoramento de cotações de criptomoedas

### Sobre
O projeto visa monitorar e obter os dados das cotações de criptomoedas, disponibilizadas pela Poloniex, e agregá-las em candlesticks e salvá-las em um banco de dados. A cada 1, 5 e 10 minutos, novos candlesticks, separados por sua frequência, serão salvos, das moedas Bitcoin, Ethereum e Solana, pareadas pelo dólar (USDT).

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
