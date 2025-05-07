import requests
import time
from datetime import datetime

# 配置参数
API_URL = "http://iot.krzhibo.com/admin/common/cloudData/getResourceAll"
# 摄像头id: # "KRIPC_93003194_90"  "KRIPC_93003280_5"  "KRIPC_101150836_64"
DEVICE_NAME = "KRIPC_101150836_64"
SAVE_FOLDER = "./photos/" + DEVICE_NAME + "/"  # 图片保存路径

# 其他配置
REQUEST_INTERVAL = 1
PHOTO_TIMES = 1

headers = {"Content-Type": "application/json"}
payload = {"deviceName": DEVICE_NAME}


def save_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True, timeout=5)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"图片下载失败: {str(e)}")
        return False


def download_request():
    try:
        # 发送抓拍请求
        response = requests.post(
            API_URL,
            json=payload,
            headers=headers,
            timeout=3
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if response.status_code == 200:
            result = response.json()
            if "data" in result and len(result["data"]) > 0:
                # 解析图片信息
                img_data = result["data"][0]
                img_url = img_data.get("pic", "")

                if img_url:
                    # 生成文件名 deviceName_时间戳_id.jpg
                    # filename = f"{DEVICE_NAME}_{timestamp}_{img_data['id']}.jpg"
                    filename = f"{DEVICE_NAME}_{img_data['id']}.jpg"
                    save_path = f"{SAVE_FOLDER}{filename}"

                    # 保存图片
                    if save_image(img_url, save_path):
                        print(f"[{timestamp}] 图片保存成功: {filename}")
                        return True
            print(f"[{timestamp}] 响应中未找到有效图片数据")
            return False
        else:
            print(f"[{timestamp}] 请求异常 | 状态码: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] 请求失败 | 错误: {str(e)}")
        return False


if __name__ == "__main__":
    import os

    # 创建保存目录
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    print(f"启动抓拍程序，设备: {DEVICE_NAME}")

    try:
        count = 0
        while count < PHOTO_TIMES:
            if download_request():
                count += 1
            time.sleep(REQUEST_INTERVAL)

    except KeyboardInterrupt:
        print("\n程序已手动终止")