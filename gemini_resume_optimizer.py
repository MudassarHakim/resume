import streamlit as st
import docx2txt
import pdfplumber
import google.generativeai as genai
import io
import base64

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Gemini ATS Resume Optimizer", layout="centered")
st.title("🤖 ATS Resume Optimizer with Gemini AI")

# --- Step 1: API Key Input ---
st.header("🔐 Step 1: Enter your Gemini API Key")
api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    st.success("API Key validated!")

    # --- File Upload Section ---
    st.header("📄 Step 2: Upload Resume and Job Description")
    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload your Resume", type=["pdf", "docx", "txt"])
    with col2:
        jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])

    # --- Extract Text ---
    def extract_text(uploaded_file):
        if uploaded_file.name.endswith(".pdf"):
            with pdfplumber.open(uploaded_file) as pdf:
                return "\n".join(page.extract_text() or "" for page in pdf.pages)
        elif uploaded_file.name.endswith(".docx"):
            return docx2txt.process(uploaded_file)
        else:
            return uploaded_file.read().decode("utf-8")

    if resume_file and jd_file:
        resume_text = extract_text(resume_file)
        jd_text = extract_text(jd_file)

        st.success("📂 Files extracted successfully!")

        st.header("🤖 Step 3: Gemini Resume Optimization")

        prompt = f"""
You are a resume optimization assistant. I am applying for the following job role:

JOB DESCRIPTION:
{jd_text}

Here is my current resume:
{resume_text}

Please rewrite my resume to better match the job description using appropriate keywords, phrasing, and skills. Ensure it is still truthful and reflects the resume structure (Summary, Work Experience, Projects, Education, etc.). Return only the optimized resume text.
        """

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            optimized_resume = response.text

            st.text_area("📝 Optimized Resume", value=optimized_resume, height=500)

            # Download button
            def convert_to_downloadable_file(text):
                b64 = base64.b64encode(text.encode()).decode()
                return f'<a href="data:file/txt;base64,{b64}" download="Optimized_Resume.txt">📥 Download Optimized Resume</a>'

            st.markdown("### 📩 Step 4: Download Your Resume")
            st.markdown(convert_to_downloadable_file(optimized_resume), unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Gemini API Error: {str(e)}")

    else:
        st.info("Please upload both your resume and job description.")
else:
    st.warning("🔑 Please enter a valid Gemini API Key to continue.")
