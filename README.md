# 10FastFingers Cheat Script

[Output sample](https://github.com/richoarbianto/10fastfinger-cheat/raw/master/play.gif)

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
    'email' : 'bolobolokun@gmail.com', # Replace with your 10FastFingers email
    'password' : 'hahaha#123', # Replace with your 10FastFingers password
    'url_test' : 'https://10fastfingers.com/anticheat/view/2/6', # Replace with the URL of the 10FastFingers test
    'delay_between_keys' : 0.05,  # in seconds
    'delay_between_keys_is_random' : True, # Set to True to randomly delay between keys, False to use the specified delay
    'is_fast_typing' : True,  # Set to True to enable fast typing, False to disable
    'with_correction' : 10, # Number of correction mistakes to make during the test, 0 for no correction
    'with_typo' : 5, # Number of typo mistakes to make during the test, 0 for no typo
    'driver_path' : 'driver/geckodriver',  # Replace with the path
    'ocr_key' : 'K83554843688957', # Replace with your OCR API key or use my key, Register OCR API https://ocr.space/ocrapi/freekey (free 25k requests per month)
    'language' : 'eng' # Replace with your preferred language (eng, dut, spa, ita, jpn)
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
