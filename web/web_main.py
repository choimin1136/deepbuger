import streamlit as st
from st_circular_progress import CircularProgress
import requests
import tempfile
import cv2
import json



st.set_page_config(layout="wide",page_title='FAKEID',page_icon='web/assets/osop_icon.png')
st.title('DEEPBUGER')
empty1, con1, empty2 = st.columns([1,8,1])

video=None

def model_predict(data):
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(data.read())
    video = open(tfile.name,'rb')
    
    file = {
        'file' : video
    }
    
    url = 'http://127.0.0.1:8000/files/'
    x = requests.post(url=url,files=file)
    response = json.loads(x.text)
    result = response['result']
    print(result)
    return result

def change_progress(result):
    color= 'red' if int(result) > 50 else'green'
    my_circular_progress.update_value(int(result))
    my_circular_progress.color=color
    
my_circular_progress=CircularProgress(
            label='Fake or Real',
            value=0,
            color="white",
            size='large')

with empty1:
    st.empty()

with con1:
    st.session_state['video']=st.file_uploader('VIDEO',type=['mp4'])
    video=st.session_state['video']

    col1, col2 = st.columns([7,3])
    with col1:
        st.text('col1')
        if video:
            data=st.video(video)
            print(type(data))
        else:
            st.video('https://youtu.be/bsrrCyn5L5I?si=ntDF2WQZBqvwev5H')


    with col2:
        result=0
        st.text('col2')
        if video:
            if st.button('분석하기',use_container_width=True):
                result = model_predict(video)
                change_progress(result)
        else:
            st.warning("분석할 영상을 입력해주세요")

        
        st.header('분석결과 : Fake')
    
        
        # my_circular_progress.st_circular_progress()
        
        my_circular_progress.st_circular_progress()
with empty2:
    st.empty()