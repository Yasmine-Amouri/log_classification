# Log Classification with Hybrid Classification Framework

## Project Overview

This project implements a **hybrid log classification system** to enhance a company's **log monitoring** process.  
It combines **Regex**, **Sentence Transformer + Logistic Regression**, and **LLM** approaches to automatically classify logs, detect anomalies, and improve responsiveness.  

**Key Advantages:**
- Detect issues proactively without waiting for customer complaints  
- Reduce time spent manually inspecting logs  
- Improve operational efficiency and security  
- Scalable for large volumes of log data  

---

## Classification Approaches

**1. Regular Expression (Regex)**  
- Applied first for high **scalability and speed**  
- Quickly classifies known patterns and reduces unnecessary computation for logs that already match rules  

**2. Sentence Transformer + Logistic Regression**  
- Uses `SentenceTransformer("all-MiniLM-L6-v2")` to generate embeddings  
- Applies Logistic Regression for classification when sufficient labeled data exists  
- Handles complex patterns efficiently  

**3. Large Language Models (LLM) via Groq**  
- Uses `llama-3.3-70b-versatile`  
- Used for logs with insufficient labeled examples or complex patterns  
- Serves as a fallback or complementary method to the other approaches  

---

## Folder Structure

**1) training/**  
- Contains the code for training models using Sentence Transformer + Logistic Regression and generating regex patterns by using clustering with DBSCAN and cosine similarity.  
- Includes a CSV file of the dataset used for training.

**2) models/**  
- Stores saved models, including Sentence Transformer embeddings and the Logistic Regression model.  

**3) resources/**  
- Contains test CSV files, generated output files.  

---

## Setup Instructions

**Install Dependencies:** Make sure you have Python installed on your system.  
Install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
