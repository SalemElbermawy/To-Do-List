import streamlit as st

st.title("To-Do📝")

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

if st.button("Add New Task ➕"):
    st.session_state["counter"] += 1

def show(ID:str):
    task=st.session_state[f"To-Do-Form{ID}"]
    date=st.session_state[f"Date-Form{ID}"]
    description=st.session_state[f"Description-Form{ID}"]
    st.session_state[f"list{ID}"]=f"""
    Task: {task}  
    Date: {date}     
    Description: {description}
"""

def form(ID:str):
    if f"list{ID}" not in st.session_state:
        st.session_state[f"list{ID}"]=None
    with st.form(key=f"Form_{ID}",enter_to_submit=False,border=False):
        st.title(f"Task \{ID}")

        st.text_input("enter your To-Do",key=f"To-Do-Form{ID}")
        st.date_input("enter the date",key=f"Date-Form{ID}")
        st.text_area("enter the description",key=f"Description-Form{ID}")

        st.form_submit_button("Add your Task ✨",on_click=show,type="primary",args=(ID,))

    st.write(st.session_state[f"list{ID}"])

for i in range(st.session_state["counter"]):
    form(str(i+1))

C=st.button("show your tasks in the table",type="primary")

if C:
    is_exit=False
    for i in range (st.session_state["counter"]):
        id=i+1
        if f"list{id}" in st.session_state and st.session_state[f"list{id}"]:
            is_exit=True
            break
    if is_exit:
        st.markdown("All Your Tasks")
        cols=st.columns([1,0.9,1, 1])
        with cols[0]:
            st.markdown("Num")
        with cols[1]:
            st.markdown("Task")
        with cols[2]:
            st.markdown("Date")
        with cols[3]:
            st.markdown("Description")
        
        colors = ["#e6f7ff", "#f0f9eb", "#fef7ec", "#fceff3", "#e6f7ff"]

        for i in range (st.session_state["counter"]):
            id=str(i+1)
            if f"list{id}" in st.session_state and st.session_state[f"list{id}"]:
                task_text = st.session_state[f"list{id}"]
                task_lines = task_text.strip().split('\n')
                
                task_name = task_lines[0].replace("Task:", "").strip()
                task_date = task_lines[1].replace("Date:", "").strip()
                task_desc = task_lines[2].replace("Description:", "").strip()
                color = colors[i % len(colors)]
                cols = st.columns([1, 2, 2, 3])
                with cols[0]:
                    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">{id}</div>', 
                               unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">{task_name}</div>', 
                               unsafe_allow_html=True)
                with cols[2]:
                    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">{task_date}</div>', 
                               unsafe_allow_html=True)
                with cols[3]:
                    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px;">{task_desc}</div>', 
                               unsafe_allow_html=True)
                
                st.markdown("---")
    


    else:
        st.warning("You have not written any code else")


    





