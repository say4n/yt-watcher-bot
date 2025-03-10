from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import ChromiumOptions as Options


def visit_and_watch(url: str):
    options = Options()
    options.add_argument("--mute-audio")
    # options.add_argument("--autoplay-policy=no-user-gesture-required")
    options.add_argument("--window-size=640,480")

    ignored_errors = [NoSuchElementException, ElementNotInteractableException]

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)

        wait = WebDriverWait(driver, timeout=float("inf"), ignored_exceptions=ignored_errors)

        cookie_reject_button_xpath = "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"
        cookie_reject_button = wait.until(
            EC.presence_of_element_located((By.XPATH, cookie_reject_button_xpath))
        )
        cookie_reject_button.click()

        replay_button_xpath = "//button[@title='Replay']"
        wait.until(EC.presence_of_element_located((By.XPATH, replay_button_xpath)))

if __name__ == "__main__":
    test_video = "https://youtu.be/dQw4w9WgXcQ?autoplay=1"
    visit_and_watch(test_video)
