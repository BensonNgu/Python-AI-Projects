import streamlit as st
import PyPDF2
import io
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ── Page & UI setup ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Critiquer",   # browser-tab title
    page_icon="📄",                     # favicon (emoji works fine)
    layout="centered"                   # center content on wide screens
)

st.title("AI Resume Critiquer")         # big page heading
st.markdown(                            # short sub-heading / instructions
    "Upload your resume and get AI-powered feedback tailored to your needs!"
)

# ── Environment & user inputs ─────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # keep secrets out of source code

uploaded_file = st.file_uploader(            # accepts PDF or plain-text résumé
    "Upload your resume (PDF or TXT)",
    type=["pdf", "txt"]
)

job_role = st.text_input(                    # lets user specify a target role
    "Enter the job role you're targeting (optional)"
)

analyze = st.button("Analyse Resume")        # click → trigger analysis logic



# ─── Helper functions ───────────────────────────────────────────────────────────

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


# ─── Main action ────────────────────────────────────────────────────────────────

def analyse_resume(resume):
    try:
        file_content = extract_text_from_file(resume)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt = f"""
        Please analyse this resume and provide constructive feedback.

        Focus on:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role or 'general job applications'}


        <RESUME>
        {file_content}
        </RESUME>


        Respond in markdown with clear section-by-section recommendations.        
        """

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert résumé reviewer with years of HR "
                        "and recruitment experience."
                    ),
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1_000
        )

        st.markdown('### Analysis Results')
        result = response.choices[0].message.content

        st.markdown(result, unsafe_allow_html=True)

        with st.expander("Copy or download this analysis"):
            st.code(result, language="markdown")   # shows Streamlit's copy icon
            st.download_button(
                label="Download as markdown file",
                data=result,
                file_name="resume_analysis.md",
                mime="text/markdown",
            )

    except Exception as e:
        st.error(f"An error occured: {str(e)}")


def fake_request(resume):
    file_content = extract_text_from_file(resume)
    if not file_content.strip():
        st.error("File does not have any readable text.")
        st.stop()

    # ── Placeholder result ──
    fake_response = (
        "### Analysis Results\n\n"
        "**Content Clarity:** 4/5  \n"
        "- Strength: Bullet points are concise.\n"
        "- Improve: Add measurable achievements.\n\n"
        "**Skills Presentation:** 3/5  \n"
        "- Group related skills together.\n\n"
        "**Experience Descriptions:** 3/5  \n"
        "- Use stronger action verbs (e.g., *orchestrated*, *engineered*)."
    )

    # Spinner closes automatically here
    st.markdown(fake_response, unsafe_allow_html=True)

    with st.expander("Copy or download this analysis"):
            st.code(fake_response, language="markdown")   # shows Streamlit's copy icon
            st.download_button(
                label="Download as markdown file",
                data=fake_response,
                file_name="resume_analysis.md",
                mime="text/markdown",
            )


if analyze:
    if not uploaded_file:
        st.warning("Please upload a file first.")
        st.stop()

    with st.spinner("Analyzing your résumé…"):
        analyse_resume(uploaded_file)

        # ── Debug / demo mode ────────────────────────────────────────────
        # To see the spinner without calling the real API:
        # 1. Comment out the line above (`analyse_resume(...)`)
        # 2. Uncomment the two lines below
        # time.sleep(3)
        # fake_request(uploaded_file)
    