import agentql
from playwright.sync_api import sync_playwright
import csv

# Initialise the browser
with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
    page = agentql.wrap(browser.new_page())
    page.goto("https://www.amazon.in")

    # Define a query for modal dialog's search input
    SEARCH_BOX_QUERY = """
    {
        search_box
    }
    """
    # Get the modal's search input and fill it with "Quick Start"
    response = page.query_elements(SEARCH_BOX_QUERY)
    response.search_box.type("laptop")

    # Find "Search" button using Smart Locator
    SEARCH_BUTTON_QUERY = """
    {
        search_button
    }
    """
    # Interact with the button
    response = page.query_elements(SEARCH_BUTTON_QUERY)
    response.search_button.click()

    LAPTOPS_QUERY = """
    {
        laptop_results[]{
            name,
            price,
            off,
            ratings,
            total_ratings
            free_delivery
            fastest_delivery
        }
    }   
    """

    PAGE_QUERY = """
    {
        page_select
        next_page
    }
    """
    laptop_array=[]

    for i in range(1, 20):
        response_page = page.query_data(LAPTOPS_QUERY)
        laptop_array += response_page["laptop_results"]

        if(i<20):
            response = page.query_elements(PAGE_QUERY)
            response.next_page.click()
    
    with open("laptop_results.csv", "w") as f:
        wr = csv.DictWriter(f, delimiter="\t",fieldnames=list(laptop_array[0].keys()))
        wr.writeheader()
        wr.writerows(laptop_array)

    f.close()


    # Used only for demo purposes. It allows you to see the effect of the script.
    page.wait_for_timeout(80000)