import time
import requests
import json
import base64
from zhipuai import ZhipuAI

# 硬编码API密钥
API_KEY = "xx"

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def generate_video(prompt, image_path=None, image_url=None):
    # 设置API请求的URL和请求头
    url = "https://open.bigmodel.cn/api/paas/v4/videos/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # 替换为你的API密钥
    }
    # 设置请求参数
    data = {
        "model": "cogvideoX",
        "prompt": prompt
    }
    
    if image_path:
        base64_image = encode_image_to_base64(image_path)
        data["image_url"] = base64_image
    elif image_url:
        data["image_url"] = image_url

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    task_id = response_data["id"]
    task_status = response_data["task_status"]

    client = ZhipuAI(api_key=API_KEY)
    # 轮询检查任务状态
    get_cnt = 0
    while task_status == 'PROCESSING' and get_cnt <= 40:
        result_response = client.videos.retrieve_videos_result(
            id=task_id
        )
        print(result_response)
        task_status = result_response.task_status

        time.sleep(10)
        get_cnt += 1

if __name__ == "__main__":
    # 使用本地图像路径
    elapsed_time = generate_video('女人微笑，风吹动头发', image_path='C:/Users/Administrator/Pictures/Saved Pictures/R.jpg')
    # 或者使用图像URL
    # elapsed_time = generate_video('美女跳舞，扭动屁股', image_url='https://mmbiz.qpic.cn/sz_mmbiz_png/RcDZlibI6KSBFBlBGNVV2WT9Da060jNTevohT0CUfOoF0730C2V1icRIliaSWJo2diaLibGo9zic6ia1ibs7Hr0wEfhiaOA/640?wxfrom=12&tp=wxpic&usePicPrefetch=1&wx_fmt=png&amp;from=appmsg')