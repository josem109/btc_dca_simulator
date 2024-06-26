# BTC DCA Simulator

This project simulates the Dollar-Cost Averaging (DCA) strategy for Bitcoin (BTC) investment. It allows users to input a date range and a monthly investment amount, then calculates the total investment, current value, and profit or loss over the selected period. The simulation uses historical BTC price data from a CSV file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [File Structure](#file-structure)
- [Data](#data)
- [Algorithm](#algorithm)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/josem109/btc_dca_simulator.git
   cd btc_dca_simulator

   ```

2. **Create a virtual environment (optional but recommended)**:

   ```python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

   ```

3. **Install the required packages**:

   ```pip install -r requirements.txt

   ```

## Usage

1. **Run the Streamlit application**:

   ```streamlit run btc_dca_simulator.py

   ```

2. **Interact with the application**:

   Input the start date and end date for the investment period.
   Enter the monthly investment amount in USD.
   Optionally, set a profit target percentage for an exit strategy.
   Click the "Calculate" button to see the results.

3. **View the results**:

   Total invested amount.
   Current value of the investment.
   Profit or loss.
   Number of months in profit and loss.
   Exit date if the profit target is achieved.
   Graphs showing investment vs. current value over time and monthly profit/loss.

## Features

    Dollar-Cost Averaging Simulation: Simulates regular investments in BTC over a selected period.
    Profit Target Exit Strategy: Allows setting a profit target to automatically determine an exit date.
    Detailed Results: Displays total investment, current value, profit/loss, and monthly breakdown.
    Visualizations: Includes graphs to visualize investment performance over time.

## File Structure

    btc_dca_simulator/

│
├── data/
│ └── Bitcoin Historical Data.csv
│
├── env/ # Virtual environment directory (optional)
│
├── btc_dca_simulator.py # Main Streamlit application
│
├── README.md # Project documentation
│
└── requirements.txt # Required Python packages

## Data

    The historical BTC price data should be placed in the data directory with the filename Bitcoin Historical Data.csv. The CSV file should have the following columns:

    Date: Date of the price data.
    Price: Closing price of BTC.
    Open, High, Low, Vol., Change %: Other price-related data (not used in the simulation).

## Algorithm

    The DCA simulation algorithm:

    Loads historical BTC price data from the CSV file.
    Filters the data for the selected date range.
    Iteratively calculates the total investment and BTC accumulated for each month.
    Computes the current value of the investment based on the latest BTC price.
    Optionally, checks if the profit target is achieved to determine the exit date.

## Future Enhancements

    Additional Exit Strategies: Implement other exit strategies such as stop loss or time-based exits.
    Advanced Visualizations: Add more interactive and detailed visualizations.
    Performance Metrics: Include additional metrics like Sharpe ratio or maximum drawdown.
    Comparison with Other Strategies: Compare DCA with other investment strategies.
    Contributing
    Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

    This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to copy and paste this content into your `README.md` file, and customize it as needed!
