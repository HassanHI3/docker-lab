 # Docker Learning 

Flask + MySQL Docker Lab
Project Overview:

This lab demonstrates how to containerise a simple Flask web application and connect it to a MySQL database using Docker.
The goal was to understand:
How Docker packages applications
How containers communicate using Docker networking
How to use Docker Compose for multi-container setups
How images are built and run in isolated environments

Tech Stack:
Python 3 (Slim Image)
Flask
MySQL
Docker
Docker Compose

Architecture Overview
Host Machine
⬇
Docker Engine
⬇
Containers:
Flask App Container
MySQL Database Container
⬇
Custom Docker Network (bridge)

The Flask container connects to MySQL using the service name as the hostname, not localhost.
Project Structure
hello_flask/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md

Dockerfile Breakdown
Uses python:3.x-slim
Sets working directory to /app
Installs system dependencies for MySQL client
Installs Python dependencies (flask, mysqlclient)
Exposes port 5002
Runs the app using python app.py

Running the App
1️⃣ Build the image
docker build -t hello-flask-mysql .
2️⃣ Run with Docker
docker run -p 5002:5002 hello-flask-mysql
Access in browser:
http://localhost:5002

Running with Docker Compose (App + DB)
docker compose up -d
This:
Creates both containers
Connects them on the same network
Automatically handles service dependencies

Key Concepts Learned
Containers are isolated but can communicate via Docker networks
localhost inside a container ≠ host machine
Docker Compose simplifies multi-container applications
YAML structure must be correctly formatted
GitHub SSH vs HTTPS authentication differences

Issues Faced & Resolved
Permission denied when pushing to GitHub (SSH account mismatch)
Docker Compose service reference errors
Understanding container networking vs local networking

Learning Outcome
By completing this lab, I now understand:
How to containerise backend applications
How services communicate across Docker networks
How to debug container build and networking issues
The foundation needed before moving into Kubernetes
