# Use a imagem oficial do Node.js
FROM node:18

# Instale o cron e as dependências do Puppeteer
RUN apt-get update && apt-get install -y cron gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget chromium

# Crie um diretório de trabalho
WORKDIR /usr/src/app

# Copie os arquivos do projeto
COPY . .

# Instale o Puppeteer
RUN npm install puppeteer

# Dê permissão ao entrypoint
RUN chmod +x /usr/src/app/entrypoint.sh

# Copie o arquivo de cron
COPY cron.d/scraper-cron /etc/cron.d/scraper-cron
RUN chmod 0644 /etc/cron.d/scraper-cron
RUN crontab /etc/cron.d/scraper-cron

# Execute o entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]