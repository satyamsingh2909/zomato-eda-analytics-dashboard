# 🍽️ Zomato EDA & Analytics Dashboard

<p align="center">
  <strong>Interactive Exploratory Data Analysis of 44,000+ Restaurant Records</strong>
</p>

<p align="center">
  <a href="https://zomato-eda-analytics-dashboard-hk.streamlit.app/">
    🚀 <strong>Live Demo</strong>
  </a>
</p>

---

## 📌 Overview

The **Zomato EDA & Analytics Dashboard** is an interactive data analysis project built using **Python, Pandas, Plotly, and Streamlit**.

The project performs Exploratory Data Analysis (EDA) on a dataset containing **44,000+ restaurant records** to identify patterns and trends related to:

* ⭐ Restaurant ratings
* 🍽️ Cuisines
* 💰 Pricing
* 🚚 Delivery time
* 📍 Locations
* 🏪 Restaurant characteristics
* 📊 Distribution and relationships between different variables

The analysis was transformed into an interactive **Streamlit web dashboard**, allowing users to explore the data dynamically through filters, searches, and interactive visualizations.

### 🚀 Live Dashboard

**[👉 Open the Zomato Analytics Dashboard](https://zomato-eda-analytics-dashboard-hk.streamlit.app/)**

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Perform data cleaning and preprocessing on a large restaurant dataset.
2. Explore important patterns and trends using Exploratory Data Analysis.
3. Analyze restaurant ratings and their distribution.
4. Study cuisine popularity and restaurant distribution.
5. Investigate pricing patterns across restaurants and locations.
6. Analyze delivery-time patterns.
7. Build meaningful and interactive data visualizations.
8. Develop a user-friendly analytics dashboard using Streamlit.
9. Deploy the dashboard online for public access.

---

## 📊 Dataset

The project uses a restaurant dataset containing **44,000+ records**.

The dataset contains information related to restaurants, including attributes such as:

| Category               | Examples                         |
| ---------------------- | -------------------------------- |
| Restaurant Information | Restaurant name, location        |
| Ratings                | Restaurant rating                |
| Cuisine                | Cuisine types                    |
| Pricing                | Price-related information        |
| Delivery               | Delivery-time information        |
| Location               | City / area information          |
| Restaurant Features    | Additional restaurant attributes |

### Dataset Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Data Transformation
     ↓
Exploratory Data Analysis
     ↓
Visualization
     ↓
Interactive Streamlit Dashboard
```

---

## 🔍 Exploratory Data Analysis

The project investigates several important dimensions of the restaurant dataset.

### ⭐ Rating Analysis

Analysis of:

* Restaurant rating distribution
* Highly rated restaurants
* Lower-rated restaurants
* Rating patterns across different categories
* Relationship between ratings and other restaurant attributes

### 🍽️ Cuisine Analysis

Analysis of:

* Most common cuisines
* Cuisine popularity
* Number of restaurants by cuisine
* Cuisine-related rating patterns

### 💰 Pricing Analysis

Analysis of:

* Restaurant pricing distribution
* Average pricing
* Pricing across different locations
* Relationship between pricing and restaurant ratings

### 🚚 Delivery Analysis

Analysis of:

* Delivery-time distribution
* Average delivery time
* Delivery patterns across restaurants
* Relationship between delivery time and other attributes

### 📍 Location Analysis

Analysis of:

* Restaurant distribution by location
* Restaurant concentration across different areas
* Rating patterns across locations
* Pricing differences across locations

---

## 📈 Interactive Dashboard

The final analysis is presented through an interactive **Streamlit dashboard**.

### Dashboard Features

* 🎛️ Interactive filters
* 🔎 Restaurant search
* ⭐ Rating analysis
* 🍽️ Cuisine analysis
* 💰 Pricing analysis
* 🚚 Delivery-time analysis
* 📍 Location-based analysis
* 📊 Interactive Plotly charts
* 📋 Data exploration

Users can change filters and explore different parts of the dataset without modifying the underlying code.

---

## 🛠️ Technology Stack

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
| **Python**           | Core programming language           |
| **Pandas**           | Data manipulation and analysis      |
| **NumPy**            | Numerical operations                |
| **Plotly**           | Interactive data visualization      |
| **Streamlit**        | Interactive web dashboard           |
| **Jupyter Notebook** | Exploratory data analysis           |
| **Git & GitHub**     | Version control and project hosting |

---

## 📁 Project Structure

```text
zomato-eda-analytics-dashboard/
│
├── data/
│   ├── zomato_dataset.csv
│   └── cleaned_zomato_dataset.csv
│
├── images/
│
├── notebooks/
│   └── zomato_analysis.ipynb
│
├── src/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

**`app.py`**
Main Streamlit application containing the interactive dashboard.

**`data/`**
Contains the raw and cleaned datasets used for analysis.

**`notebooks/`**
Contains Jupyter Notebook files used for exploratory analysis and experimentation.

**`src/`**
Contains supporting source code and analysis components.

**`requirements.txt`**
Contains the Python dependencies required to run the project.

**`.gitignore`**
Specifies files and folders that should not be uploaded to GitHub.

---

## ⚙️ Run the Project Locally

If you want to run the dashboard on your own computer:

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/zomato-eda-analytics-dashboard.git
```

### 2. Navigate to the project directory

```bash
cd zomato-eda-analytics-dashboard
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

---

## 🌐 Live Deployment

The dashboard is deployed using **Streamlit Community Cloud**.

### 🚀 Live Demo

**[Open the Zomato EDA & Analytics Dashboard](https://zomato-eda-analytics-dashboard-hk.streamlit.app/)**

The deployed application allows users to interact with the dashboard directly from a web browser without installing Python or any project dependencies.

---

## 💡 Key Skills Demonstrated

This project demonstrates practical experience with:

* Data cleaning
* Data preprocessing
* Exploratory Data Analysis
* Statistical exploration
* Data visualization
* Interactive dashboards
* Python programming
* Pandas
* NumPy
* Plotly
* Streamlit
* Jupyter Notebook
* Git
* GitHub
* Application deployment

---

## 📚 What I Learned

Through this project, I gained practical experience in taking a dataset from the **raw data stage to a deployed analytics application**.

The complete workflow involved:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Preprocessing
      ↓
EDA
      ↓
Visualization
      ↓
Dashboard Development
      ↓
Deployment
```

This helped me understand how data analysis can be transformed into an interactive application rather than remaining only inside a Jupyter Notebook.

---

## 🚀 Future Improvements

Potential improvements for future versions include:

* [ ] Add advanced statistical analysis
* [ ] Add geographic/map-based visualizations
* [ ] Add recommendation functionality
* [ ] Add predictive restaurant rating models
* [ ] Add cuisine recommendation system
* [ ] Add advanced filtering and comparison features
* [ ] Improve dashboard UI/UX
* [ ] Add automated data refresh
* [ ] Add machine learning-based insights

---

## 👨‍💻 Author

### Satyam Kumar Singh

**B.Tech — Computer Science & Engineering (AI & ML)**

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Competitive Programming
* Software Engineering

---

## ⭐ Project Links

| Resource                 | Link                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------- |
| 🚀 **Live Dashboard**    | [Open Dashboard](https://zomato-eda-analytics-dashboard-hk.streamlit.app/)          |
| 💻 **GitHub Repository** | [View Source Code](https://github.com/satyamsingh2909/zomato-eda-analytics-dashboard) |

---

## ⭐ If you found this project useful

Feel free to **star ⭐ the repository** and explore the dashboard.

<p align="center">
  <strong>Built with Python 🐍 • Pandas • Plotly • Streamlit</strong>
</p>
