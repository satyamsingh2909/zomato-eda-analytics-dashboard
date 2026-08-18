import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="Zomato Analytics Dashboard",
    page_icon="🍽️",
    layout="wide"
)

# ---------------- Dashboard Header ----------------

st.title("🍽️ Zomato Restaurant Analytics Dashboard")

st.markdown("""
Analyze restaurant ratings, pricing, delivery time, cuisines, 
and city-wise restaurant distribution using an interactive dashboard.
""")

# ---------------- Load & Clean Data ----------------

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    # --- Clean Rating: "New", "-", blanks -> NaN, else numeric ---
    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

    # --- Clean Average Price: "₹1,400 for one" -> 1400.0 ---
    df["Average Price"] = (
        df["Average Price"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.extract(r"(\d+\.?\d*)")[0]
    )
    df["Average Price"] = pd.to_numeric(df["Average Price"], errors="coerce")

    # --- Clean Average Delivery Time: "36 min" -> 36.0 ---
    df["Average Delivery Time"] = (
        df["Average Delivery Time"]
        .astype(str)
        .str.extract(r"(\d+\.?\d*)")[0]
    )
    df["Average Delivery Time"] = pd.to_numeric(df["Average Delivery Time"], errors="coerce")

    # --- Clean Cuisine: keep raw string but also build a list column ---
    df["Cuisine"] = df["Cuisine"].fillna("Unknown").astype(str).str.strip()
    df["Cuisine List"] = df["Cuisine"].apply(
        lambda x: [c.strip() for c in x.split(",") if c.strip()]
    )

    # --- Clean text columns ---
    df["Restaurant Name"] = df["Restaurant Name"].astype(str).str.strip()
    df["Location"] = df["Location"].astype(str).str.strip()

    return df.reset_index(drop=True)


DATA_PATH = "data/cleaned_zomato_dataset.csv"  # change to "data/zomato_dataset.csv" if using raw file
df = load_data(DATA_PATH)

filtered_df = df.copy()

# ---------------- Sidebar Filters ----------------

st.sidebar.header("🔎 Filters")

# --- Global search: matches Restaurant Name, Cuisine, or Location ---
search = st.sidebar.text_input(
    "🔍 Search (name, cuisine, or city)",
    placeholder="e.g. Pizza, Burger King, Agra..."
)

# --- City filter (multi-select) ---
all_cities = sorted(df["Location"].dropna().unique().tolist())
selected_cities = st.sidebar.multiselect(
    "Select City",
    options=all_cities,
    default=[]
)

# --- Cuisine filter (multi-select, built from exploded individual cuisines) ---
all_cuisines = sorted(
    {cuisine for cuisines in df["Cuisine List"] for cuisine in cuisines}
)
selected_cuisines = st.sidebar.multiselect(
    "Select Cuisine",
    options=all_cuisines,
    default=[]
)

# --- Rating range filter ---
min_rating, max_rating = float(df["Rating"].min(skipna=True) or 0), float(df["Rating"].max(skipna=True) or 5)
rating_range = st.sidebar.slider(
    "Rating Range",
    min_value=0.0,
    max_value=5.0,
    value=(0.0, 5.0),
    step=0.1
)

# --- Price range filter ---
price_min = int(df["Average Price"].min(skipna=True) or 0)
price_max = int(df["Average Price"].max(skipna=True) or 1000)
price_range = st.sidebar.slider(
    "Price Range (₹)",
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max)
)

include_unrated = st.sidebar.checkbox("Include restaurants with no rating", value=True)

# ---------------- Apply Filters ----------------

# Global search across name, cuisine, location
if search:
    s = search.strip().lower()
    mask = (
        filtered_df["Restaurant Name"].str.lower().str.contains(s, na=False)
        | filtered_df["Cuisine"].str.lower().str.contains(s, na=False)
        | filtered_df["Location"].str.lower().str.contains(s, na=False)
    )
    filtered_df = filtered_df[mask]

# City filter
if selected_cities:
    filtered_df = filtered_df[filtered_df["Location"].isin(selected_cities)]

# Cuisine filter: restaurant matches if it serves ANY of the selected cuisines
if selected_cuisines:
    selected_set = set(selected_cuisines)
    filtered_df = filtered_df[
        filtered_df["Cuisine List"].apply(lambda lst: bool(selected_set.intersection(lst)))
    ]

# Rating filter (optionally keep unrated restaurants)
if include_unrated:
    filtered_df = filtered_df[
        filtered_df["Rating"].isna()
        | filtered_df["Rating"].between(rating_range[0], rating_range[1])
    ]
else:
    filtered_df = filtered_df[
        filtered_df["Rating"].between(rating_range[0], rating_range[1])
    ]

# Price filter
filtered_df = filtered_df[
    filtered_df["Average Price"].between(price_range[0], price_range[1])
    | filtered_df["Average Price"].isna()
]

# ---------------- Sidebar Info + Reset ----------------

st.sidebar.markdown("---")

if st.sidebar.button("♻️ Reset Filters"):
    st.rerun()

st.sidebar.info(
    """
    🍽️ **Zomato Analytics Dashboard**

    Built using:
    - Streamlit
    - Pandas
    - Plotly
    """
)

# ---------------- KPI Cards ----------------

st.subheader("📊 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🍽 Restaurants", len(filtered_df))

with col2:
    avg_rating = filtered_df["Rating"].mean()
    st.metric(
        "⭐ Avg Rating",
        round(avg_rating, 2) if not pd.isna(avg_rating) else "N/A"
    )

with col3:
    avg_price = filtered_df["Average Price"].mean()
    st.metric(
        "💰 Avg Price",
        f"₹{round(avg_price, 0):.0f}" if not pd.isna(avg_price) else "N/A"
    )

with col4:
    avg_delivery = filtered_df["Average Delivery Time"].mean()
    st.metric(
        "🚚 Avg Delivery",
        f"{round(avg_delivery, 0):.0f} min" if not pd.isna(avg_delivery) else "N/A"
    )

# ---------------- Dataset Preview ----------------

st.divider()
st.subheader("📋 Dataset Preview")

if filtered_df.empty:
    st.warning("No restaurants match your current filters. Try widening your search or clearing filters.")
else:
    preview_cols = [
        "Restaurant Name", "Rating", "Cuisine",
        "Average Price", "Average Delivery Time", "Location"
    ]
    st.dataframe(filtered_df[preview_cols].head(20), use_container_width=True)

# ---------------- Rating Distribution ----------------

st.divider()
st.subheader("⭐ Rating Distribution")

if filtered_df["Rating"].dropna().empty:
    st.info("No rating data available for the current filters.")
else:
    fig = px.histogram(
        filtered_df.dropna(subset=["Rating"]),
        x="Rating",
        nbins=20,
        color_discrete_sequence=["orange"],
        title="Distribution of Restaurant Ratings"
    )
    fig.update_layout(xaxis_title="Rating", yaxis_title="Number of Restaurants")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Top Cities ----------------

st.divider()
st.subheader("🏙️ Top 10 Cities")

if filtered_df.empty:
    st.info("No data available for the current filters.")
else:
    city_counts = (
        filtered_df["Location"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    city_counts.columns = ["City", "Restaurants"]

    fig = px.bar(
        city_counts,
        x="City",
        y="Restaurants",
        color="Restaurants",
        text="Restaurants",
        title="Top 10 Cities"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(xaxis_title="City", yaxis_title="Number of Restaurants")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Top Cuisines ----------------

st.divider()
st.subheader("🍕 Top 10 Cuisines")

if filtered_df.empty:
    st.info("No data available for the current filters.")
else:
    cuisine_series = filtered_df["Cuisine List"].explode()
    cuisine_counts = (
        cuisine_series.value_counts()
        .head(10)
        .reset_index()
    )
    cuisine_counts.columns = ["Cuisine", "Count"]

    fig = px.bar(
        cuisine_counts,
        x="Cuisine",
        y="Count",
        color="Count",
        text="Count",
        title="Top 10 Most Popular Cuisines"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(xaxis_title="Cuisine", yaxis_title="Number of Restaurants")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Price Distribution ----------------

st.divider()
st.subheader("💰 Average Price Distribution")

if filtered_df["Average Price"].dropna().empty:
    st.info("No price data available for the current filters.")
else:
    fig = px.histogram(
        filtered_df.dropna(subset=["Average Price"]),
        x="Average Price",
        nbins=25,
        color_discrete_sequence=["green"],
        title="Average Price Distribution"
    )
    fig.update_layout(xaxis_title="Average Price (₹)", yaxis_title="Number of Restaurants")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Delivery Time Distribution ----------------

st.divider()
st.subheader("🚚 Delivery Time Distribution")

if filtered_df["Average Delivery Time"].dropna().empty:
    st.info("No delivery time data available for the current filters.")
else:
    fig = px.histogram(
        filtered_df.dropna(subset=["Average Delivery Time"]),
        x="Average Delivery Time",
        nbins=20,
        color_discrete_sequence=["red"],
        title="Delivery Time Distribution"
    )
    fig.update_layout(xaxis_title="Delivery Time (Minutes)", yaxis_title="Number of Restaurants")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Price vs Rating ----------------

st.divider()
st.subheader("⭐ Rating vs Average Price")

scatter_df = filtered_df.dropna(subset=["Average Price", "Rating"])
if scatter_df.empty:
    st.info("Not enough data to plot price vs rating for the current filters.")
else:
    fig = px.scatter(
        scatter_df,
        x="Average Price",
        y="Rating",
        color="Rating",
        hover_name="Restaurant Name",
        title="Relationship Between Price and Rating"
    )
    fig.update_layout(xaxis_title="Average Price (₹)", yaxis_title="Rating")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Download Button ----------------

st.divider()

download_cols = [
    "Restaurant Name", "Rating", "Cuisine",
    "Average Price", "Average Delivery Time", "Safety Measure", "Location"
]
download_cols = [c for c in download_cols if c in filtered_df.columns]
csv = filtered_df[download_cols].to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_zomato_data.csv",
    mime="text/csv",
    disabled=filtered_df.empty
)

# ---------------- Footer ----------------

st.divider()
st.caption(
    "Created by Satyam Kumar Singh | Zomato EDA Dashboard | 2026"
)