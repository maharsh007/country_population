import agentql
from playwright.sync_api import sync_playwright

# Initialise the browser
with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
    page = agentql.wrap(browser.new_page())
    page.goto("https://www.sacnilk.com")

    TABS_QUERY = """
    {
        header_tabs(The tabs present in the top header)[]
    }
    """
    response = page.query_elements(TABS_QUERY)

    response.header_tabs[1].hover()

    BOX_OFFICE_QUERY = """
    {
        box_office_options[]
    }
    """

    response = page.query_elements(BOX_OFFICE_QUERY)
    
    print(response)

    response.box_office_options.get_by_title("All Bollywood 100 Cr Club Movies").click()

    BOX_OFFICE_100_CRORE="""
    {
        bollywood_100_cr_club_all_time[]{
            movie_name,
            worldwide,
            hindi_net,
            india_gross,
            overseas,
            budget,
            verdict
        }
    }
    """
    response = page.query_elements(BOX_OFFICE_100_CRORE)

    print(response)

    # print(response.header_tabs[1].inner_html())

    # Used only for demo purposes. It allows you to see the effect of the script.
    page.wait_for_timeout(80000)