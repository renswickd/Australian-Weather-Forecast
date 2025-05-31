# AUS Weather Forecast - End-to-End CI/CD Deployment to GKE

## Objective
The goal of this project is to build, deploy, and manage a weather forecasting application for Australia using an end-to-end CI/CD pipeline. The pipeline automates the process of data ingestion, model training, and deployment to a Google Kubernetes Engine (GKE) cluster. The application leverages machine learning models to provide accurate weather forecasts.

---

## Use Case
This project demonstrates:
1. **Automated Data Ingestion**: Fetches weather data from external sources and processes it for model training.
2. **Machine Learning Model Deployment**: Deploys a trained machine learning model for weather forecasting.
3. **CI/CD Workflow**: Automates the build, test, and deployment process using GitHub Actions.
4. **Scalable Deployment**: Utilizes Kubernetes for container orchestration, enabling scalability and high availability.
5. **Google Cloud Integration**: Leverages Google Cloud services such as GKE and Artifact Registry for container management and deployment.

---

## Project Workflow

### 1. Data Ingestion
- The data ingestion pipeline fetches weather data from external APIs or datasets. (Data loaded from local for demonstration)
- The pipeline processes the data and stores it in a format suitable for model training.
- The processed data is stored in a cloud storage bucket or database for further use.

### 2. Model Training
- The machine learning model is trained using the processed weather data.
- The trained model is serialized and stored in the `artifacts/model` directory.

### 3. CI/CD Pipeline
- The CI/CD pipeline automates the following steps:
  1. **Code Checkout**: Pulls the latest code from the `main` branch.
  2. **Docker Image Build and Push**: Builds a Docker image for the application and pushes it to Google Artifact Registry.
  3. **GKE Cluster Configuration**: Configures the GKE cluster for deployment.
  4. **Application Deployment**: Deploys the application to the GKE cluster using Kubernetes manifests.

---

## Setup Instructions

### Prerequisites
1. **Google Cloud Platform (GCP) Setup**:
   - A GCP project with billing enabled.
   - A GKE cluster created in the desired region.
   - An Artifact Registry repository for storing Docker images.

2. **GitHub Repository**:
   - A GitHub repository with the application code and CI/CD workflow configuration.

3. **Secrets Configuration**:
   - Add the following secrets to your GitHub repository:
     - `GCP_PROJECT_ID`: Your GCP project ID.
     - `GCP_SA_KEY`: The JSON key for your GCP service account with the necessary permissions.

4. **Kubernetes Deployment File**:
   - Ensure you have a `kubernetes-deployment.yaml` file in your repository for deploying the application to GKE.

---

### Data Ingestion Pipeline
1. **Set Up Data Sources**:
   - Configure the data ingestion script to fetch weather data from APIs or datasets.
   - Update the script with API keys or dataset paths as required.

2. **Run the Data Ingestion Script**:
   - Execute the script to fetch and process the data:
     ```bash
     python src/data_ingestion.py
     ```

3. **Verify Processed Data**:
   - Ensure the processed data is stored in the specified location (e.g., cloud storage bucket or database).

---

### CI/CD Workflow Overview
The CI/CD pipeline is defined in the `.github/workflows/deploy.yml` file. It performs the following steps:

1. **Code Checkout**:
   - Pulls the latest code from the `main` branch.

2. **Google Cloud SDK Setup**:
   - Authenticates with GCP using the service account key.
   - Configures Docker to push images to the Artifact Registry.

3. **Docker Image Build and Push**:
   - Builds a Docker image for the application.
   - Pushes the image to the Artifact Registry.

4. **GKE Cluster Configuration**:
   - Retrieves credentials for the GKE cluster.

5. **Application Deployment**:
   - Deploys the application to the GKE cluster using `kubectl`.
   - Updates the deployment with the new Docker image and monitors the rollout status.

---

### Deployment Instructions

1. **Clone the Repository**:
```bash
git clone https://github.com/your-username/aus-weather.git
cd aus-weather
```

2. **Set Up GCP**:
- Create a GKE cluster
```bash
gcloud container clusters create kb-cluster-aus-forecast --region us-central1
```
- Create an Artifact Registry repository
```bash
gcloud artifacts repositories create my-repo --repository-format=docker --location=us-central1
```

3. Configure GitHub Secrets:

Add `GCP_PROJECT_ID` and `GCP_SA_KEY` as secrets in your GitHub repository.

4. Push Code to GitHub:

Push your code to the main branch to trigger the CI/CD workflow
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

5. Monitor the Workflow:

Go to the "Actions" tab in your GitHub repository to monitor the CI/CD workflow.

6. Verify Deployment:

Check the status of the deployment in GKE
```bash
kubectl get pods
kubectl get services
```

