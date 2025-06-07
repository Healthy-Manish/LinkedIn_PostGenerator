import streamlit as st

from few_shots import FewShotPosts
from post_generator import generate_post
lengths = ["Short","Medium","Long"]
language = ["Hinglish","English"]
def main():
    st.title("LinkedIn Post Generator: ft.Healthy_Manish")
    col1,col2,col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title",options=fs.unique_tags)
    with col2:
        selected_length = st.selectbox("Length",options = lengths )
    with col3:
        selected_language = st.selectbox("Language",options = language)
    if st.button("Generate"):
        post =generate_post(selected_length,selected_language,selected_tag)

        st.write(f"Generating posts for {selected_tag,selected_language,selected_length}..... :D")
        st.write(post)



if __name__ == "__main__":
    main()