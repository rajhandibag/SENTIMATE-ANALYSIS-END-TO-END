# 🚀 End-to-End Sentiment Analysis Project (MLOps + Cloud + Monitoring)

## 📌 Overview

This project is a **complete end-to-end sentiment analysis system** built with modern **MLOps practices**. It covers everything from data processing to deployment, monitoring, and scaling on cloud infrastructure.

The project demonstrates real-world production skills including:

* Model training & tracking
* CI/CD pipelines
* Containerization (Docker)
* Kubernetes deployment (EKS)
* Monitoring using Prometheus & Grafana

---

## 🧠 Tech Stack

* **Language**: Python 3.10
* **ML Tools**: Scikit-learn, MLflow
* **Experiment Tracking**: Dagshub + MLflow
* **Pipeline**: DVC
* **Backend**: Flask
* **Containerization**: Docker
* **Cloud**: AWS (S3, ECR, EKS, EC2)
* **CI/CD**: GitHub Actions
* **Monitoring**: Prometheus + Grafana

---

## 📂 Project Structure

```
├── data/
├── src/
│   ├── data/
│   ├── model/
│   ├── logger/
├── flask_app/
├── tests/
├── scripts/
├── dvc.yaml
├── params.yaml
├── Dockerfile
├── .github/workflows/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Environment Setup

```bash
conda create -n atlas python=3.10
conda activate atlas
pip install cookiecutter
```

Create project structure:

```bash
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```

---

### 2️⃣ MLflow + Dagshub Setup

* Connect GitHub repo to Dagshub
* Copy MLflow tracking URI
* Install dependencies:

```bash
pip install dagshub mlflow
```

---

### 3️⃣ DVC Pipeline Setup

```bash
dvc init
dvc remote add -d mylocal local_s3
```

Run pipeline:

```bash
dvc repro
dvc status
```

---

### 4️⃣ AWS S3 Integration

```bash
pip install dvc[s3] awscli
aws configure
dvc remote add -d myremote s3://<bucket-name>
```

---

### 5️⃣ Flask App

```bash
pip install flask
python app.py
```

Push artifacts:

```bash
dvc push
```

---

### 6️⃣ CI/CD Setup

* Add GitHub Actions workflow
* Add secrets:

  * AWS_ACCESS_KEY_ID
  * AWS_SECRET_ACCESS_KEY
  * DAGSHUB_TOKEN

---

## 🐳 Docker Setup

Build image:

```bash
docker build -t capstone-app:latest .
```

Run container:

```bash
docker run -p 8888:5000 capstone-app:latest
```

With environment variable:

```bash
docker run -p 8888:5000 -e CAPSTONE_TEST=<token> capstone-app:latest
```

---

## ☁️ AWS Deployment (ECR + EKS)

### Push to ECR

* Create repository
* Push Docker image via CI/CD

---

### Create EKS Cluster

```bash
eksctl create cluster \
--name flask-app-cluster \
--region us-east-1 \
--nodegroup-name flask-app-nodes \
--node-type t3.small
```

Update kubeconfig:

```bash
aws eks update-kubeconfig --region us-east-1 --name flask-app-cluster
```

---

### Deploy Application

```bash
kubectl get nodes
kubectl get pods
kubectl get svc
```

Access service:

```bash
curl http://<external-ip>:5000
```

---

## 📊 Monitoring Setup

### 🔍 Prometheus

* Installed on EC2 instance
* Scrapes Flask app metrics

Run:

```bash
prometheus --config.file=/etc/prometheus/prometheus.yml
```

---

### 📈 Grafana

* Installed on EC2 instance
* Connected to Prometheus

Access:

```
http://<ec2-ip>:3000
```

Default login:

```
username: admin
password: admin
```

---

## 🔥 Key Features

✅ End-to-End ML Pipeline
✅ Experiment Tracking with MLflow
✅ Data Versioning with DVC
✅ CI/CD Automation
✅ Dockerized Application
✅ Kubernetes Deployment (EKS)
✅ Real-time Monitoring (Prometheus + Grafana)

---

## 📌 What I Learned

* Building production-ready ML systems
* Managing pipelines with DVC
* Containerization & orchestration
* AWS cloud deployment (ECR, EKS, EC2)
* Monitoring and observability tools
* CI/CD best practices

---

## 🚀 Future Improvements

* Add authentication layer
* Improve model performance
* Add frontend UI
* Auto-scaling in Kubernetes
* Advanced alerting in Grafana

---

## 👨‍💻 Author

**Raj Handibag**
Aspiring ML Engineer | MLOps Enthusiast

---

⭐ If you found this project helpful, feel free to star the repo!
