import subprocess
import time
import os

# this is section from freeWifi.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException

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
        
        driver.get("http://acm.awingconnect.vn/login?serial=4C:5E:0C:05:00:40&client_mac=34:F3:9A:6C:44:B8&client_ip=172.172.30.204&userurl=http://www.msftconnecttest.com/redirect&login_url=http://free.wi-mesh.vn/login")
        time.sleep(4)  # Đợi trang web load 4s

        # Nhấn nút "acceptconnection"
        accept_button = driver.find_element(By.ID, "acceptconnection")
        accept_button.click()

        # Tắt âm thanh của tab bằng cách chạy JavaScript trong trình duyệt
        driver.execute_script("var videos = document.getElementsByTagName('video'); for (var i = 0; i < videos.length; i++) {videos[i].muted = true;}")

        # Cuộn xuống dưới cùng của trang
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)

        # Đợi 7s
        time.sleep(7)

        connect_button = driver.find_element(By.ID, "connectToInternet")
        connect_button.click()
        # time.sleep(2)

    except Exception as e:
        print("Đã xảy ra lỗi:", e)
    finally:
        if driver:
            driver.quit()

def check_internet_connection():
    try:
        # Thử ping đến Default Gateway
        result = subprocess.run(['ping', '172.172.0.1', '-n', '1'], capture_output=True, text=True, timeout=5)
        if "Destination host unreachable" in result.stdout or "Destination net unreachable" or "Request timed out" in result.stdout:
            print("Destination net unreachable. Running the executable program.")
            # Chạy chương trình
            auto_wireless_login()
            return False
        else:
            print('connected')
            return True
    except subprocess.TimeoutExpired:
        print('timeout')
        return False

# Run indefinitely
while True:
    # Check internet connection
    if not check_internet_connection():
        print("Internet connected!")
    
    # Wait for 15 minutes before checking again
    time.sleep(15 * 60 - 14)  # 15 minutes - 3 second delay
