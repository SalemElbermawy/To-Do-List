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
    st.header("Extract the 'task' ")
    
    user_input = st.text_area(" write what you want to do with all info like Date:", height=150)
    
    if st.button(" Click to extract "):
        if user_input:
            with st.spinner(" Wait..."):
                
                tasks = extract_tasks_local(user_input)
                
                if tasks:
                    st.success("Tasks:")
                    
                    for i, task in enumerate(tasks, 1):
                        with st.expander(f"Task: {i}"):
                            st.write(f"{task['sentence']}")
                            if task['dates']:
                                st.write(f"Date: {', '.join(task['dates'])}")
                            else:
                                st.write("*there is not dtermined Date*")
                else:
                    st.warning("There is not any Task here, Sorry.")
        else:
            st.error("Please Enter the Text!")
task_extraction_ui()