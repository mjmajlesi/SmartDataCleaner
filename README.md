# SmartDataCleaner

A powerful, user-friendly web application for intelligent data cleaning and preprocessing. Upload your messy datasets and let SmartDataCleaner handle the heavy lifting!

## ✨ Features

- **Smart Missing Value Detection**
  - Automatically detects both explicit missing values (NaN, NULL) and hidden ones (?, "n/a", "unknown", etc.)
  - Shows detailed statistics on missing data

- **Detect and remove duplicate data**
  - Identify and handle duplicate rows to ensure data integrity

- **Handling mixed data types**
  - Detect and convert mixed data types for accurate analysis

- **Visualization**
  - Visualize missing data patterns and distributions
  - Generate summary statistics and insights from your cleaned data
  - matplotlib, seaborn, and plotly integration for powerful visualizations

  - **Data Standardization**
  - Automatic column name cleaning (lowercase, remove spaces, standardize formatting)
  - Consistent data indexing

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SmartDataCleaner.git
   cd SmartDataCleaner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Start the application**
   ```bash
   cd src
   streamlit run app.py
   ```

2. **Open in your browser**
   - The app will automatically open at `http://localhost:8501`

3. **Upload and clean your data**
   - Click the "Upload your dataset" button
   - Select your CSV, Excel, JSON, or TXT file
   - View the cleaned data preview

## 📁 Project Structure

```
SmartDataCleaner/
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── data_read.py        # Data reading utilities
│   ├── data_analyst.py     # Data analysis and cleaning functions
│   ├── titanic.csv         # Sample dataset
│   └── __pycache__/
├── test/
│   ├── test.py             # Test suite
│   └── titanic.csv
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── LICENSE                 # Project license
```

## 📦 Dependencies

- **streamlit**: Web framework for data apps
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization

See `requirements.txt` for the complete list.

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
cd test
python test.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

Future enhancements may include:
- Duplicate row detection and removal
- Outlier detection and handling
- Data type inference and conversion
- Statistical summaries and visualizations
- Export cleaned data directly from the app

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements
