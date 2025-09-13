# 🐳 Scraper com Node.js + Chromium + Cron

Este projeto roda um **scraper em Node.js** dentro de um container Docker, utilizando **Chromium** (para automação com Puppeteer) e **cron** (para agendamento de tarefas).

---

## 🚀 Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado
- [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Executando o projeto com Docker Compose

Para executar o projeto, basta ter o Docker e o Docker Compose instalados e executar o seguinte comando na raiz do projeto:

```sh
docker-compose up -d
```

Este comando irá construir as imagens e iniciar os containers em modo detached.

### Executando o scraper manualmente

Para executar o scraper manualmente, utilize o seguinte comando:

```sh
docker-compose exec scraper node scraper.js
```

Este comando irá executar o script `scraper.js` dentro do container do scraper e irá gerar os arquivos `output.json` e `screenshot.png` na pasta `scraper`.

### ⏰ Gerenciando o cron

O container já inicia com o cron habilitado pelo entrypoint.sh.

Para verificar os logs do cron, utilize o seguinte comando:

```sh
docker-compose exec scraper tail -f /var/log/cron.log
```

## 📂 Estrutura de pastas

.
├── classes_dowload     # Código relacionado ao scraping
├── cron.d              # Configurações de agendamento do cron
├── docker/entrypoint.sh # Script que inicia cron + app
├── package.json
├── package-lock.json
└── Dockerfile

## 📌 Variáveis de ambiente

PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium → Define o caminho do Chromium dentro do container.

## 📡 Endpoints

O app expõe a porta 5000:

```
http://localhost:5000
```