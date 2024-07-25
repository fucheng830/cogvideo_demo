import time
import requests
import json
from zhipuai import ZhipuAI

# 硬编码API密钥
API_KEY = "01eb5c1d13b4f48b1972fc5350fa588c.wbsA6HPHD9vK2jA6"

def generate_video(prompt, image_url):
    # 设置API请求的URL和请求头
    url = "https://open.bigmodel.cn/api/paas/v4/videos/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # 替换为你的API密钥
    }
    # 设置请求参数
    data = {
        "model": "cogvideo",
        "prompt": prompt,
        "image_url": image_url  # 可选，如果需要图生视频
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    print(response_data)
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
    elapsed_time = generate_video('风轻轻吹动她的头发', 
                                  'https://mmbiz.qpic.cn/sz_mmbiz_png/oHz5prVpwVt8mbiboeicW3pZFZKND8kCXcvECecboFszsReRvBrwuN8RTjrdglXUybz5IjicMbZLkDU6hPkgnxWHQ/640?wxfrom=12&tp=wxpic&wx_fmt=png&amp;from=appmsg')
