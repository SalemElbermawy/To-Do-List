import streamlit as st


st.title("📝 My Fun To-Do List 🎉")


if "counter" not in st.session_state:
    st.session_state["counter"] = 0


if st.button("➕ Add New Task"):
    st.session_state["counter"] += 1


def show(ID: str):
    task = st.session_state[f"To-Do-Form{ID}"]
    date = st.session_state[f"Date-Form{ID}"]
    description = st.session_state[f"Description-Form{ID}"]
    category=st.session_state[f"Category_Of{ID}"]
    st.session_state[f"list{ID}"] = f"""
📝 Task: {task}
📅 Date: {date}
🖊️ Description: {description}
🏷️ Category: {category}
"""

def form(ID: str):
    if f"list{ID}" not in st.session_state:
        st.session_state[f"list{ID}"] = None

    with st.form(key=f"Form_{ID}", enter_to_submit=False, border=False):
        st.subheader(f"✨ Task {ID} Form")
        
        st.text_input("📝 Enter your To-Do", key=f"To-Do-Form{ID}")
        st.date_input("📅 Enter the date", key=f"Date-Form{ID}")
        st.text_area("🖊️ Enter the description", key=f"Description-Form{ID}")
        st.selectbox("Enter the Category of Your Task",key=f"Category_Of{ID}",options= ["💼 Work", "🏠 Personal", "📝 General"])

        st.form_submit_button("✅ Add your Task", on_click=show, type="primary", args=(ID,))

    st.write(st.session_state[f"list{ID}"])

for i in range(st.session_state["counter"]):
    form(str(i + 1))

C = st.button("📊 Show your tasks in the table", type="primary")

if C:
    is_exit = False
    for i in range(st.session_state["counter"]):
        id = i + 1
        if f"list{id}" in st.session_state and st.session_state[f"list{id}"]:
            is_exit = True
            break

    if is_exit:
        st.markdown("### 🎯 All Your Tasks")
        colors = ["#1b635a", "#1b635a", "#1b635a", "#1b635a", "#1b635a"]

        # Header
        cols = st.columns([1, 2, 2, 3,2])
        headers = ["#️⃣ Num", "📝 Task", "📅 Date", "🖊️ Description" , "Category"]
        for col, header in zip(cols, headers):
            col.markdown(f"<b style='font-size:16px;'>{header}</b>", unsafe_allow_html=True)

        st.markdown("---")

        for i in range(st.session_state["counter"]):
            id = str(i + 1)
            if f"list{id}" in st.session_state and st.session_state[f"list{id}"]:
                task_text = st.session_state[f"list{id}"]
                task_lines = task_text.strip().split('\n')
                task_name = task_lines[0].replace("📝 Task:", "").strip()
                task_date = task_lines[1].replace("📅 Date:", "").strip()
                task_desc = task_lines[2].replace("🖊️ Description:", "").strip()
                task_cat=task_lines[3].replace("Category:", "").strip()
                color = colors[i % len(colors)]
                cols = st.columns([1, 2, 2, 3,2])
                with cols[0]:
                    st.markdown(f'<div style="background-color:{color}; padding:12px; border-radius:8px; font-weight:bold; text-align:center;">{id}</div>', unsafe_allow_html=True)
                with cols[1]:
                    st.markdown(f'<div style="background-color:{color}; padding:12px; border-radius:8px;">{task_name} ✨</div>', unsafe_allow_html=True)
                with cols[2]:
                    st.markdown(f'<div style="background-color:{color}; padding:12px; border-radius:8px;">{task_date} 📅</div>', unsafe_allow_html=True)
                with cols[3]:
                    st.markdown(f'<div style="background-color:{color}; padding:12px; border-radius:8px;">{task_desc} 🖊️</div>', unsafe_allow_html=True)
                with cols[4]:
                    st.markdown(f'<div style="background-color:{color}; padding:12px; border-radius:8px;">{task_cat} </div>', unsafe_allow_html=True)
                st.markdown("---")
    else:
        st.warning("⚠️ You have not written any task yet!")


