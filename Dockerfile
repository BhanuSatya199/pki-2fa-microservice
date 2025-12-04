# ---- builder ----
FROM python:3.11-slim as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# ---- runtime ----
FROM python:3.11-slim
ENV TZ=UTC
WORKDIR /app

# system deps for cron
RUN apt-get update && apt-get install -y --no-install-recommends cron tzdata && \
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" > /etc/timezone && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# copy python packages from builder
COPY --from=builder /install /usr/local

# copy app code and scripts
COPY . /app

# ensure /data and /cron exist and are correct perms
RUN mkdir -p /data /cron && chmod 755 /data /cron

# install cron file
RUN crontab cron/2fa-cron

EXPOSE 8080

# start cron and uvicorn (both in foreground)
CMD service cron start && uvicorn app.main:app --host 0.0.0.0 --port 8080
