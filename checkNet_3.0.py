import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import datetime

edge_options = Options()
# profile_path = r"C:\Users\WIN-PRO\AppData\Local\Microsoft\Edge\User Data\Profile 1"
# edge_options.add_argument(f"user-data-dir={profile_path}")
edge_options.add_argument("headless")
edge_options.add_argument('--disable-gpu')  # Vô hiệu hóa GPU (khuyến nghị khi chạy headless)
edge_options.add_argument('--log-level=3')  # Giảm số lượng thông báo log (Chỉ hoạt động với Chrome, nhưng thử nếu bạn sử dụng bản dựa trên Chromium)
edge_options.add_argument('--silent')  # Cố gắng chạy trình điều khiển mà không xuất log ra console
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Loại bỏ thông báo "DevTools listening on..."

# ngăn log error ra cmd
# edge_service = Service(log_path=os.devnull)

edge_service = Service("./msedgedriver.exe")

def printTime():
    # Lấy thời gian hiện tại
    now = datetime.datetime.now()
    # Định dạng thời gian theo dạng giờ:phút
    print("Time current check: ", now.strftime("%H:%M:%S"))

def auto_wireless_login():
    driver = None
    try:
        # Khởi tạo WebDriver với các tùy chọn đã cấu hình
        driver = webdriver.Edge(options=edge_options, service=edge_service)
        
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
            driver.execute_script("var videos = document.getElementsByTagName('video'); for (var i = 0; i < videos.length; i++) {videos[i].muted = true;}")
            driver.execute_script("awingStateMachineContextActions.nextView()")
            time.sleep(1)
            # printTime()
            return True
        else:
            print("Không tìm thấy thẻ video")
            return True

    except Exception as e:
        print("Đã xảy ra lỗi:", e)
        return False
    # finally:
    #     if driver:
    #         driver.quit()

# Run indefinitely
while True:
    # printTime()
    # Check internet connection
    if auto_wireless_login():
        print("Internet connected!")
    else :
        print("Error")
    # Wait for 15 minutes before checking again
    # new_time = datetime.datetime.now() + datetime.timedelta(minutes=15, seconds=-5)
    # print("Time next check: ", new_time.strftime("%H:%M:%S"))
    time.sleep(15 * 60 - 6 )  # 15 minutes - 7 second delay

