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

# Portfolio: Sales Dashboard
elif page == "Portfolio: Sales Dashboard":
    st.title("Portfolio: Sales Dashboard")
    st.header("Project Overview")
    st.write("""
    Developed an interactive sales dashboard for a retail client to monitor key performance indicators and sales trends.
    """)
    st.header("Objectives")
    st.write("- Provide real-time insights into sales performance.")
    st.write("- Enable regional managers to identify underperforming products.")
    st.write("- Improve decision-making with drill-down capabilities.")
    st.header("Tools Used")
    st.write("- **Tableau**: For dashboard creation and visualization.")
    st.write("- **SQL**: For data extraction and transformation.")
    st.write("- **Python**: For data preprocessing.")
    st.header("Outcomes")
    st.write("- Reduced reporting time by 50%.")
    st.write("- Increased sales in underperforming regions by 15% through targeted strategies.")
    st.write("- Enhanced user adoption with intuitive interface design.")

# Portfolio: Customer Segmentation
elif page == "Portfolio: Customer Segmentation":
    st.title("Portfolio: Customer Segmentation")
    st.header("Project Overview")
    st.write("""
    Conducted customer segmentation analysis for an e-commerce company to optimize marketing strategies.
    """)
    st.header("Objectives")
    st.write("- Identify distinct customer groups based on purchasing behavior.")
    st.write("- Tailor marketing campaigns to specific segments.")
    st.header("Tools Used")
    st.write("- **Python (Pandas, Scikit-learn)**: For clustering and data analysis.")
    st.write("- **SQL**: For querying customer data.")
    st.write("- **Power BI**: For visualizing segment characteristics.")
    st.header("Outcomes")
    st.write("- Improved campaign ROI by 25% through targeted marketing.")
    st.write("- Identified 5 distinct customer segments, enabling personalized promotions.")
    st.write("- Reduced customer churn by 10% with segment-specific retention strategies.")

# Portfolio: Supply Chain Analysis
elif page == "Portfolio: Supply Chain Analysis":
    st.title("Portfolio: Supply Chain Analysis")
    st.header("Project Overview")
    st.write("""
    Analyzed supply chain data to optimize inventory management and reduce operational costs for a manufacturing firm.
    """)
    st.header("Objectives")
    st.write("- Identify bottlenecks in the supply chain.")
    st.write("- Optimize inventory levels to minimize stockouts and overstock.")
    st.header("Tools Used")
    st.write("- **SQL**: For data extraction and aggregation.")
    st.write("- **Python (Pandas, NumPy)**: For statistical analysis.")
    st.write("- **Tableau**: For visualizing supply chain KPIs.")
    st.header("Outcomes")
    st.write("- Reduced inventory holding costs by 20%.")
    st.write("- Decreased stockouts by 30% through improved demand forecasting.")
    st.write("- Streamlined supplier evaluation process, saving 15 hours per month.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2025 John Doe | Built with Streamlit")