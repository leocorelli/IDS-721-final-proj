# Duke University IDS721 Final Project
[![Python application test with Github Actions](https://github.com/leocorelli/IDS-721-final-proj/actions/workflows/main.yml/badge.svg)](https://github.com/leocorelli/IDS-721-final-proj/actions/workflows/main.yml)

Leo Corelli and Bhargav Shetgaonkar

- [Website](https://u3fd6dambz.us-east-1.awsapprunner.com/)
- [Demo Video](https://duke.box.com/s/izob0a3mg9gotg9qo2190n8yef1xj2xu)

<p align="center">
  <img src="https://github.com/leocorelli/IDS-721-final-proj/blob/main/images/Red_Wine_picto.png" width="120" />
</p>


## What we did
In this project, we built and deployed a machine learning web microservice on AWS that predicts the quality score of red wine based on its physical attributes (such as alcohol content, pH, sulphate concentration, etc). This can be a valuable service to wine producers who desire a more scientific approach to answer the question of what makes a high quality wine. Producers can use our tool to inform/tweak their production process to change the physical attributes of their wine in order to make it higher quality. For example, producers can use our tool to see that if they decrease the alcohol content and increase the pH, then it is predicted that their wine will be rated higher quality than it currently is.

## How we did it
After both being blown away by the power of AutoML, we decided to train a model on the [kaggle red wine quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) dataset using Databricks AutoML on Azure. After setting up and running the AutoML experiment, we selected one of the top-performing models (based on validation RMSE) and went with an sklearn RandomForestRegressor. We used GitHub and GitHub Actions for our continuous integration tests and code storage, and we used AWS Elastic Container Registry (ECR) for container image storage. We used AWS App Runner (PaaS) to deploy our container from ECR, which is configured to automatically deploy the most recent container version in the ECR repo. We then performed load testing on this cloud deployed container, and verified that it can handle over 15 concurrent users with 0 failures. The response time is slower than a non-machine learning application and typical web-microservice might be due to the fact that the cheapest hardware avaialble is running our microservice (gotta save those credits), and a non-trivial machine learning model must run on the backend every time the service is called. 

## Workflow Diagram

<p align="center">
  <img src="https://github.com/leocorelli/IDS-721-final-proj/blob/main/images/workflow%20diagram.png" width="800" />
</p>

## Additional Load Testing

In our initial load testing in our demo video, we were running the ML model every time for each user. In the case below, we just swarmed the home page of our web microservice. It easily accomodates 30 concurrent users at around 500 requests per second with an average response time of 61 ms.

<p align="center">
  <img src="https://github.com/leocorelli/IDS-721-final-proj/blob/main/images/locust%20params.png" width="200" />
</p>
<p align="center">
  <img src="https://github.com/leocorelli/IDS-721-final-proj/blob/main/images/further%20results.png" width="1000" />
</p>
