import time
import argparse
from zhipuai import ZhipuAI

# 硬编码API密钥
API_KEY = "01eb5c1d13b4f48b1972fc5350fa588c.wbsA6HPHD9vK2jA6"

def generate_video(prompt):
    # 初始化客户端
    client = ZhipuAI(api_key=API_KEY)

    # 记录开始时间
    start_time = time.time()

    # 生成视频
    response = client.videos.generations(
        model="cogvideo",
        prompt=prompt
    )
    print(response)

    # 获取任务ID和任务状态
    task_id = response.id
    task_status = response.task_status
    get_cnt = 0

    # 轮询检查任务状态
    while task_status == 'PROCESSING' and get_cnt <= 40:
        result_response = client.videos.retrieve_videos_result(
            id=task_id
        )
        print(result_response)
        task_status = result_response.task_status

        time.sleep(10)
        get_cnt += 1

    # 记录结束时间
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"视频生成耗时: {elapsed_time:.2f} 秒")
    return elapsed_time

if __name__ == "__main__":
    prompt = [
        "彼得兔（主体）驾驶着一辆迷你汽车（主体描述），穿梭在蜿蜒的乡间小路上（环境描述），它的脸上洋溢着无比的快乐和兴奋（氛围设定）",
        "小狮子（主体）在草原上追逐着蝴蝶（主体描述），它的金色鬃毛在阳光下闪闪发光（环境描述），整个场景充满了童真和活力（氛围设定）",
        "向日葵（主体）在微风中轻轻摇曳（主体描述），它们的花盘随着太阳转动（环境描述），营造出一种宁静而温暖的氛围（氛围设定）",
        "都市白领（主体）在繁忙的街道上快步行走（主体描述），高楼大厦的玻璃幕墙反射着耀眼的阳光（环境描述），整个城市充满了紧张而有序的节奏（氛围设定）",
        "古老的城堡（主体）静静地矗立在山丘之上（主体描述），它的石墙被岁月的风雨侵蚀（环境描述），散发出一种历史的厚重感（氛围设定）",
        "亚洲女子（主体）穿着传统服饰在古镇中漫步（主体描述），她的身影在古老的石板路上显得格外优雅（环境描述），整个场景充满了文化的韵味（氛围设定）",
        "雄鹰（主体）在天空中翱翔（主体描述），它的翅膀在蓝天白云的映衬下显得格外矫健（环境描述），整个画面充满了自由和力量（氛围设定）",
        "工业区的机器（主体）在轰鸣声中运转（主体描述），烟囱中冒出的白烟与蓝天形成鲜明对比（环境描述），整个场景充满了现代工业的活力（氛围设定）",
        "迁徙的鸟群（主体）在湿地之上形成壮观的队形（主体描述），它们的身影在夕阳的余晖中显得格外美丽（环境描述），整个画面充满了自然的和谐（氛围设定）",
        "现代化的城市（主体）在夜幕下灯火辉煌（主体描述），高楼大厦的灯光与星空交相辉映（环境描述），整个场景充满了都市的繁华和梦想（氛围设定）"
    ]
    
    total_elapsed_time = 0
    for p in prompt:
        elapsed_time = generate_video(p)
        total_elapsed_time += elapsed_time
    
    average_elapsed_time = total_elapsed_time / len(prompt)
    print(f"平均视频生成耗时: {average_elapsed_time:.2f} 秒")