# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the app layout with a colorful theme
st.markdown(
    """
    <style>
        .main {background-color: #f3f4f6;}
        h1 {color: #2f4f4f;}
        .header, .footer {background-color: #4682b4; color: white; padding: 10px 0; text-align: center; font-size: 20px;}
        .section-header {color: #4682b4; font-size: 24px; font-weight: bold; margin-top: 20px;}
        .data-preview, .feedback-form {background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin-top: 15px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown("<div class='header'>🌟 Business Dashboard 🌟</div>", unsafe_allow_html=True)
st.write("This colorful dashboard provides insights into sales, customer demographics, and product performance. Upload your data to get started.")

# Data Input
st.markdown("<div class='section-header'>Upload Business Data</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📁 Choose a CSV File", type="csv")

# App Body - Display Data Insights
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.markdown("<div class='data-preview'><b>Preview of the Uploaded Data:</b></div>", unsafe_allow_html=True)
    st.write(data.head())

    # Sales Insights
    st.markdown("<div class='section-header'>📈 Sales Insights</div>", unsafe_allow_html=True)
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        st.write("Sales Over Time")
        fig = px.line(data, x='sales_date', y='sales_amount', title='Sales Over Time', template="plotly_dark")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # Customer Segmentation by Region
    st.markdown("<div class='section-header'>🌍 Customer Segmentation</div>", unsafe_allow_html=True)
    if 'region' in data.columns and 'sales_amount' in data.columns:
        fig = px.pie(data, names="region", values="sales_amount", title="Customer Segmentation by Region", template="plotly_dark")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has a 'region' column for customer segmentation.")

    # Product Analysis
    st.markdown("<div class='section-header'>📊 Product Analysis</div>", unsafe_allow_html=True)
    if 'product' in data.columns and 'sales_amount' in data.columns:
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount')
        fig = px.bar(top_products_df, x=top_products_df.index, y='sales_amount', title="Top Products By Sales", template="plotly_dark")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # Feedback Form
    st.markdown("<div class='section-header'>💬 Feedback (Your Opinion Counts)</div>", unsafe_allow_html=True)
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback.")

# Footer
st.markdown("<div class='footer'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    pass
