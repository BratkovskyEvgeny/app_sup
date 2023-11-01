import streamlit as st
from streamlit_extras.let_it_rain import rain
from typing import Union
from PIL import Image
import time
from streamlit_player import st_player


    
    st.image('1.JPEG',width=710)
    st.markdown("<h1 style='text-align: center; '>Благодарность</h1>", unsafe_allow_html = True)
    st.balloons()
    st.write("От всех обучающихся секретам Apache Superset выражаю благодарность за этот курс !!! ")
    
    st_player("https://www.youtube.com/watch?v=MdnE-7IpaD8")
    

    
    if st.button("Что дальше?"):
        
       
        st.write('Дальше - зима и время клепать дашборды, как пирожки :sunglasses:.')
        time.sleep(2.5)
        
        
        st.snow()
        time.sleep(3.5)
        st_player("https://soundcloud.com/user-854788030/paul-hertzog-preparation-mp3")
        
        
    