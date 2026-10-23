import streamlit as st

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father's name: ")
adr = st.text_input("Enter your Text: ")
classdata = st.selectbox("Select your class: ", ("Select", 1, 2, 3, 4, 5))
##Ab hme in sare data ko ek sath get karna h, button ki help se and then we'll represent on this window 

button = st.button("Done") #Done dabate hi sara data aa jayega 
if button : #Condition true honi chaiye, aur ab classdata me jo bhi h use show karna h
    st.markdown(f"""  
    Name: {name}
    Father's Name: {fname}
    Address: {adr}
    Class: {classdata}
""") #Using f string to get the data from the user and show it on the screen



