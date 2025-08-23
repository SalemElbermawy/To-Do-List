import re
from datetime import datetime, timedelta
import dateparser
import streamlit as st

def extract_tasks_local(text):
    tasks = []
    
    date_patterns = [
        r'\b(today|tomorrow|next week|next month)\b',
        r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b',
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b'
    ]
    
    task_keywords = ['need to', 'must', 'should', 'have to', 'remember to', 'don\'t forget to','want to']
    
    sentences = re.split(r'[.!?]', text)
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        is_task = any(keyword in sentence.lower() for keyword in task_keywords)
        
        if is_task:
            dates_found = []
            for pattern in date_patterns:
                dates = re.findall(pattern, sentence, re.IGNORECASE)
                dates_found.extend(dates)
            
            parsed_dates = []
            for date_str in dates_found:
                try:
                    parsed_date = dateparser.parse(date_str)
                    if parsed_date:
                        parsed_dates.append(parsed_date.strftime("%Y-%m-%d"))
                except:
                    pass
            
            tasks.append({
                "sentence": sentence,
                "dates": parsed_dates,
                "is_task": True
            })
    
    return tasks

def task_extraction_ui():
    st.markdown("## 📝 Task Extraction Tool")
    
  
    st.markdown("""
Welcome! 👋  
This tool helps you **extract tasks automatically** from your text.  
Simply write your tasks, plans, or notes below, and it will detect **what needs to be done and any associated dates**. 🔍
""")
    
    user_input = st.text_area("💬 Write your tasks here:", height=150)
    
    if st.button("🚀 Extract Tasks"):
        if user_input:
            with st.spinner("⏳ Processing..."):
                tasks = extract_tasks_local(user_input)
                
                if tasks:
                    st.success(f"✅ Found {len(tasks)} Task(s)!")
                    
                    for i, task in enumerate(tasks, 1):
                        with st.expander(f"Task {i} 🗂️"):
                            st.markdown(f"**📝 Task Description:** {task['sentence']}")
                            if task['dates']:
                                st.markdown(f"📅 **Date(s):** {', '.join(task['dates'])}")
                            else:
                                st.markdown("📅 **Date:** *Not determined*")
                else:
                    st.warning("⚠️ No tasks found. Try adding action keywords like 'need to', 'must', etc. ✨")
        else:
            st.error("❌ Please enter some text to extract tasks!")

task_extraction_ui()
