# Micro Price Shifter

A web-based price tracking and analysis application built with Python and Flask. The project provides a dashboard to view price information, explore historical price records, and analyze price trends.

## Features

- **Price Dashboard:** View price-related information through a web interface.
- **Price History:** Store and review historical price records using CSV data.
- **Results Page:** Display price analysis results.
- **Statistics Page:** Present price-related statistics.
- **History Page:** Explore previously recorded price data.
- **Multi-page Interface:** Navigate between Home, About, Welcome, Results, History, and Statistics pages.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- CSV

## Project Structure

```text
price_dashboard_project/
├── static/
│   └── style.css
├── templates/
│   ├── about.html
│   ├── history.html
│   ├── home.html
│   ├── result.html
│   ├── stats.html
│   └── welcome.html
├── app.py
├── price_history.csv
└── README.md
```

## Getting Started

### Prerequisites

- Python 3 installed
- pip package manager

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Anushiya-collab/Micro-Price-Shifter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Micro-Price-Shifter
   ```

3. Install Flask:

   ```bash
   pip install flask
   ```

### Run the Application

Start the Flask application:

```bash
python app.py
```

Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Future Improvements

- Add interactive price trend visualizations.
- Improve price comparison and analysis features.
- Enhance the dashboard's user interface.
- Add more detailed historical price reports.

## Author

**Anushiya**

## License

This project is available for educational and portfolio purposes. Add a formal license if you intend to specify permissions for reuse and distribution.
