from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests, random, time, bs4

# Configuration parameters
config = {
    'email' : 'your_email', # Replace with your 10FastFingers email
    'password' : 'your_password', # Replace with your 10FastFingers password
    'url_test' : 'https://10fastfingers.com/typing-test/english', # Replace with the URL of the 10FastFingers test
    'delay_between_keys' : 0.05,  # in seconds
    'delay_between_keys_is_random' : True, # Set to True to randomly delay between keys, False to use the specified delay
    'is_fast_typing' : True,  # Set to True to enable fast typing, False to disable
    'with_correction' : 2, # Number of correction mistakes to make during the test, 0 for no correction
    'with_typo' : 2, # Number of typo mistakes to make during the test, 0 for no typo
}
def delay():
    if config['delay_between_keys_is_random']:
        # Generate a random delay between 0.03 and 0.1 seconds for fast typing,
        # otherwise use the specified delay.
        minimum, maximum = (0.03, 0.06) if config['is_fast_typing'] else (0.5, 0.8)
        return random.uniform(minimum, maximum)
    return config['delay_between_keys']

def random_alphabet(old_alphabet):
    while True:
        new = chr(random.randint(ord('a'), ord('z')))
        if old_alphabet != new:
            return new

def get_time_remaining(driver):
    return driver.find_element(By.ID, 'timer').text

def random_time(n):
    result = []
    while len(result) < n:
        a = random.randint(0,59)
        text = f'0:{a:02}'
        if text not in result:
            result.append(text)
    return result

def extract_words_from_page(driver, div_id='words'):
    a = driver.page_source
    b = bs4.BeautifulSoup(a, 'html.parser')
    words = b.find('div', {'id': div_id}).text.strip()
    return words

def send_character(driver, key):
    driver.find_element(By.ID, 'inputfield').send_keys(key)

def image_to_text(filename):
    # Register OCR API https://ocr.space/ocrapi/freekey (free 25k requests per month)
    payload = {'isOverlayRequired': False,
               'apikey': 'K83554843688957', # Replace with your OCR API key
               'language': 'eng'} # Replace with your preferred language (eng, deu, fra, ita, jpn)
    f = open(filename, 'rb')
    r = requests.post('https://api.ocr.space/parse/image', files={filename: f}, data=payload)
    try:
        text = r.json()['ParsedResults'][0]['ParsedText'].strip().replace('\r\n',' ').replace('\n',' ')
    except:
        print('Failed : ' + r.json()['ErrorMessage'])
        return False
    return text

def get_cookie(driver):
    cookie_string = ''
    for cookie in driver.get_cookies():
        cookie_string += f"{cookie['name']}={cookie['value']}; "
    cookie_string = cookie_string.strip('; ')
    return cookie_string

def main():
    # Set up Selenium WebDriver
    service = Service(executable_path='driver/geckodriver')
    driver = webdriver.Firefox(service=service)
    if config['email'] and config['password']:
        print('Login to your account...')
        # Login to 10FastFingers
        driver.get('https://10fastfingers.com/login')
        # wait for the page to load and for the login form to be loaded (3 seconds)
        time.sleep(3)
        # Accept cookies
        driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        # Enter email and password and submit the login form
        driver.find_element(By.ID, 'UserEmail').send_keys(config['email'])
        driver.find_element(By.ID, 'UserPassword').send_keys(config['password'])
        driver.find_element(By.ID, 'login-form-submit').submit()
        time.sleep(3)  # Wait for the login to complete
        # Check if login was successful
        if driver.current_url == 'https://10fastfingers.com/':
            print('Login failed, please check your email and password.')
            return
        print('Login successful.')

    print('Starting the test...')
    # IF ANTICHEAT page is detected
    if 'anticheat' in config['url_test']:
        driver.get(config['url_test'])
        time.sleep(3)
        try:
            driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        except:
            pass
        time.sleep(3)
        driver.find_element(By.ID, 'start-btn').click()
        time.sleep(2)
        div_img = driver.find_element(By.CSS_SELECTOR, '#word-img img')
        get_img_url = div_img.get_attribute('src')
        cookie = get_cookie(driver)
        response = requests.get(get_img_url, headers = {'Cookie': cookie})
        # save file
        filename = 'image.jpg'
        with open(filename, 'wb') as f:
            f.write(response.content)
        # Convert image to text using OCR
        text = image_to_text(filename)
        if not text:
            print('Failed to extract text from the image.')
            return
        print('Text extracted from the image :'+ text)
        for i in text.split(' '):
            for j in i:
                driver.find_element(By.ID, 'word-input').send_keys(j)
                time.sleep(delay())
            driver.find_element(By.ID, 'word-input').send_keys(Keys.SPACE)
        driver.find_element(By.ID, 'word-input').send_keys(Keys.TAB + Keys.ENTER)
    else:
        # Normal typing test (not anticheat)
        # Generate random times for typing mistakes and corrections
        time_for_typo = random_time(config['with_typo'])
        time_for_correction = random_time(config['with_correction'])
        print('Typo will happen at : ' + ', '.join(time_for_typo) + ' (time remaining)')
        print('Correction will happen at : ' + ', '.join(time_for_correction) + ' (time remaining)')
        # Navigate to the 10FastFingers typing test page
        driver.get(config['url_test'])
        # Wait for the page to load and for the words to be loaded (3 seconds)
        time.sleep(3)
        # Accept cookies
        if not (config['email'] and config['password']):
            driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
        # collect all words from the page test
        words = extract_words_from_page(driver)
        # Types a sequence of words into a specified input field on a webpage, simulating a user typing.
        for i in words.split(' '):
            for j in i:
                now_time = get_time_remaining(driver)
                if now_time in time_for_typo:
                    j = random_alphabet(j)
                    time_for_typo.remove(now_time)
                if now_time in time_for_correction:
                    incorrect_char = random_alphabet(j)
                    send_character(driver, incorrect_char)
                    time.sleep(0.5)
                    send_character(driver, Keys.BACKSPACE)
                    time_for_correction.remove(now_time)
                # Send a key to the input field
                send_character(driver, j)
                time.sleep(delay())
                # Check if the timer has run out and break the loop if it has
                if get_time_remaining(driver) == '0:00':
                    driver.find_element(By.ID, 'inputfield').clear()
                    return
            # Press Enter to submit the word
            send_character(driver, Keys.SPACE)
            # Wait for the next word
            time.sleep(0.1)
    print('')
    print('Test completed.')
    print('')
    is_close = input('Do you want to close the browser? (y/n): ')
    if is_close.lower() == 'y':
        driver.quit()
    else:
        print('Browser is still open.')

main()