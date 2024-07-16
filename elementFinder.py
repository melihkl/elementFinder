import time
import json

from selenium import webdriver
from selenium.webdriver import EdgeOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

with open('config.json') as config_file:
    config = json.load(config_file)

driver = webdriver

if config['browser_type'] == "Edge":
    options = EdgeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Edge(options=options)
    driver.maximize_window()


elif config['browser_type'] == "Chrome":
    options = ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()


if config['login_required']:
    driver.get(config["login_url"])

    time.sleep(1)

    username = driver.find_element(By.ID, config['username_element'])
    password = driver.find_element(By.ID, config['password_element'])

    username.send_keys(config['username'])
    password.send_keys(config['password'])
    
    driver.find_element(By.ID, config['login_button_element']).click()

    time.sleep(1)


driver.get(config['target_url'])
time.sleep(2)

driver.execute_script("""
window.getXPath = function(element) {
    if (element.id !== '') {
        return 'id("' + element.id + '")';
    }
    if (element === document.body) {
        return element.tagName;
    }

    var ix = 0;
    var siblings = element.parentNode.childNodes;
    for (var i = 0; i < siblings.length; i++) {
        var sibling = siblings[i];
        if (sibling === element) {
            return getXPath(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
        }
        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
            ix++;
        }
    }
}

""")

elements = driver.find_elements(By.XPATH, '//button | //input | //textarea | //select')

elements_info = []
for element in elements:
    element_type = element.get_attribute('type')
    element_id = element.get_attribute('id')
    element_name = element.get_attribute('name')
    element_class = element.get_attribute('class')
    element_text = element.find_element(By.XPATH, '..').text
    element_xpath = driver.execute_script("""return getXPath(arguments[0]);""", element)
    elements_info.append({
        "type": element_type,
        "id": element_id,
        "name": element_name,
        "className": element_class,
        "text": element_text,
        "xpath": element_xpath
    })


json_output = json.dumps(elements_info, indent=4, ensure_ascii=False)

with open('elemens_info.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)

driver.quit()
