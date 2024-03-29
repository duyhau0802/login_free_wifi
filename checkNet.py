import subprocess

def check_internet_connection():
    try:
        # Thử ping đến Default Gateway
        result = subprocess.run(['ping', '172.172.0.1', '-n', '1'], capture_output=True, text=True, timeout=5)
        if "Destination host unreachable" in result.stdout or "Destination net unreachable" or "time out" in result.stdout:
            print("Destination net unreachable. Running the executable program.")
            # Chạy chương trình .exe 
            subprocess.run(["./dist/freeWifi.exe"])
        else:
            print('connected')
            return True
    except subprocess.TimeoutExpired:
        print('timeout')
        return False


check_internet_connection()
