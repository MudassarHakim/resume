Here’s a polished, professional `README.md` for your **Gemini-Powered ATS Resume Optimizer** deployed via Streamlit.

* * *

📄 Gemini-Powered ATS Resume Optimizer
--------------------------------------

Optimize your resume using **Google Gemini Pro** to match any job description — and boost your chances of passing Applicant Tracking Systems (ATS)!

<p align="center"> <img src="https://img.shields.io/badge/Powered%20by-Gemini%20Pro-blueviolet?style=for-the-badge" /> <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?style=for-the-badge" /> </p>

* * *

### 🚀 Live Demo

👉 [Launch App](https://resume-mudasar-hakim.streamlit.app)

* * *

### 📌 Features

*   🔐 **Gemini API Key Input** for secure resume optimization
    
*   📄 Upload your **resume** and **job description**
    
*   🤖 Resume rewritten using Gemini Pro with ATS-friendly keywords
    
*   ✅ Download your optimized resume
    
*   📊 See match % and missing keywords (optionally extendable)
    
*   ⚡ Lightweight, fast, and privacy-first (no data stored)
    

* * *

### 🧠 How It Works

1.  **User enters Gemini API key** from Google AI Studio
    
2.  Upload your resume (PDF/DOCX/TXT)
    
3.  Upload the job description
    
4.  Gemini rewrites the resume using job-specific phrasing & keywords
    
5.  Download the enhanced resume
    

* * *

### 📦 Installation (Local)

Clone this repo and run it locally:

`git clone https://github.com/yourusername/resume.git cd resume
pip install -r requirements.txt
streamlit run gemini_resume_optimizer.py` 

* * *

### 📁 Project Structure

`resume/
│
├── gemini_resume_optimizer.py # Streamlit app source ├── requirements.txt # Required Python packages └── README.md # This file` 

* * *

### 🧾 Requirements

See `requirements.txt`:

`streamlit==1.35.0
pdfplumber==0.10.3
docx2txt==0.8
google-generativeai==0.4.1
scikit-learn==1.5.0` 

Install with:

`pip install -r requirements.txt` 

* * *

### 🔑 Get Your Gemini API Key

1.  Go to Google AI Studio
    
2.  Generate a new API Key
    
3.  Paste it into the app when prompted (never stored)
    


* * *

### 📃 License

MIT License. Use freely, but don’t forget to give credit!

* * *
