from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains


import time

def auto_wireless_login():
    try:
        edge_options = Options()
        profile_path = r"C:\Users\WIN-PRO\AppData\Local\Microsoft\Edge\User Data\Profile 1"
        edge_options.add_argument(f"user-data-dir={profile_path}")

        # Khởi tạo WebDriver với các tùy chọn đã cấu hình
        driver = webdriver.Edge(options=edge_options)

        driver.get("http://acm.awingconnect.vn/login?serial=4C:5E:0C:05:00:40&client_mac=34:F3:9A:6C:44:B8&client_ip=172.172.30.204&userurl=http://www.msftconnecttest.com/redirect&login_url=http://free.wi-mesh.vn/login")
        time.sleep(4)  # Đợi trang web load

        # Nhấn nút "acceptconnection"
        accept_button = driver.find_element(By.ID, "acceptconnection")
        accept_button.click()

        # Tắt âm thanh của tab bằng cách chạy JavaScript trong trình duyệt
        driver.execute_script("var videos = document.getElementsByTagName('video'); for (var i = 0; i < videos.length; i++) {videos[i].muted = true;}")

        # Đợi 6s
        time.sleep(7)
        # driver.execute_script(f"console.log('Giá trị của src_value là: {src_value}')")

        connect_button = driver.find_element(By.ID, "connectToInternet")
        connect_button.click()
        time.sleep(2)

        connect_button = driver.find_element(By.ID, "connectToInternet")
        connect_button.click()
        time.sleep(2)

    except Exception as e:
        print("Đã xảy ra lỗi:", e)
    finally:
        driver.quit()

# Thực hiện chương trình
auto_wireless_login()
