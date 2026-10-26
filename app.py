
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Service Request Monitoring",
    layout="wide"
)

st.title("Student Service Request Monitoring")
st.write("Data Mining Decision-Support System")

page = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "Dataset",
        "Data Analysis",
        "Prediction",
        "Dashboard",
        "System Design"
    ]
)

if page == "Home":
    st.header("Home")
    st.write("Welcome to the monitoring system.")

elif page == "Dataset":
    st.header("Dataset Upload")
    file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if file is not None:
        df = pd.read_csv(file)
        st.subheader("Dataset Preview")
        st.dataframe(df.head(20))
        st.write("Number of rows:", len(df))
        st.write("Number of columns:", len(df.columns))
        st.subheader("Missing Values")
        st.write(df.isnull().sum())
        st.write("Duplicate rows:", int(df.duplicated().sum()))

elif page == "Data Analysis":
    st.header("Data Analysis")
    st.info("Statistical analysis and charts will be added here.")

elif page == "Prediction":
    st.header("Prediction")
    st.warning("Your trained midterm model must be connected here.")

elif page == "Dashboard":
    st.header("Dashboard")
    st.info("Dashboard metrics will be added here.")

elif page == "System Design":
    st.header("System Design")
    st.write("The system supports staff review of student service requests.")
  
