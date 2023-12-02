import streamlit as st
from st_circular_progress import CircularProgress
import requests



st.set_page_config(layout="wide",page_title='FAKEID',page_icon='web/assets/osop_icon.png')
st.title('DEEPBUGER')
empty1, con1, empty2 = st.columns([1,8,1])

video=None

def model_predict(data):
    
    print(data)
    
    

with empty1:
    st.empty()

with con1:
    st.session_state['video']=st.file_uploader('VIDEO',type=['mp4'])
    video=st.session_state['video']

    col1, col2 = st.columns([7,3])
    with col1:
        st.text('col1')
        if video:
            st.video(video)
        else:
            st.image('web/assets/not_found_video.png',use_column_width=True)


    with col2:
        st.text('col2')
        st.button('분석하기',use_container_width=True, on_click=model_predict(video))

        st.header('분석결과 : Fake')
    
        my_circular_progress=CircularProgress(
            label='Fake or Real',
            value=78,
            color='red',
            size='large')
        my_circular_progress.st_circular_progress()
    
with empty2:
    st.empty()