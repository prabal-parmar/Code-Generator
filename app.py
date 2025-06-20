import streamlit as st
import model

st.set_page_config(
    page_title="Code Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "saved_codes" not in st.session_state:
    st.session_state.saved_codes = []

if "show_saved" not in st.session_state:
    st.session_state.show_saved = False



st.title("Code Generator")

question = st.text_area("Type your question...")

all_languages = ["Python", "C", "C++", "Java", "Javascript", "Rust", "Go", "R"]

col1, col2, col3 = st.columns([1,8,1])

with col1:
    language = st.selectbox(
        "Select a language",
        sorted(all_languages),
        key="language",
        index=sorted(all_languages).index("Python"),
        placeholder="Python"
    )


def toggle_show():
    st.session_state.show_saved =  not st.session_state.show_saved

with col3:
    st.button("Previous Codes", on_click=toggle_show)


submit = st.button("Generate")


if submit and question:
    st.session_state.show_saved = False
    response = model.generate_response(question, language)
    
    st.write(response)

    st.session_state.saved_codes.append({"question": question, "code": response})
    

if st.session_state.show_saved:
    st.header("Your previously generated codes")
    if st.session_state.saved_codes:
        cnt = 1
        for code in st.session_state.saved_codes:
            st.subheader("Question-"  + str(cnt) + ": " + str(code["question"]))
            cnt += 1
            st.write(str(code["code"]))
    else:
        st.warning("No code generated yet")