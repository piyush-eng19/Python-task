from pathlib import Path

import streamlit as st
from PIL import Image


#--- PATH SETTINGS---
current_dir = Path(__file__).parent if"__file__"in locals() else Path.cwd()
css_file= current_dir /"styles"/"main.css"
resume_file= current_dir /"assets"/"cv.pdf"
profile_pic= current_dir /"assets" /"profile-pic.png"


#---GENERAL SETTINGS---
PAGE_TITLE = "Digital CV | PIYUSH SINGH"
PAGE_ICON = "🕉"
NAME = "Piyush Singh"
DESCRIPTION = """
Beginner Data Analyst,learning new languages"""
EMAIL = "piyushks1907@gmail.com"
SOCIAL_MEDIA = {
    "YouTube":"https://youtube.com/@piyushsingh-zv7yv?si=l2tR8glVsaXU2xEb",
    "SnapChat":"https://www.snapchat.com/add/onsy07?share_id=Cae6j9kw3IY&locale=en-US",
    "Facebook":"https://www.facebook.com/profile.php?id=100084339737375&mibextid=ZbWKwL",
    "GitHub":"https://github.com/piyush-eng19",
}

#Projects={}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


# --- LOAD CSS,PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)





#--- HERO SECTION ---
col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )    

st.write(":envelope:",EMAIL)



# --- SOCIAL LINES ---
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ---- EXPERIENCE AND QUALIFICATIONS----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
▶ Programming: Python (scikit-learn,pandas), SQL, VBA\n
▶ Data Visualization: MS Excel\n
▶ Database: MongoDB
"""
)

