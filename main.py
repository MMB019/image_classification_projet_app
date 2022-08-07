import streamlit as st
import cv2
from PIL import Image
from model_predict import predict

st.title('AgroIA')
file=st.file_uploader("Ajoute votre image ici...!",type=['jpg','png','jpeg'])
etat=['blurure','rouille','grise','sains','mais']

if file == None:
    st.text("En attendant l'image...")

else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    res=predict(image)
    classe=etat[res[0]]
    st.success(f"classe:{classe}, la precision: {res[1]}")

    html_string = "<h2 >Conseil Pratique</h2>"

    st.markdown(html_string, unsafe_allow_html=True)

    html_if="<embed src='rouille.html' width='100%' height='500px'>"
    st.markdown(html_if, unsafe_allow_html=True)

    

