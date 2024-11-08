import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

label1 = st.text_input(label="", placeholder="Add new todo...", key="new_todo")
