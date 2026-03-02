**This mini project demonstrates how to build and run a multi-container application using Docker and Docker Compose.**

**Overview**

The application consists of:
- A Python Flask web app
- A Redis database
- Managed together using Docker Compose

The Flask app connects to Redis to store and retrieve a visit counter.

Application Routes
- / → Displays a simple welcome message
- /count → Increments and displays a visit count stored in Redis
- Each time the /count endpoint is refreshed, the counter increases — proving persistent inter-container communication.

Tech Stack:
- Python (Flask)
- Redis (Key-Value Store)
- Docker
- Docker Compose

What This Demonstrates?
- Building custom Docker images
- Running multiple containers in a shared network
- Service-to-service communication (Flask ↔ Redis)
- Containerised application architecture
- Infrastructure reproducibility using Docker Compose

