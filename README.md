🐳 Docker Projects

This repository contains two Docker-based projects demonstrating containerised web applications and multi-container architectures using Docker Compose.
my-app — Multi-container Flask + Redis application
hello_flask — Flask + MySQL application containerised with Docker

📂 1. my-app — Flask + Redis

Overview
A simple Python Flask web application connected to a Redis database.
The application stores and increments a visitor counter using Redis, demonstrating inter-container communication using Docker Compose.

Features
Flask — Python web framework for serving pages
Redis — Key-value store used to track visitor counts
Docker Compose — Runs and manages multiple containers

Endpoint
/ → Displays a welcome message and visitor count
Each page refresh increments the visitor count stored in Redis.

How to Run
Build and start services:
docker compose up --build

Visit:
http://localhost:5005
Container Communication

The Flask container connects to Redis using the Docker service name:
redis

This demonstrates Docker networking where containers communicate using service names instead of localhost.
📂 2. hello_flask — Flask + MySQL

Overview
A Python Flask application connected to a MySQL database using Docker Compose.
The application retrieves the MySQL version from the database and displays it in the browser.

Features
Flask — Python web framework
MySQL — Relational database
Docker Compose — Multi-container orchestration
Multi-stage Docker build — Reduces image size

How to Run
Build and start services:
docker compose up --build

Visit the app:
http://localhost:5002
MySQL Configuration
MySQL root password:
my-secret-pw
Database service name:
mydb

The Flask application connects to MySQL using the service name defined in docker-compose.yml.
Notes

The my-app project demonstrates container-to-container communication using Redis.
The hello_flask project demonstrates Dockerising a web application connected to a relational database.
Both projects demonstrate multi-container architectures using Docker Compose and can be extended for deployment to container platforms such as AWS ECS, ECR, or Kubernetes.
