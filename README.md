# 🏡 Real Estate Analytics App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

An interactive web application for real estate price prediction and market analysis, built with Streamlit.

Real-Estate-Analytics-App is an interactive web application built with Streamlit to predict property prices and analyze market trends. Leveraging machine learning, data visualization (Plotly, Seaborn, WordCloud), and cloud deployment on Streamlit Cloud, this app provides actionable insights for homebuyers and investors.

## 🌟 Features

### 📊 Interactive Dashboards
- **Price Prediction**: ML-powered property valuation based on:
  - Location (sector)
  - Property size (area in sq. ft.)
  - Bedroom count (BHK)
  - And other key features
 
### 👩‍💻Tech Stack
- **Frontend**: Streamlit (interactive web app)
- **Backend**: Python, Pandas, Scikit-learn (data processing and machine learning)
- **Visualization**: Plotly, Seaborn, Matplotlib, WordCloud
- **Deployment**: Streamlit Cloud
- **File Hosting**: GitHub (raw URLs for datasets), Google Drive (for large model files)


### 📈 Market Insights
- **Geospatial Analysis**: Price per sq. ft. heatmap by sector
- **Trend Visualization**:
  - Area vs. Price scatter plots
  - BHK distribution pie charts
  - Price comparison box plots
- **Feature Analysis**: Word clouds of popular property amenities

### 📂 Documentation
- Downloadable user guides and project notes
- Clear data source references

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/G1Codes/Real-Estate-Analytics-App.git
cd Real-Estate-Analytics-App   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run Home.py
   ```
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Online

- The app is deployed on Streamlit Cloud: https://real-estate-analytics.streamlit.app/

## Deployment

- Deployed on Streamlit Cloud for seamless access.
- Large model files (e.g., 140 MB pipeline) are hosted on Google Drive and downloaded at runtime using gdown.
- Datasets like data_viz1.csv are loaded from GitHub raw URLs to optimize deployment.

## Usage

- Home Page: Overview of the app with links to download documentation (PDFs).
- Price Predictor: Enter property details to get a price prediction.
- Analysis: Explore interactive visualizations to understand market trends.

## Skills Demonstrated

- Machine learning model development and deployment (Scikit-learn)
- Data visualization and analysis (Plotly, Seaborn, WordCloud)
- Web app development with Streamlit
- Cloud deployment and file management (Streamlit Cloud, GitHub, Google Drive)

## 🛠️ Project Structure

```
Real-Estate-Analytics-App/
├── datasets/                  # Property datasets (CSV) and model files (pickle)
├── pages/
│   ├── 2_Price_Predictor.py   # Price prediction interface
│   └── 3_Analysis.py          # Market trend visualizations
├── docs/                      # PDF documentation
├── devcontainer/              # VS Code dev container config
├── Jupyter Notebooks/         # Data exploration notebooks
├── Home.py                    # Main application entry point
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

## 🌐 Live Demo
Access the deployed app: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]( https://real-estate-analytics.streamlit.app/)

---

