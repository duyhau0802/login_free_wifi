import subprocess

# import re

# def get_wifi_state(result):
#     # Sử dụng biểu thức chính quy để tìm dòng chứa thông tin trạng thái kết nối
#     state_pattern = re.compile(r"^\s*State\s*:\s*(\S+)", re.MULTILINE)
#     state_match = state_pattern.search(result.stdout)
#     if state_match:
#         return state_match.group(1)
#     else:
#         return None

# def check_wifi_connection(wifi_name):
#     try:
#         result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True, check=True)
#         wifi_state = get_wifi_state(result)

#         print(wifi_state)

#         # if wifi_state == 'connected':
#         #     print("Mạng WiFi đang kết nối.")
#         # elif wifi_state == 'disconnected':
#         #     print("Mạng WiFi đang không kết nối.")
#         # else:
#             # print("Không thể xác định trạng thái kết nối của mạng WiFi.")

#     except subprocess.CalledProcessError:
#         print("Error: Command execution failed.")
#         return False

# wifi_name = "WiFi"  # Tên của mạng WiFi bạn muốn kiểm tra
# check_wifi_connection(wifi_name)


def check_internet_connection():
    try:
        # Thử ping đến Default Gateway
        result = subprocess.run(['ping', '172.172.0.1', '-n', '1'], capture_output=True, text=True, timeout=5)
        if "Destination host unreachable" in result.stdout or "Destination net unreachable" or "time out" in result.stdout:
            print("Destination net unreachable. Running the executable program.")
            # Chạy chương trình .exe ở đây
            # Ví dụ:
            # subprocess.run(["path/to/your/program.exe"])
        else:
            print('connected')
            return True
    except subprocess.TimeoutExpired:
        print('timeout')
        return False


check_internet_connection()
