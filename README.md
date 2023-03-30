## Nyx

### SOBRE O PROJETO :file_folder:
Microsserviço em Python utilizando FastAPI e mensageria com Kafka com o objetivo de praticar processos assíncronos envolvendo filas.

A Nyx é um API que envia ordens para um tópico do Kafka que serão consumidas e tratadas pelo Erebus (https://github.com/Ig0or/erebus).

<hr>

### TECNOLOGIAS QUE ESTÃO SENDO USADAS :space_invader:

:small_blue_diamond: Cryptography: Criptografar os valores que são enviados para o tópico do Kafka.

:small_blue_diamond: FastAPI: Web framework para construir a API.

:small_blue_diamond: Kafka-python: Client do Kafka para conexão e envio das mensagens.

:small_blue_diamond: Loglifos: Loggar avisos/erros.

:small_blue_diamond: Pip-chill: Alternativa ao pip-freeze, agrupando somente top-level.

:small_blue_diamond: Pydantic: Validação dos dados de entrada.

:small_blue_diamond: Pyfiglet: Prints mais bonitinhos :P

:small_blue_diamond: Pymongo: Conexão com banco de dados MongoDB.

:small_blue_diamond: Python-decouple: Utilizar variaveis de ambiente.

:small_blue_diamond: Uuid: Gerar unique id.

<hr>

### ROTAS DISPONIVEIS :telescope:

##### Acesse a rota abaixo para maiores detalhes.

```
{host}:{port}/docs
```

#### GET

```
{host}:{port}/stock_market/list_orders - Lista todas as ordens enviadas.
{host}:{port}/stock_market/detail_order/{order_id} - Busca detalhes de uma ordem especifica. 
```

#### POST

```
{host}:{port}/stock_market/send_order - Envia uma nova ordem de acordo com o body enviado - {"symbol": string, "quantity": integer}.
```

<hr>

### PARA EXECUTAR O SERVIDOR VIA DOCKER COMPOSE :floppy_disk:
- Com o Docker e Docker Compose instalados na sua maquina rode o comando ```docker-compose up -d``` ou ```docker compose up -d``` na pasta raiz do projeto.
- Ao executar com o Docker, será criado uma imagem para o Kafka, MongoDB, Nyx (produtor dos dados) e o Erebus (consumidor do dados)
- Acesse ```localhost:8080/docs```


### PARA EXECUTAR O SERVIDOR SEM O DOCKER :calling:
- Crie um novo ambiente virtual com ```python3 -m virtualenv .venv``` ou ```python3 -m venv .venv```
- Ative o seu novo ambiente virtual com ```source ./venv/bin/activate``` ou ```.venv\Scripts\activate.bat```
- Instale as dependências do projeto com ```pip install -r requirements.txt```

- Crie um arquivo ```.env``` na raiz do projeto de acordo com o ```.env_exemple```

```
-- SERVER --
SERVER_PORT= Porta em que o servidor ficará de pé.

-- KAFKA --
KAFKA_URI= Host de conexão com o Kafka.
KAFKA_CLIENT_ID= Nome do client que está usando o Kafka.
KAFKA_TOPIC_NAME= Nome do tópico onde as mensagens serão enviadas.

-- MONGODB --
MONGO_HOST= Conexão com o MongoDB.
MONGO_DATABASE= Nome do database.
MONGO_COLLECTION= Nome da collection.

-- OBFUSCATE --
FERNET_KEY= Chave que será utilizada para criptografar os valores enviados para o Kafka - Com a venv ativada execute o comando "python3 generate_fernet_key_script.py" para gerar uma nova chave.
```

- Execute o comando ```python3 nyx.py``` para startar o servidor.
- Acesse ```localhost:8080/docs```
