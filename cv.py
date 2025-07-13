import streamlit as st

# Set page configuration
st.set_page_config(page_title="Business Intelligence Analyst CV", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Portfolio: Sales Dashboard", "Portfolio: Customer Segmentation", "Portfolio: Supply Chain Analysis"])

# Home page (CV)
if page == "Home":
    st.title("John Doe - Business Intelligence Analyst")
    
    # Contact Information
    st.header("Contact Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Email**: john.doe@example.com")
        st.write("**Phone**: (123) 456-7890")
    with col2:
        st.write("**LinkedIn**: linkedin.com/in/johndoe")
        st.write("**Location**: New York, NY")
    
    # Summary
    st.header("Summary")
    st.write("""
    Results-driven Business Intelligence Analyst with 5+ years of experience in transforming complex data into actionable insights. 
    Proficient in data visualization, statistical analysis, and predictive modeling, with a proven track record of driving business growth 
    through data-driven strategies. Adept at using tools like Tableau, Power BI, SQL, and Python to deliver impactful solutions.
    """)
    
    # Skills
    st.header("Skills")
    skills = ["SQL", "Python (Pandas, NumPy)", "Tableau", "Power BI", "Excel", "R", "Data Modeling", "ETL Processes", "Statistical Analysis", "Machine Learning"]
    col1, col2 = st.columns(2)
    for i, skill in enumerate(skills):
        if i % 2 == 0:
            col1.write(f"- {skill}")
        else:
            col2.write(f"- {skill}")
    
    # Experience
    st.header("Professional Experience")
    st.subheader("Senior BI Analyst | ABC Corporation | Jan 2022 - Present")
    st.write("""
    - Developed interactive dashboards in Tableau and Power BI, reducing report generation time by 40%.
    - Led data warehousing initiatives, improving data retrieval efficiency by 30%.
    - Collaborated with cross-functional teams to identify KPIs and deliver actionable insights.
    """)
    st.subheader("BI Analyst | XYZ Solutions | Jun 2019 - Dec 2021")
    st.write("""
    - Designed and implemented ETL pipelines using SQL and Python, streamlining data integration processes.
    - Conducted predictive analytics to forecast sales trends, achieving 95% accuracy.
    - Trained 10+ team members on data visualization best practices.
    """)
    
    # Education
    st.header("Education")
    st.write("**Master of Science in Data Analytics** | University of Example | 2017 - 2019")
    st.write("**Bachelor of Science in Statistics** | State University | 2013 - 2017")
    
    # Certifications
    st.header("Certifications")
    st.write("- Certified Business Intelligence Professional (CBIP)")
    st.write("- Tableau Desktop Specialist")
    st.write("- Microsoft Certified: Data Analyst Associate")


# Import modular portfolio pages
from portfolio_sales_dashboard import show_sales_dashboard
from portfolio_customer_segmentation import show_customer_segmentation
from portfolio_supply_chain_analysis import show_supply_chain_analysis

# Portfolio: Sales Dashboard
elif page == "Portfolio: Sales Dashboard":
    show_sales_dashboard()

# Portfolio: Customer Segmentation
elif page == "Portfolio: Customer Segmentation":
    show_customer_segmentation()

# Portfolio: Supply Chain Analysis
elif page == "Portfolio: Supply Chain Analysis":
    show_supply_chain_analysis()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2025 John Doe | Built with Streamlit")