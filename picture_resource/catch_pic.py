import requests
import time
from datetime import datetime

"""
间隔时间 T 实现抓拍
"""

# 配置参数
API_URL = "http://iot.krzhibo.com/admin/common/cloudData/getPic"
# 摄像头id: # "KRIPC_93003194_90"  "KRIPC_93003280_5"  "KRIPC_101150836_64"
DEVICE_NAME = "KRIPC_101150836_64"

REQUEST_INTERVAL = 1  # 秒
PHOTO_TIMES = 1  # 抓拍次数

# # 请求头配置
# headers = {
#     "Content-Type": "application/json",
# }
#
# # 请求体配置
# payload = {
#     "deviceName": DEVICE_NAME
# }


def capture_request():
    try:
        # 发送POST请求
        # response = requests.post(
        #     API_URL,
        #     json=payload,
        #     headers=headers,
        #     timeout=3
        # )

        # 拼接GET请求URL
        url_with_params = f"{API_URL}?deviceName={DEVICE_NAME}"

        # 发送GET请求
        response = requests.get(url_with_params, timeout=3)

        # 记录请求时间戳
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 处理响应
        if response.status_code == 200:
            result = response.json()
            print(f"[{timestamp}] 抓拍成功 | 状态码: {response.status_code}")
            print(f"请求ID: {result.get('data', {}).get('RequestId', '')}")
            return True
        else:
            print(f"[{timestamp}] 请求异常 | 状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] 请求失败 | 错误: {str(e)}")
        return False


if __name__ == "__main__":
    print(f"启动抓拍程序，设备: {DEVICE_NAME}")

    over_times = 0
    try:
        while over_times < PHOTO_TIMES:
            capture_request()
            time.sleep(REQUEST_INTERVAL)
            over_times += 1

    except KeyboardInterrupt:
        print("\n程序已手动终止")