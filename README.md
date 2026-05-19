# Production DevOps Reliability Platform

This project demonstrates an end-to-end DevOps and SRE platform for deploying and managing a cloud-native application using AWS, Azure, Kubernetes, Terraform, CI/CD, monitoring, alerting, and automation.

## Key Features

- AWS infrastructure with Terraform
- Azure infrastructure with Terraform
- Dockerized Python application
- Kubernetes deployment
- Horizontal Pod Autoscaling
- GitHub Actions CI/CD pipeline
- Trivy security scanning
- Grafana/Prometheus monitoring
- Sentry error tracking
- PagerDuty-style incident response runbook
- Ansible configuration management
- Reliability engineering documentation

## Architecture

Developer pushes code to GitHub.  
GitHub Actions builds and scans Docker image.  
Application is deployed to Kubernetes.  
Prometheus collects metrics.  
Grafana shows dashboards.  
Sentry captures application errors.  
PagerDuty-style workflow handles incidents.  
Terraform provisions infrastructure.  
Ansible configures servers.

## Tools Used

- AWS
- Azure
- Terraform
- Docker
- Kubernetes
- GitHub Actions
- Helm
- Ansible
- Prometheus
- Grafana
- Sentry
- PagerDuty
- Trivy

## DevOps Responsibilities Covered

### Cloud Infrastructure

Designed AWS and Azure cloud infrastructure using Terraform.

### CI/CD

Created GitHub Actions pipeline for build, test, scan, and deployment automation.

### Monitoring

Implemented Prometheus and Grafana for infrastructure and application metrics.

### Error Tracking

Integrated Sentry for application exception tracking.

### Incident Management

Created PagerDuty-style incident response runbook.

### Automation

Used Terraform for provisioning and Ansible for configuration management.

### Scaling

Implemented Kubernetes Horizontal Pod Autoscaler.

### Reliability Engineering

Added health checks, rollback strategy, SLOs, and postmortem documentation.
