# 10FastFingers Cheat Script

This script is designed to help users automatically complete 10FastFingers typing tests using Selenium. It can perform fast typing with options to introduce typos and corrections.

## Features
- AntiCheat bypass
- Custom Fast typing with random delays between characters.
- Introduces typos and corrections during the test.
- Automatically logs into your 10FastFingers account.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- Webdriver (ChromeDriver, GeckoDriver, etc.)

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/richoarbianto/10fastfingers-cheat.git
   cd 10fastfingers-cheat
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Download and place the appropriate webdriver (e.g., `chromedriver` for Google Chrome) in the project directory or in your system PATH.

## Configuration

Edit the `main.py` file to fill in your 10FastFingers account details and set other parameters:

```python
config = {
    'email' : 'your_email', # Replace with your 10FastFingers email
    'password' : 'your_password', # Replace with your 10FastFingers password
    'url_test' : 'https://10fastfingers.com/typing-test/english', # URL of the 10FastFingers test
    'delay_between_keys' : 0.05,  # in seconds
    'delay_between_keys_is_random' : True, # Random delay between keys
    'is_fast_typing' : True,  # Enable fast typing
    'with_correction' : 2, # Number of correction mistakes during the test
    'with_typo' : 2, # Number of typo mistakes during the test
    'driver_path' : 'driver/geckodriver'  # Replace with the path
}
```

## Usage

Run the script with the following command:

```sh
python main.py
```

The script will open a browser and start the typing test according to the configuration settings.

## Notes

- Make sure you use the appropriate webdriver for your browser.
- This script is intended for educational and personal use. Misuse of this script may violate the terms of service of 10FastFingers.

## License

This project is licensed under the MIT License.
