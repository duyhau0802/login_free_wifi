import subprocess
import time
import os

def check_internet_connection():
    try:
        # Thử ping đến Default Gateway
        result = subprocess.run(['ping', '172.172.0.1', '-n', '1'], capture_output=True, text=True, timeout=5)
        if "Destination host unreachable" in result.stdout or "Destination net unreachable" or "Request timed out" in result.stdout:
            print("Destination net unreachable. Running the executable program.")
            # Chạy chương trình .exe 
            subprocess.run(["./dist/freeWifi.exe"], stderr=subprocess.PIPE)
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
    if check_internet_connection():
        print("Internet connected!")
    else:
        print("No internet connection!")
    
    # Wait for 15 minutes before checking again
    time.sleep(15 * 60 + 2)  # 15 minutes + 5 second delay
