Cloud Based Language Translation Service Project

# Cloud-Based Language Translation Service

A cloud computing mini-project built using **AWS Lambda**, **API Gateway**, **S3 Static Hosting**, and a **Public Translation API**.

---

## Features
- Translate text into multiple languages  
- Fully serverless architecture  
- API Gateway + Lambda backend  
- HTML/JS/CSS frontend  
- Uses free MyMemory translation API  

---

## Architecture

User → S3 → API Gateway → Lambda → MyMemory Translation API → Output

---

## Project Structure

backend/
├── lambda_function.py
└── requirements.txt

frontend/
├── index.html
├── script.js
└── style.css

architecture/
└── architecture_diagram.txt

README.md

yaml
Copy code

---

## How to Deploy
1. Upload frontend folder to **AWS S3**  
2. Create API Gateway (HTTP POST)  
3. Attach Lambda function  
4. Enable CORS  
5. Copy Invoke URL into `script.js`  

---

## Developer
Prakhar Soumya  
Cloud Computing Project  
