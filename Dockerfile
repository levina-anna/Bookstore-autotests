# Используем последнюю версию Ubuntu как базовый образ
FROM ubuntu:latest

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    python3 \
    python3-pip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1

# Установка Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i --force-depends google-chrome-stable_current_amd64.deb || apt-get install -f -y \
    && rm google-chrome-stable_current_amd64.deb

# Установка ChromeDriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.128/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver-linux64.zip

# Установка Python зависимостей
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Копируем директорию с тестами в контейнер
COPY tests /tests

# Копируем файл окружения в контейнер
COPY .env /

WORKDIR /tests

# Запуск тестов с pytest
CMD pytest -s /tests/test_cost_table.py

