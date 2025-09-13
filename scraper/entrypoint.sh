#!/bin/bash

# Inicia o cron em background
cron -f &

# Mantém o container rodando
tail -f /dev/null