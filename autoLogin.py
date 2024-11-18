import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

edge_options = Options()
edge_options.add_argument("headless")
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--log-level=3')
edge_options.add_argument('--silent')
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])

edge_service = Service("./msedgedriver.exe")

def print_time(string):
    now = datetime.datetime.now()
    print(string, now.strftime("%H:%M:%S"))

def auto_wireless_login(driver):
    try:
        driver.get("http://v1.awingconnect.vn/login?serial=4C:5E:0C:05:00:40&client_mac=34:F3:9A:6C:44:B8&client_ip=172.172.27.57&userurl=http://www.msftconnecttest.com/redirect&login_url=http://free.wi-mesh.vn/login")
        time.sleep(3)
        if driver.execute_script("return typeof awingStateMachineContextActions !== 'undefined';"):
            driver.execute_script("awingStateMachineContextActions.nextView()")
        else:
            print("awingStateMachineContextActions is not defined on this page.")
            return False
        # Tìm kiếm các thẻ video
        video_tags = driver.find_elements(By.TAG_NAME, "video")
        if video_tags:
            driver.execute_script("var videos = document.getElementsByTagName('video'); for (var i = 0; i < videos.length; i++) {videos[i].muted = true;}; awingStateMachineContextActions.nextView()")
            # driver.execute_script("")
            time.sleep(1)
            # printTime()
            return True
        else:
            print("Không tìm thấy thẻ video")
            return False

    except Exception as e:
        print("Đã xảy ra lỗi:", e)
        return False

# Initialize driver once
driver = webdriver.Edge(options=edge_options, service=edge_service)

# Run indefinitely
count = 0
try:
    while True:
        # print_time("Time start check: ")
        # time_start = datetime.datetime.now()
        if auto_wireless_login(driver):
            print("OK!")
        else:
            print("Error!")
            break
        # print_time("Time end check: ")
        # print("\n")
        # time_end = datetime.datetime.now()
        # print("Time check: ", time_end - time_start)
        # new_time = datetime.datetime.now() + datetime.timedelta(minutes=15, seconds=-4)
        # print("Time next check: ", new_time.strftime("%H:%M:%S"))
        
        # Wait for 15 minutes before checking again
        time.sleep(15 * 60 - 2.5 )  # Wait for 15 minutes minus 3 seconds
finally:
    driver.quit()  # Ensure driver quits on exitc