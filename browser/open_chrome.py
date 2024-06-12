import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Use webdriver_manager to handle the driver installation
chrome_driver_path = ChromeDriverManager().install()

driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://licwin.com/#/pages/login/index?type=0")

driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-movable-area/uni-view[5]/uni-view/uni-view[1]/uni-view/uni-view/uni-view[2]/uni-input/div/input").send_keys("9497342770")
driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-movable-area/uni-view[5]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-input/div/input").send_keys("Mendozaa@123")

input("Logged in ? ")

def check_profit_or_loss():
    m,p = [], "S"
    with open("points.txt", "r") as file:
        m = file.read().split('\n')
    money = 100
    for i,j in enumerate(m):
        if j == "":
            continue
        num = j.split()[2][0]
        if i == 0:
            p = num
            continue
        if num == p:
            money += 9.55
        else:
            p = num
            money -= 10
        print(i, j, p, num, money)
        if money > 150 or money < 50:
            print(money)
    return money > 150 or money < 50

def bet(color, period):
    if color == "S":
        ele = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]/uni-view[2]/uni-view[2]"
    else:
        ele = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]/uni-view[2]/uni-view[1]"
    try:
        driver.find_element(By.XPATH, ele).click()
    except:
        print("scrolled")
        time.sleep(5)
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        driver.find_element(By.XPATH, ele).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[3]/uni-view[2]/uni-view/uni-view[1]/uni-view[2]/uni-view[2]/uni-view/uni-view[2]").click()
    driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[3]/uni-view[2]/uni-view/uni-view[1]/uni-view[3]/uni-view[2]").click()
    print("Period      :",period)
    print("Betted Size :", color)

def add_text(texts):
    with open("points.txt", "a") as file:
        for i in texts:
            file.write(i + "\n")

# count = 1
# c = 13
# while count<=c:
#     count += 1
#     texts = []
#     for i in range(2,12):
#         m = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[" + str(i) + "]"
#         n = driver.find_element(By.XPATH, m).text
#         n = n.replace('\n', ' ')
#         texts.append(n)
#     add_text(texts)
#     driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[12]/uni-view/uni-view[3]").click()
#     time.sleep(0.5)

num_with_point = {}
t = 0
while True:
    m = "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view[2]/uni-view[2]"
    n = driver.find_element(By.XPATH, m).text
    n = n.replace('\n', ' ')
    period = n.split()[0][-3:]
    size = n.split()[2][0]
    point = num_with_point.get(period)
    if not point:
        num_with_point[period] = size
        print(num_with_point)
        add_text([n])
        bet(size, int(period) + 1)
        t += 1
        print(t, "bets remaining")
        if check_profit_or_loss():
            break
    else:
        time.sleep(5)
        print("Slept for 5 seconds")
    
    if t > 60:
        break


time.sleep(5)
driver.quit()
