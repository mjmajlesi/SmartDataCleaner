# SmartDataCleaner

A powerful, user-friendly web application for intelligent data cleaning and preprocessing. Upload your messy datasets and let SmartDataCleaner handle the heavy lifting!

## ✨ Features

- **Smart Missing Value Detection**
  - Automatically detects both explicit missing values (NaN, NULL) and hidden ones (?, "n/a", "unknown", etc.)
  - Shows detailed statistics on missing data

- **Data Standardization**
  - Automatic column name cleaning (lowercase, remove spaces, standardize formatting)
  - Consistent data indexing

- **Multi-Format Support**
  - CSV files
  - Excel files (XLSX, XLS)
  - JSON files
  - Tab-separated text files (TXT)

- **Interactive Web Interface**
  - Built with Streamlit for a responsive, modern UI
  - Real-time data preview
  - Comprehensive missing value report

- **Data Quality Insights**
  - View data previews instantly
  - Track missing value percentages
  - Identify data quality issues at a glance

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
   - Check the missing values report

## 📊 How It Works

### Data Processing Pipeline

```
Upload File → Read Data → Standardize Columns → Detect Hidden Values → Display Results
```

### Data Standardization

The application automatically:
- Converts column names to lowercase
- Removes extra whitespace
- Replaces spaces with underscores
- Removes parentheses from column names
- Starts row indexing from 1

### Missing Value Detection

Detects and replaces hidden missing values represented as:
- `?`, `n/a`, `NA`, `null`, `none`, `-`, `--`, `undefined`, `unknown`, `missing`
- Empty strings and spaces

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
- **openpyxl**: Excel file support

See `requirements.txt` for the complete list.

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
cd test
python test.py
```

## 🔧 Configuration

The application uses sensible defaults for all settings. No additional configuration is required to get started!

## 🐛 Known Limitations

- Maximum file size depends on available system memory
- Very large datasets may require additional processing time

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Example Use Cases

- **Data Scientists**: Prepare datasets for machine learning models
- **Business Analysts**: Clean and normalize business data
- **Researchers**: Process survey and experimental data
- **Content Creators**: Prepare datasets for analysis and visualization

## 🎯 Roadmap

Future enhancements may include:
- Duplicate row detection and removal
- Outlier detection and handling
- Data type inference and conversion
- Statistical summaries and visualizations
- Export cleaned data directly from the app

## 📧 Support

For questions, issues, or feature requests, please open an issue on the GitHub repository.

---

**Happy Data Cleaning!** 🎉