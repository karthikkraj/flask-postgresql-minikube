# Kubernetes Flask-PostgreSQL Application

## Project Overview
This repository contains a full-stack web application deployed on Kubernetes (Minikube), consisting of a Flask REST API backend with PostgreSQL database. The application demonstrates containerization, orchestration, and DevOps best practices.

## Features
- Flask REST API with CRUD operations
- PostgreSQL database with persistent storage
- Kubernetes configuration with Deployments, Services, ConfigMaps, and Secrets
- Docker containerization for application components
- Complete local development and deployment workflow

## Project Structure
```
├── app.py                  # Flask application with CRUD endpoints
├── init.sql                # Database initialization script
├── Dockerfile              # Flask app containerization
├── requirements.txt        # Python dependencies
├── backend-deploy.yaml     # Flask app deployment configuration
├── backend-service.yaml    # Service exposing the Flask API
├── db-config.yaml          # Database ConfigMap
├── db-secret.yaml          # Database credentials as Secret
├── postgres-deploy.yaml    # PostgreSQL deployment and service
├── postgres-pv.yaml        # Persistent volume configuration
```

## Deployment Instructions

### Prerequisites
- Docker installed
- Minikube installed
- kubectl configured

### Setup and Deployment

1. **Start Minikube**
   ```bash
   minikube start
   ```

2. **Configure Docker environment**
   ```bash
   eval $(minikube docker-env)
   ```

3. **Build Docker image**
   ```bash
   docker build -t 2022bcd0041-karthik .
   ```

4. **Deploy Kubernetes resources**
   ```bash
   kubectl apply -f postgres-pv.yaml
   kubectl apply -f db-config.yaml
   kubectl apply -f db-secret.yaml
   kubectl apply -f postgres-deploy.yaml
   kubectl apply -f backend-deploy.yaml
   kubectl apply -f backend-service.yaml
   ```

5. **Access the API**
   ```bash
   minikube service backend-service-2022bcd0041 --url
   ```

## API Endpoints

| Method | Endpoint    | Description         |
|--------|-------------|---------------------|
| GET    | /users      | Retrieve all users  |
| POST   | /user       | Create a new user   |
| PUT    | /user/<id>  | Update user by ID   |

## Configuration Details

### Database ConfigMap
Contains non-sensitive configuration:
- DB_HOST: postgres-service
- DB_NAME: mydatabase

### Database Secret
Contains base64-encoded sensitive data:
- DB_USER: postgres
- DB_PASSWORD: password

## Database Initialization
The PostgreSQL database is initialized with a users table as defined in init.sql:

```sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```

## Author
[Karthik Raj](https://github.com/karthikkraj)
Register Number: 2022bcd0041

## License
This project is for academic and educational purposes under IOE324 – Introduction to DevOps and Microservices.
