# Streamlit App README
This repository contains a Streamlit application that serves as a demonstration of sending prediction requests to the InferenceService using KServe in a Kubeflow environment. 

The Streamlit app features five pages: Ancestry, EEG, Heart Disease, Skin Cancer, and Speech-to-Text. Each page provides specific functionalities and insights related to its respective topic.

## Usage

### Running Locally

To run the Streamlit app locally, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Access the app in your web browser at `http://localhost:8501`.

### Building and Pushing Docker Image

To build and push a Docker image containing the Streamlit app:

1. Build the Docker image:
   ```bash
   docker build -t <docker_image> .
   ```

2. Push the Docker image to your Docker registry:
   ```bash
   docker push <docker_image>
   ```

### Deploying to Kubernetes

To deploy the Streamlit app to Kubernetes:

1. Make sure you have a Kubernetes cluster set up and `kubectl` configured to communicate with it.

2. Apply the Kubernetes manifest file:
   ```bash
   kubectl apply -f k8s-streamlit.yaml
   ```

## Pages

### Ancestry

The Ancestry page allows users to check the ancestry (%) of one or more samples already present in the 1000 Genomes Project (1KGP) dataset. Additionally, users can visualize human populations worldwide to assess the differences between populations or superpopulations.

### EEG

The EEG page explores brainwave patterns generated when humans think, which can be mapped to actual intentions. In this project, we use EEG data from individuals with the aim of spelling a word by focusing solely on visual stimuli. The project's goal is to detect errors in the spelling process based on the subject's brainwaves.

### Heart Disease

The Heart Disease page allows users to assess the risk of heart disease based on various health indicators and diagnostic features. It provides interactive visualizations and predictive models.

### Skin Cancer

The Skin Cancer page focuses on classifying skin cancer types from images of common skin cancers.

### Speech-to-Text

The Speech-to-Text page enables users to transcribe spoken language into text. It utilizes speech recognition algorithms and provides real-time transcription capabilities.

## Contributors

- [Cao Hung](https://github.com/hungcao0402) - Description of contributions

