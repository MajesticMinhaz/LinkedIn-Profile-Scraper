import json
from dotenv import dotenv_values
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from database import create_linkedin_data


def profile_url_extractor(keyword_search_url: str, chrome_driver: Chrome) -> list or None:
    chrome_driver.get(keyword_search_url)

    try:
        # Wait for the webpage to load and find search-results-container div
        wait_for_search_results_container_div_tag = WebDriverWait(driver=chrome_driver, timeout=10)
        div_tag_element = wait_for_search_results_container_div_tag.until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "div.search-results-container")
            )
        )

        profile_urls = list()

        try:
            li_tags = div_tag_element.find_elements(by=By.CSS_SELECTOR, value="li.reusable-search__result-container")

        except NoSuchElementException:
            li_tags = list()

        for li_tag in li_tags:
            try:
                a_tag = li_tag.find_element(
                    by=By.CSS_SELECTOR,
                    value='a.app-aware-link[href^="https://www.linkedin.com/in/"]'
                )

                href_value = a_tag.get_attribute("href")
                profile_urls.append(href_value)
            except NoSuchElementException:
                pass

        return profile_urls
    except TimeoutException:
        # Handle the case where the elements are not found within the specified timeout
        return None
    except AttributeError:
        return None


def clean_linkedin_profile_url(profile_url):
    # Check if the profile URL contains "?"
    if '?' in profile_url:
        # Split the URL by "?"
        base_url, _ = profile_url.split('?', 1)
        return base_url
    else:
        return profile_url


if __name__ == '__main__':
    # Get the config values from .env file
    config = dotenv_values('.env')

    # create the driver instance
    # driver = Chrome(driver_executable_path=config.get('DRIVER_PATH'), use_subprocess=False)
    driver = Chrome(driver_executable_path=config.get('DRIVER_PATH'), use_subprocess=True)
    driver.set_window_size(
        width=int(config.get('SCRAP_WINDOW_WIDTH')),
        height=int(config.get('SCRAP_WINDOW_HEIGHT'))
    )
    driver.get(config.get("LINKEDIN_WEBSITE_URL"))

    # read cookies file and login to facebook website
    with open(file=config.get('COOKIES_FILE_PATH'), mode="r") as read_cookie_file:
        cookie = json.loads(read_cookie_file.read())

        for cookie_data in cookie:
            customized_cookie = dict()
            customized_cookie['domain'] = cookie_data.get("domain")
            customized_cookie['name'] = cookie_data.get("name")
            customized_cookie['value'] = cookie_data.get("value")

            driver.add_cookie(cookie_dict=customized_cookie)

        driver.refresh()
        driver.get(config.get("LINKEDIN_WEBSITE_URL"))

    from_page = int(config.get("KEYWORD_SEARCH_START_PAGE_NUMBER"))
    to_page = int(config.get("KEYWORD_SEARCH_STOP_PAGE_NUMBER")) + 1

    for page_number in range(from_page, to_page):
        url = config.get("KEYWORD_SEARCH_URL").replace("{}", str(page_number)).strip()
        extracted_urls = profile_url_extractor(keyword_search_url=url, chrome_driver=driver)

        # Using map to apply clean_linkedin_profile_url() to each URL in the list
        cleaned_profile_urls = list(map(clean_linkedin_profile_url, extracted_urls))

        for cleaned_profile_url in cleaned_profile_urls:
            create_linkedin_data(
                profile_url=cleaned_profile_url,
            )

    print("Successfully Completed the tasks")
