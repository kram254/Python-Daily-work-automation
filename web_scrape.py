from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username','demo')
    page.fill('input#input-password','demo')
    page.click('button[type = submit]')
    page.wait_for_load_state('networkidle')
    page.is_visible('div.tile-body')
    html = page.inner_html('#content')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.find_all('h2'))
    total_orders = soup.find('h2', {'class': 'float-end'}).text 
    print(f'total orders = {total_orders}')
    
    print("Total orders collected successfully.")
    
