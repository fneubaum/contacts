# Contacts application

This is a simple application that lets you manage your contacts, it has been written in Vuejs (Quasar) for the backend and Flask for the backend.

You can make it work following these instructions.

## Frontend setup

```bash
npm install
```

### Compiles and hot-reloads for development

```bash
npm run serve
```

### Compiles and minifies for production

```bash
npm run build
```

## Backend setup

```bash
pip install -r requirements.txt
```

### Run the server for development

```bash
gunicorn -b 0.0.0.0:5000 app:app
```

## Build Docker container for deployment

```bash
docker build -t contacts .
```

### Run container locally

```bash
docker run --rm -p 8000:8000 --name contacts contacts:latest
```