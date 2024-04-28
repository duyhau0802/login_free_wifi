import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

edge_options = Options()
profile_path = r"C:\Users\WIN-PRO\AppData\Local\Microsoft\Edge\User Data\Profile 1"
edge_options.add_argument(f"user-data-dir={profile_path}")
edge_options.add_argument("headless")
edge_options.add_argument('--disable-gpu')  # Vô hiệu hóa GPU (khuyến nghị khi chạy headless)
edge_options.add_argument('--log-level=3')  # Giảm số lượng thông báo log (Chỉ hoạt động với Chrome, nhưng thử nếu bạn sử dụng bản dựa trên Chromium)
edge_options.add_argument('--silent')  # Cố gắng chạy trình điều khiển mà không xuất log ra console
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Loại bỏ thông báo "DevTools listening on..."

# ngăn log error ra cmd
service = Service(log_path=os.devnull)

def auto_wireless_login():
    driver = None
    try:
        # Khởi tạo WebDriver với các tùy chọn đã cấu hình
        driver = webdriver.Edge(options=edge_options, service=service)
        
        driver.get("http://acm.awingconnect.vn/login?serial=4C:5E:0C:05:00:40&client_mac=34:F3:9A:6C:44:B8&client_ip=172.172.27.242&userurl=http://www.msftconnecttest.com/redirect&login_url=http://free.wi-mesh.vn/login")
        
        time.sleep(1)  # Đợi trang web load 4s

        driver.execute_script("nextView()")

        driver.execute_script("var videos = document.getElementsByTagName('video'); for (var i = 0; i < videos.length; i++) {videos[i].muted = true;}")
        
        time.sleep(1)

        driver.execute_script("nextView()")

        time.sleep(1)

        return True
    except Exception as e:
        print("Đã xảy ra lỗi:", e)
        return False
    # finally:
    #     if driver:
    #         driver.quit()

# Run indefinitely
while True:
    # Check internet connection
    if auto_wireless_login():
        print("Internet connected!"+"\n")
    else :
        print("Error"+"\n")
    # Wait for 15 minutes before checking again
    time.sleep(15 * 60 - 3)  # 15 minutes - 3 second delay
