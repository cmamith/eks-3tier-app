eks-3tier-app/README.md

Overview

This repo contains the application code and infrastructure definitions for a production-style 3-tier app deployed on AWS EKS. It demonstrates modern DevOps practices: Infrastructure-as-Code, GitOps, secure secrets management, observability, and CI/CD integration. This repository is ideal for DevOps engineers looking to deploy scalable and secure applications on AWS EKS.

Architecture
           Internet
              |
          Amazon ALB (via AWS Load Balancer Controller)
           /     \
   /frontend     (services)
     |                   
     v                   
  Frontend  ————>  Auth-Service  ——>  RDS (MySQL)
  (Frontend handles user interactions, Auth-Service validates user credentials and writes session data to RDS.)
                      |  
                      v  
                 Profile-Service ——>  RDS (PostgreSQL)


   [External Secrets Operator]
        | (IRSA)
        v
   AWS Secrets Manager

 Observability: Prometheus → exporters → Grafana
 Observability: Prometheus <— exporters — Grafana
 Logging: Fluent Bit —> CloudWatch Logs
Tech Stack

The following tools and technologies are used in this project:

Component	Purpose
Terraform	Provision VPC, EKS, IAM, RDS, networking
Helm	Package and deploy microservices
Argo CD	GitOps delivery (managed in separate repo)
ESO + IRSA	Secure secrets from AWS Secrets Manager
Repo Layout

This section provides an overview of the repository structure for developers and contributors.

terraform/       # VPC, EKS, IAM IRSA, RDS modules
charts/          # Helm charts for frontend, auth, profile
k8s/             # ESO manifests, ingress, namespaces
docker/          # Dockerfiles per service
scripts/         # Build & bootstrap helpers
Flow

This section outlines the high-level data flow and interactions between components.

Frontend sends login → Auth-service validates → writes to MySQL.
Flow

Frontend sends login → Auth-service validates → writes to MySQL.

Profile-service reads user profile data → stored in PostgreSQL.

Secrets (DB credentials) live in AWS Secrets Manager and sync into K8s via ESO.

Setup Instructions

**Prerequisites:** Ensure you have Terraform, AWS CLI, and Docker installed before proceeding.

Provision infra:

Provision infra:

cd terraform/envs/dev
terraform init -backend-config=backend.tfvars
terraform apply -var-file=terraform.tfvars -auto-approve

Build & push images:

./scripts/build_push_ecr.sh auth-service <TAG>
./scripts/build_push_ecr.sh profile-service <TAG>
Deploy via GitOps: update tags in the GitOps repository (e.g., [gitops-apps](https://github.com/your-org/gitops-apps)) to reflect the new image versions.

Deploy via GitOps: update tags in GitOps repo (gitops-apps).

Local Testing

This section provides instructions for testing the application locally during development.

Run services with Docker Compose (optional).

CI/CD

This section outlines the automated build and deployment process for the application.

GitHub Actions / Jenkins builds images → pushes to ECR → updates GitOps repo with new tag.

GitHub Actions / Jenkins builds images → pushes to ECR → updates GitOps repo with new tag.

Troubleshooting

Ingress stuck: check ALB controller logs & annotations.

Pod CrashLoop: verify DB credentials in K8s Secret.

Secrets empty: ensure ESO has IRSA IAM permissions.

**Note:** For additional context when resolving issues, always refer to the relevant logs and official documentation.

Roadmap

Move nodes to private subnets.

Add ExternalDNS, HPA/VPA, PodDisruptionBudgets.

Security scans with Trivy/SonarQube.

Contributions to the roadmap are welcome. Please submit issues or pull requests for consideration.

Security scans with Trivy/SonarQube.
