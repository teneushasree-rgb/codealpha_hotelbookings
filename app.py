import streamlit as st

st.title("🎓 Student Grade Tracker")

student_name = st.text_input("Enter Student Name")
marks = st.text_area("Enter marks separated by commas")

if st.button("Calculate"):

    try:
        scores = list(map(int, marks.split(",")))

        average = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)

        st.success(f"Student: {student_name}")

        st.write(f"✅ Average Score: {average}")
        st.write(f"🏆 Highest Score: {highest}")
        st.write(f"📉 Lowest Score: {lowest}")

    except:
        st.error("Please enter valid numbers separated by commas")