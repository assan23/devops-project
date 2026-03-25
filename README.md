# 🚀 DevOps Project

## 📌 Description

Ce projet consiste à développer une API REST avec Flask, la conteneuriser avec Docker, puis la déployer sur Kubernetes.
Un pipeline CI/CD est utilisé pour automatiser le build, les tests et le déploiement.
L’infrastructure est provisionnée avec Terraform et configurée avec Ansible.

---

## 🧱 Architecture

* Application : Flask
* Containerisation : Docker
* Orchestration : Kubernetes
* CI/CD : GitHub Actions
* Infrastructure : Terraform + Ansible

---

## 🔗 Endpoints

| Route       | Description          |
| ----------- | -------------------- |
| GET /       | Message de bienvenue |
| GET /health | Statut OK            |

---

## 🚀 Lancer en local

```bash
pip install -r app/requirements.txt
python app/app.py
```

👉 http://localhost:5000

---

## 🐳 Lancer avec Docker

```bash
docker build -t devops-flask-api ./app
docker run -p 5000:5000 devops-flask-api
```

---

## ☸️ Déploiement Kubernetes

```bash
kubectl apply -f k8s/
```

---

## ⚙️ Infrastructure (Terraform)

```bash
terraform init
terraform plan
terraform apply
```

---

## 🤖 CI/CD

Le pipeline GitHub Actions automatise :

* Build de l’image Docker
* Tests avec pytest
* Déploiement Kubernetes

---

## 🔁 Reproduire le projet

```bash
git clone https://github.com/assan23/devops-project.git
cd devops-project

# Docker
docker build -t devops-flask-api ./app
docker run -p 5000:5000 devops-flask-api

# Kubernetes
kubectl apply -f k8s/

# Terraform (optionnel)
terraform init
terraform apply
```

---

## ⚠️ Sécurité

Les fichiers sensibles (clé SSH, Terraform state) ne sont pas inclus dans le repository pour des raisons de sécurité.

---

## 👨‍💻 Auteurs

* # 🚀 DevOps Project

## 📌 Description

Ce projet consiste à développer une API REST avec Flask, la conteneuriser avec Docker, puis la déployer sur Kubernetes.
Un pipeline CI/CD est utilisé pour automatiser le build, les tests et le déploiement.
L’infrastructure est provisionnée avec Terraform et configurée avec Ansible.

---

## 🧱 Architecture

* Application : Flask
* Containerisation : Docker
* Orchestration : Kubernetes
* CI/CD : GitHub Actions
* Infrastructure : Terraform + Ansible

---

## 🔗 Endpoints

| Route       | Description          |
| ----------- | -------------------- |
| GET /       | Message de bienvenue |
| GET /health | Statut OK            |

---

## 🚀 Lancer en local

```bash
pip install -r app/requirements.txt
python app/app.py
```

👉 http://localhost:5000

---

## 🐳 Lancer avec Docker

```bash
docker build -t devops-flask-api ./app
docker run -p 5000:5000 devops-flask-api
```

---

## ☸️ Déploiement Kubernetes

```bash
kubectl apply -f k8s/
```

---

## ⚙️ Infrastructure (Terraform)

```bash
terraform init
terraform plan
terraform apply
```

---

## 🤖 CI/CD

Le pipeline GitHub Actions automatise :

* Build de l’image Docker
* Tests avec pytest
* Déploiement Kubernetes

---

## 🔁 Reproduire le projet

```bash
git clone https://github.com/assan23/devops-project.git
cd devops-project

# Docker
docker build -t devops-flask-api ./app
docker run -p 5000:5000 devops-flask-api

# Kubernetes
kubectl apply -f k8s/

# Terraform (optionnel)
terraform init
terraform apply
```

---

## ⚠️ Sécurité

Les fichiers sensibles (clé SSH, Terraform state) ne sont pas inclus dans le repository pour des raisons de sécurité.

---

## 👨‍💻 Auteurs

* Hassan el hadi
* MERIEM BERRIMA
* Hassnae AMEJOUD
* Hajar BENTAIB
