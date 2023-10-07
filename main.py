import streamlit as st
import pandas as pd
import numpy as np



import streamlit as st

def main():
    st.title("Embedded Power BI Report")
    
    # Embed the Power BI report using the iframe code
    iframe_code = """
    <iframe title="3rd" width="1140" height="541.25" 
    src="https://app.powerbi.com/reportEmbed?reportId=3c0a1892-aa63-4137-8627-bcad46adbcd2&autoAuth=true&ctid=23035d1f-133c-44b5-b2ad-b3aef17baaa1" 
    frameborder="0" allowFullScreen="true"></iframe>
    """
    
    st.markdown(iframe_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
