import streamlit as st
import pandas as pd

# --- Task 1: App Setup & Title ---
st.title("📊 Simple Sales Summary")
st.subheader("An interactive dashboard for non-technical managers to explore sales trends.")

# --- Task 1: Hardcoded Dataset ---
data = {
    "Product": ["Laptop", "Desk Chair", "Monitor", "Bookshelf", "Headphones", "Notebook"],
    "Category": ["Electronics", "Furniture", "Electronics", "Furniture", "Electronics", "Office"],
    "Sales": [1200, 150, 300, 450, 80, 20]
}

df = pd.DataFrame(data)

# --- Task 2: Sidebar Filter ---
# Moving the selectbox into the sidebar
st.sidebar.header("Filters")
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category:", categories)

# Filtering the data based on selection
filtered_df = df[df["Category"] == selected_category]

# --- Task 2: Display Main Content ---
st.write(f"### Showing results for: {selected_category}")

# Displaying the filtered DataFrame
st.dataframe(filtered_df, use_container_width=True)

# Displaying the line chart of Sales values
st.line_chart(filtered_df.set_index("Product")["Sales"])
