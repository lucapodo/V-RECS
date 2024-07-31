import streamlit as st
st.set_page_config(layout="wide")
# import chardet
# from st_aggrid import AgGrid

# import os
# import pandas as pd
# import requests
# import re
# import altair_viewer
# import altair as alt


from src.data.load import load_data
from src.style import get_css
from src.data.transform import extract_response, extract_visualization, build_prompt
from src.huggingfaces.hf import stream

st.markdown(get_css(), unsafe_allow_html=True)


if 'stream' not in st.session_state:
    st.session_state.stream = ''

if 'vis' not in st.session_state:
    st.session_state.vis = None

if 'isLoaded' not in st.session_state:
    st.session_state.isLoaded = False


def main():

    with st.sidebar:
        st.title("V-RECS demo")
        st.image("./assets/logo.png")

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

        if uploaded_file is not None:
            result = load_data(uploaded_file)

            if isinstance(result, str):
                print(result)
            else:
                dataset_, df_data = result
                st.session_state.isLoaded = True




    user_query = st.chat_input("Say something")


    if st.session_state.isLoaded:

        st.dataframe(df_data.head(1), use_container_width=True)
        st.divider()

        is_vis = False

        if user_query:

            with st.chat_message("user"):
                st.markdown(user_query)

            st.session_state.stream = ''        

            with st.chat_message("assistant"):
                assistant_placeholder = st.empty()

                for token in stream(build_prompt(user_query, dataset_)):
                    st.session_state.stream += token + ''

                    col1, col2 = assistant_placeholder.columns([1,1])

                
                    with col1:
                        if(not is_vis):
                            col1 = st.empty()
                            try: 
                                vega_lite_visualization = extract_visualization(st.session_state.stream)
                                col1.vega_lite_chart(df_data, vega_lite_visualization, use_container_width=True)
                                is_vis = True
                            except Exception:
                                pass

                    with col2:
                        try:
                            col2 = st.empty()
                            response  =  extract_response(st.session_state.stream)
                            col2.markdown(response)
                        except Exception as e:
                            print (e)
                            pass

if __name__ == '__main__':
    main()
