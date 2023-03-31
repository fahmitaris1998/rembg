import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np
from io import BytesIO


st.title("rembg Demo")
col1, col2 = st.columns(2)
images = st.sidebar.file_uploader("Load Image", accept_multiple_files =True)
if images:
    for image in images:
        with Image.open(image) as img:
            col1.header("Original")
            col1.image(img)

            output = remove(img)
            col2.header("Extracted")
            col2.image(output)

            buf = BytesIO()
            output.save(buf, format="png")
            byte_im = buf.getvalue()
            col2.download_button(label="Download Sketch Images",data=byte_im,file_name='Pencil Sketch.jpeg')
