 # Docker Learning 

🐳 Docker Learning – Flask + MySQL Lab

📌 Project Overview
This lab demonstrates how to containerise a simple Flask web application and connect it to a MySQL database using Docker.
The objective of this project was to understand:
How Docker packages applications into images
How containers run in isolated environments
How containers communicate using Docker networking
How to use Docker Compose for multi-container setups
The difference between host networking and container networking

🛠 Tech Stack
- Python 3 (Slim Image)
- Flask
- MySQL
- Docker
- Docker Compose

🏗 Architecture Overview
Host Machine
    ↓
Docker Engine
    ↓
Containers
    ├── Flask App Container
    └── MySQL Database Container
    ↓
Custom Bridge Network

Key Networking Concept
The Flask container connects to MySQL using the Docker Compose service name as the hostname, not localhost.

Inside a container:
localhost refers to the container itself
Services communicate using the Docker network
📂 Project Structure
hello_flask/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
└── README.md

📦 Dockerfile Breakdown
Uses python:3.x-slim as a lightweight base image
Sets working directory to /app
Installs system dependencies for MySQL client
Installs Python dependencies (flask, mysqlclient)
Exposes port 5002
Runs the application using python app.py

▶️ Running the Application
1️⃣ Build the Docker Image
docker build -t hello-flask-mysql .
2️⃣ Run the Container
docker run -p 5002:5002 hello-flask-mysql

Access in browser:
http://localhost:5002

🐳 Running with Docker Compose (App + Database)
docker compose up -d
This command:
Creates both containers
Connects them to the same Docker network
Automatically handles service dependencies
Runs the application and database together

🧠 Key Concepts Learned
Containers are isolated but can communicate through Docker networks
localhost inside a container is not the host machine
Docker Compose simplifies multi-container orchestration
YAML formatting must be precise
SSH vs HTTPS authentication differences when pushing to GitHub
Container networking vs local machine networking

🛠 Issues Faced & Resolved
GitHub Permission Denied (403)
Cause: SSH account mismatch
Fix: Correct SSH key configuration

Docker Compose Service Reference Error
Cause: Incorrect service dependency definition
Fix: Correct YAML structure and service naming

Container Networking Confusion
Cause: Attempting to use localhost between containers
Fix: Use Docker service name as hostname

🎯 Learning Outcome
By completing this lab, I now understand:
How to containerise backend applications
How multi-container applications communicate
How to debug Docker build and networking issues
The foundational concepts required before moving into Kubernetes
