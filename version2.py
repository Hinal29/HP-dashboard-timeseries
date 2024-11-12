# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# 1.0 Title and Introduction with colorful text
st.markdown("<h1 style='text-align: center; color: darkblue;'>🌟 Business Dashboard 🌟</h1>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #808080;">
    <p>This dashboard provides insights into sales, customer demographics, and product performance. 
    Upload your data to get started.</p>
</div>
""", unsafe_allow_html=True)

# 2.0 Data Input Section
st.markdown("<h2 style='color: teal;'>📂 Upload Business Data</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a CSV File", type="csv", accept_multiple_files=False)

# 3.0 App Body 
# What Happens Once Data Is Loaded?
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.markdown("<h3 style='color: #3CB371;'>📄 Preview of the Uploaded Data:</h3>", unsafe_allow_html=True)
    st.write(data.head())

    # * Sales insights
    st.markdown("<h2 style='color: darkorange;'>📊 Sales Insights</h2>", unsafe_allow_html=True)
    if 'sales_date' in data.columns and 'sales_amount' in data.columns: 
        st.markdown("<h4 style='color: #FF6347;'>Sales Over Time</h4>", unsafe_allow_html=True)
        fig = px.line(data, x='sales_date', y='sales_amount', title='Sales Over Time')
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # * Customer Segmentation by Region
    st.markdown("<h2 style='color: purple;'>🌍 Customer Segmentation</h2>", unsafe_allow_html=True)
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.markdown("<h4 style='color: #4B0082;'>Customer Segmentation by Region</h4>", unsafe_allow_html=True)
        fig = px.pie(data, names="region", values='sales_amount', title="Customer Segmentation by Region")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has a 'region' column for customer segmentation.")

    # * Product Analysis
    st.markdown("<h2 style='color: #FF4500;'>📦 Product Analysis</h2>", unsafe_allow_html=True)
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.markdown("<h4 style='color: #8B0000;'>Top Products by Sales</h4>", unsafe_allow_html=True)
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount')
        fig = px.bar(top_products_df, x=top_products_df.index, y='sales_amount', title="Top Products By Sales")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # * Feedback Form
    st.markdown("<h2 style='color: #1E90FF;'>💬 Feedback (Your Opinion Counts)</h2>", unsafe_allow_html=True)
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success('✅ Thank you for your feedback!')

# 4.0 Footer
st.write("---")
st.markdown("<p style='text-align: center; color: #808080;'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</p>", unsafe_allow_html=True)

if _name_ == "_main_":
    pass
