 # Docker Learning 

🐳 Docker based project
Overview

This repository contains small projects built to practice Docker fundamentals and multi-container application development.

The projects demonstrate how to containerise applications, connect services together using Docker networking, and manage multiple containers with Docker Compose.

Tech Stack:
Docker
Docker Compose
Python (Flask)
MySQL
Redis

Projects:
1️⃣ Flask + MySQL Application
A containerised Flask application connected to a MySQL database.

**Concepts demonstrated**
- Writing Dockerfiles
- Multi-stage builds
- Running multiple containers with Docker Compose
- Container-to-container communication using service names
- Database connectivity from containers

Project folder:
hello_flask/

2️⃣ Flask + Redis Visitor Counter
A simple Flask web app that connects to Redis to store and increment a visitor counter.
Each refresh increases the visitor count stored in Redis, demonstrating persistent container communication.
Concepts demonstrated
Multi-container applications
Service discovery in Docker networks
Using Redis as a key-value store
Container orchestration with Docker Compose

Project folder:
my-app/

**How to Run the Project**
Navigate to the project folder and run:
- docker compose up --build

Then open the application in your browser using the port specified in the project.

**Key Concepts Practiced**
Containerisation with Docker
Building images with Dockerfiles
Multi-container architectures
Docker networking and service discovery
Application orchestration with Docker Compose

🧠 **Key Concepts Learned**
- Containers are isolated but can communicate through Docker networks
- localhost inside a container is not the host machine
- Docker Compose simplifies multi-container orchestration
- YAML formatting must be precise
- SSH vs HTTPS authentication differences when pushing to GitHub
- Container networking vs local machine networking

🛠 **Issues Faced & Resolved**
GitHub Permission Denied (403)
- Cause: SSH account mismatch
- Fix: Correct SSH key configuration

**Docker Compose Service Reference Error**
- Cause: Incorrect service dependency definition
- Fix: Correct YAML structure and service naming

**Container Networking Confusion**
- Cause: Attempting to use localhost between containers
- Fix: Use Docker service name as hostname

🎯 **Learning Outcome**
- By completing this lab, I now understand:
- How to containerise backend applications
- How multi-container applications communicate
- How to debug Docker build and networking issues
- The foundational concepts required before moving into Kubernetes
