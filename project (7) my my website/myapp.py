import streamlit as st 
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", page_icon=":tade:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#-----local css---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
#---LOAD ASSETS---
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json")

#----HEADER SECTION------
with st.container():
    st.subheader("Hi, I am Mohit :wave:")
    st.title("My first website")
    st.write("Trying my first website")


#-----what I do -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write('''My first website created by python.And Strimlette.Im  learning python.''')

with right_column:
    st_lottie(lottie_coding, height=500, key="coding")
    #------projrcts------





    #-----contact---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
        
#-----email---
contact_form='''
<form action="https://formsubmit.co/jhamtanimohit173@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
    '''
    
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
    st.empty()
