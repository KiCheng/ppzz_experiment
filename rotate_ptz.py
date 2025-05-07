import time

import requests
import json


def control_ptz(direction, speed=10):
    # 摄像头id: # "KRIPC_93003194_90"  "KRIPC_93003280_5"  "KRIPC_101150836_64"
    device_id = "KRIPC_101150836_64"
    api_url = "http://iot.krzhibo.com/index/xcx/ptz/setPtz"

    # 请求头
    headers = {
        "Content-Type": "application/json; charset=utf-8",
    }

    # 请求体
    payload = {
        "uid": device_id,
        "cmd": direction,
        "speed": speed,
    }

    try:
        response = requests.post(
            url=api_url,
            headers=headers,
            data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
            timeout=5
        )

        # 处理响应
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                print("控制指令发送成功")
            elif result.get("code") == 1:
                print(f"操作成功：{result.get('data')}")
        else:
            print(f"请求失败，状态码：{response.status_code}")

    except Exception as e:
        print(f"发生异常：{str(e)}")

def control_direction(direction, speed):
    if direction == "ptz_left_press":
        control_ptz(
            direction="ptz_left_press",
            speed=speed
        )
    elif direction == "ptz_right_press":
        control_ptz(
            direction="ptz_right_press",
            speed=speed
        )
    elif direction == "ptz_up_press":
        control_ptz(
            direction="ptz_up_press",
            speed=speed
        )
    elif direction == "ptz_down_press":
        control_ptz(
            direction="ptz_down_press",
            speed=speed
        )

    time.sleep(1)
    control_ptz(
        direction="ptz_release_pre",
        speed=speed
    )


if __name__ == "__main__":
    # 向左移动步长
    control_direction("ptz_left_press", 10)
    # 向右移动步长
    # control_direction("ptz_right_press", 10)
    # 向上移动步长
    # control_direction("ptz_up_press", 10)
    # 向下移动步长
    # control_direction("ptz_down_press", 10)

    