
---

# Projeto Django - Gerenciador da Radio UFT

Este projeto é um aplicativo Django configurado para ser executado em um ambiente Docker com PostgreSQL.

## Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados no seu sistema. Você pode baixá-los em [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/).

## Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone https://github.com/Radio-UFT/radio_manager.git
   cd radio_manager
   ```

2. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente necessárias. Você pode usar `.env.example` como referência.

3. Execute o seguinte comando para construir a imagem do Docker e iniciar os contêineres:

   ```bash
   docker-compose up --build
   ```

4. Aguarde até que todos os contêineres sejam iniciados. Isso inclui o contêiner do aplicativo Django e o contêiner do PostgreSQL.

5. Abra um navegador da web e acesse [http://localhost:8000/](http://localhost:8000/) para visualizar o aplicativo Django.

## Comandos Úteis

- Para parar os contêineres, pressione `Ctrl+C` no terminal onde o `docker-compose up` está sendo executado.

- Para reiniciar os contêineres após a modificação do código ou configuração, execute:

  ```bash
  docker-compose up --build
  ```

- Para parar e remover os contêineres, execute:

  ```bash
  docker-compose down
  ```

## Contribuindo

Sinta-se à vontade para contribuir com melhorias para este projeto. Abra uma issue ou envie um pull request!
