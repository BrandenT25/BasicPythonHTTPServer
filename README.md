# 🚀 Python HTTP Server - DevOps Project

A production-ready HTTP server built from scratch using Python sockets, demonstrating full-stack DevOps capabilities including containerization, infrastructure as code, CI/CD, and monitoring.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)

## ✨ Key Features

- **Custom HTTP Server:** Built entirely from scratch using Python's socket library (no frameworks)
- **HTTP Methods:** Handles GET and POST requests with proper routing
- **Request Logging:** Tracks all incoming requests with timestamps, IP addresses, methods, and paths
- **Metrics Endpoint:** Exposes `/metrics` in Prometheus format for monitoring
- **Error Handling:** Proper 404 responses and status code tracking

## 🐳 Containerization

### Docker Implementation
- Multi-container architecture with application and Prometheus containers
- Optimized Dockerfile for Python applications
- Container networking configured for inter-service communication
- Proper volume mounting for configuration files

## ☁️ Cloud Infrastructure

### AWS Deployment
- **Platform:** AWS EC2 (t3.micro)
- **Region:** US-East-2
- **OS:** Amazon Linux 2023
- **Networking:** Custom security groups with proper port configuration

### Infrastructure as Code (Terraform)
- EC2 instance provisioning
- Security group configuration (ports 22, 8000/9000, 9090)
- Automated infrastructure deployment
- Version-controlled infrastructure definitions

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow
- **Trigger:** Automatic deployment on push to main branch
- **Process:**
  1. SSH into EC2 instance
  2. Pull latest code from GitHub
  3. Rebuild Docker containers
  4. Deploy updated application with zero manual intervention
- **Benefits:** Continuous deployment, automated testing, rapid iteration

## 📊 Monitoring & Observability

### Prometheus Integration
- Real-time metrics collection and monitoring
- Custom application metrics:
  - Total HTTP requests
  - Requests by path
  - HTTP status code distribution
- Prometheus dashboard accessible at `:9090`
- Configurable scrape intervals

## 🏗️ Architecture Overview

### Application Layer
- Python HTTP server handling requests on port 9000
- Route-based request handling (/, /about, /contact, /metrics)
- Request logging and metrics generation

### Container Layer
- Dockerized application for portability
- Separate Prometheus container for monitoring
- Host networking for inter-container communication

### Infrastructure Layer
- AWS EC2 instance managed by Terraform
- Security groups controlling inbound/outbound traffic
- Automated deployment via GitHub Actions

## 🎯 Skills Demonstrated

- **Programming:** Python, networking protocols, HTTP implementation
- **DevOps:** CI/CD pipelines, automation, configuration management
- **Containerization:** Docker, multi-container orchestration
- **Cloud:** AWS EC2, security groups, cloud networking
- **IaC:** Terraform for infrastructure management
- **Monitoring:** Prometheus metrics, observability
- **Version Control:** Git, GitHub, branching strategies

## 🚦 Getting Started

### Local Development
```bash
# Clone the repository
git clone <repository-url>

# Build Docker image
docker build -t http-server .

# Run container
docker run -p 9000:9000 http-server

# Access at http://localhost:9000
```

### Deployment
```bash
# Configure AWS credentials
aws configure

# Initialize Terraform
terraform init

# Apply infrastructure
terraform apply

# Push to main branch triggers automatic deployment via GitHub Actions
git push origin main
```

## 📈 Future Enhancements

- Grafana integration for advanced visualization
- Load balancing with multiple instances
- HTTPS/SSL certificate implementation
- Kubernetes deployment
- Automated testing suite
- Database integration

## 📝 License

This project is open source and available for educational purposes.

---

**Built with ❤️ as a DevOps learning project**
