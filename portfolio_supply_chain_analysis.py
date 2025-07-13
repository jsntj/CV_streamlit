import streamlit as st

def show_supply_chain_analysis():
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
