# SmartDataCleaner

A powerful, user-friendly web application for intelligent data cleaning and preprocessing. Upload your messy datasets and let SmartDataCleaner handle the heavy lifting!

## ✨ Features

- **Smart Missing Value Detection & Imputation**
  - Automatically detects both explicit missing values (NaN, NULL) and hidden ones (?, "n/a", "unknown", etc.)
  - Shows detailed statistics on missing data
  - **KNN Imputation** for numeric columns
  - **Mode Imputation** for categorical columns
  - **Forward Fill** for date/time columns
  - Visual comparison of data before and after imputation with histograms

- **Outlier Detection**
  - **IQR Method** for numeric columns to identify statistical outliers
  - **Frequency-Based Detection** for categorical columns (rare categories < 1%)
  - Scatter plot visualization of detected outliers
  - Detailed summary statistics per column

- **Data Type Handling**
  - Detect and convert mixed data types for accurate analysis
  - Identify columns with inconsistent data types
  - Automatic type conversion with data loss reporting

- **Automatic Data Cleaning**
  - Drop rows and columns with 90% or more missing values
  - Automatic column name standardization (lowercase, remove spaces, remove parentheses)
  - Consistent data indexing

- **Data Visualization**
  - Missing data patterns using matrix visualization
  - Scatter plots for outlier detection
  - Histogram comparisons for imputation effects
  - Summary statistics and metrics
  - matplotlib and seaborn integration for powerful visualizations

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
│   ├── data_read.py        # Data reading utilities (CSV, Excel, JSON, TXT)
│   ├── data_analyst.py     # Data analysis & cleaning functions (imputation, missing values)
│   ├── data_outlier.py     # Outlier detection (IQR, frequency-based)
│   ├── clean_dtype.py      # Data type standardization and conversion
│   └── __pycache__/
├── test/
│   ├── test.py             # Test suite
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── LICENSE                 # Project license
```

## 📦 Dependencies

- **streamlit** - Web framework for data apps
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **scikit-learn** - Machine learning library (KNN Imputation)
- **missingno** - Missing data visualization
- **openpyxl** - Excel file support
- **dateparser** - Date parsing and conversion

See `requirements.txt` for the complete list with versions.

## 📂 Supported File Formats

- CSV (.csv)
- Excel (.xlsx, .xls)
- JSON (.json)
- Text (.txt)

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
cd test
python test.py
```

## 🔄 Data Cleaning Pipeline

SmartDataCleaner follows a comprehensive data cleaning workflow:

1. **Data Standardization** → Column name cleaning and normalization
2. **Data Type Detection** → Identify mixed types and inconsistencies
3. **Hidden Missing Value Detection** → Find and replace hidden missing values
4. **Automatic Filtering** → Remove rows/columns with 90%+ missing data
5. **Missing Value Imputation**
   - Numeric columns: KNN Imputation
   - Categorical columns: Mode Imputation
   - Date columns: Forward Fill + Backward Fill
6. **Outlier Detection** → Identify and report outliers using IQR and frequency analysis
7. **Export Clean Data** → Download your cleaned dataset

## � Methods & Algorithms

### Missing Value Imputation
- **KNN Imputation**: For numeric columns, uses 5 nearest neighbors to estimate missing values
- **Mode Imputation**: For categorical columns, fills with most frequent value
- **Forward Fill**: For time-series data, propagates last known value forward

### Outlier Detection
- **IQR Method** (Numeric): 
  - Identifies values outside the range [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- **Frequency-Based** (Categorical):
  - Flags categories with frequency < 1% as rare/outliers

### Data Type Detection
- **Mixed Type Detection**: Identifies columns with inconsistent data types
- **Automatic Conversion**: Converts to dominant type with loss reporting
- **Hidden Missing Value Detection**: Recognizes common missing value representations (?, n/a, null, etc.)

## ���📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

**✅ Completed Features:**
- ✅ Duplicate row detection and removal
- ✅ Outlier detection (numeric and categorical)
- ✅ Data type inference and conversion
- ✅ Missing value imputation (KNN, Mode, Forward Fill)
- ✅ Statistical visualizations

**🚧 Planned Features:**
- Advanced statistical summaries and distribution analysis
- Correlation matrix and feature relationship visualization
- Time-series data handling and forecasting
- Custom imputation strategies and algorithms
- Export cleaned data with multiple format options (CSV, Excel, JSON)
- Data quality score and profiling
- Automated data profiling and recommendations

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements
