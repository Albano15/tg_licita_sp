# 🐳 Scraper com Node.js + Chromium + Cron

Este projeto roda um **scraper em Node.js** dentro de um container Docker, utilizando **Chromium** (para automação com Puppeteer) e **cron** (para agendamento de tarefas).

---

## 🚀 Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado
- Opcional: [Docker Compose](https://docs.docker.com/compose/)

---

## 🔨 Build da imagem

### Build normal (com cache)

```sh
docker build -t scraper-app .
Build sem cache
docker build --no-cache -t scraper-app .

▶️ Executando o container
Rodar o container normalmente
docker run -d --name scraper-container -p 5000:5000 scraper-app

Rodar o container com shell interativo
docker run -it --rm --name scraper-container -p 5000:5000 scraper-app bash

🗑️ Removendo containers e imagens
Parar e remover o container
docker stop scraper-container
docker rm scraper-container

Remover a imagem
docker rmi scraper-app

⏰ Gerenciando o cron
O container já inicia com o cron habilitado pelo entrypoint.sh.

Ativar o cron
Se por algum motivo ele tiver sido desativado, você pode iniciar manualmente:
docker exec -it scraper-container service cron start

Desativar o cron
docker exec -it scraper-container service cron stop

Ver status do cron
docker exec -it scraper-container service cron status

Logs do cron
docker exec -it scraper-container tail -f /var/log/cron.log

📂 Estrutura de pastas

.
├── classes_dowload     # Código relacionado ao scraping
├── cron.d              # Configurações de agendamento do cron
├── docker/entrypoint.sh # Script que inicia cron + app
├── package.json
├── package-lock.json
└── Dockerfile

📌 Variáveis de ambiente
PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium → Define o caminho do Chromium dentro do container.

📡 Endpoints
O app expõe a porta 5000:

arduino

http://localhost:5000
```
