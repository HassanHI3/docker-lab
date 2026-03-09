🐳 Docker Projects

This repository contains two Docker-based projects demonstrating containerised web applications and multi-container architectures using Docker Compose.

- `my-app` — Multi-container Flask + Redis application
- `hello_flask` — Flask + MySQL application containerised with Docker
***
## 📂 1. my-app — Flask + Redis + Nginx

This project is a multi-container application using Flask (Python) and Redis. The Flask app displays a welcome message and tracks visit counts, which are stored in Redis. Both services are containerized using Docker and orchestrated with Docker Compose.

## Requirements

- **Flask**: Python web framework for the web app
- **Redis**: Key-value store to track visit counts
- **Docker**: Containerization platform
- **Docker Compose**: Tool to manage multi-container apps
***
### Endpoints
- / → Welcome page with button to /count.
- /count → Increments and displays visit count (shared across all instances via Redis).
***
## How to Run

Follow these steps to get the application running on your local machine:

### Ensure Docker and Docker Compose are installed

Make sure you have Docker Desktop and Docker Compose installed on your machine.

### Clone the repository

```bash
git clone <your-repo-url>
cd my-app
```

### Build and run the containers

In the project directory, execute:
```bash
docker compose up --build
```
### Access the app

Open your browser and go to:
```bash
http://localhost:5006
```
- Visit the home page: You’ll see a welcome message

- Visit /count: Each refresh increments the visitor count stored in Redis

### Features

- Flask Web App: Two routes — welcome page (/) and visit count (/count)

- Redis Integration: Stores visit count in Redis

- Nginx Reverse Proxy: Nginx forwards requests from port 5006 to the Flask app running on port 5005

- Persistent Redis Storage: Redis data is stored in a named volume (redis-data), ensuring the visit counts persist even if the containers restart

### Notes

The Flask app runs on port 5005 internally, and Nginx exposes it on port 5006

This demonstrates Docker networking where containers communicate using service names instead of localhost

***

## 📂 2. hello_flask — Flask + MySQL

## Overview

A Python Flask application connected to a MySQL database using Docker Compose.  
The application retrieves the MySQL version from the database and displays it in the browser.

## Features

- **Flask** — Python web framework
- **MySQL** — Relational database
- **Docker Compose** — Multi-container orchestration
- **Multi-stage Docker build** — Reduces image size

## How to Run

### Build and start the services

```bash
docker compose up --build
```
### Visit the app

Open your browser and go to:
```bash
http://localhost:5002
```

### MySQL Configuration
- MySQL root password: my-secret-pw (set in docker-compose.yml)
- Database service name: db (named as mydb as a container in docker-compose.yml)

### Database service name
```bash
db
```
### Notes

- The my-app project demonstrates container-to-container communication using Redis

- The hello_flask project demonstrates Dockerising a web application connected to a relational database

