from win10toast import ToastNotifier
import subprocess
import time

# Khởi tạo một đối tượng ToastNotifier
toaster = ToastNotifier()

# Hàm để kiểm tra kết nối mạng
def check_network():
    # try:
    #     subprocess.run(["checknet.exe"], check=True)
    # except subprocess.CalledProcessError as e:
    #     print("Error:", e)
    print("run exe")

# Hàm để xử lý thông báo nhận được
def handle_notification(title, message):
    if title == "Wireless":
        # Kiểm tra kết nối mạng khi nhận được thông báo từ ứng dụng "Wireless"
        check_network()

# Lắng nghe các thông báo
while True:
    notification = toaster.notification_active()
    if notification:
        handle_notification(notification[0], notification[1])
    time.sleep(1)
