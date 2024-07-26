import time
import argparse
from zhipuai import ZhipuAI

# 硬编码API密钥
API_KEY = "xx"

def generate_video(prompt):
    # 初始化客户端
    client = ZhipuAI(api_key=API_KEY)

    # 记录开始时间
    start_time = time.time()

    # 生成视频
    response = client.videos.generations(
        model="cogvideoX",
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
    "清晨的湖畔，一只天鹅（主体）优雅地划过平静的水面（环境描述），天鹅的颈项在晨光中显得格外修长（动作）。背景是一片宁静的湖景。",
    "黄昏的沙漠，一只骆驼（主体）缓缓行走在沙丘之间（环境描述），骆驼的驼峰在夕阳的映照下呈现出金黄色（动作）。背景是一望无际的沙海。",
    "午后的花园，一只蝴蝶（主体）在花丛中翩翩起舞（环境描述），蝴蝶的翅膀在阳光下闪烁着五彩斑斓的光芒（动作）。背景是一片繁花似锦的景象。",
    "深夜的城市街头，一只流浪猫（主体）悄悄地穿过狭窄的巷子（环境描述），猫的眼睛在街灯的照射下显得格外明亮（动作）。背景是寂静无声的都市夜景。",
    "黎明的山巅，一只雄鹰（主体）展翅高飞在云雾缭绕的山峰之上（环境描述），鹰的翅膀在初升的阳光下显得格外有力（动作）。背景是一片壮丽的山川。",
    "傍晚的海边，一只海豚（主体）跃出波涛汹涌的海面（环境描述），海豚的身体在晚霞的映衬下显得格外灵动（动作）。背景是一片浩瀚的海洋。",
    "午夜的图书馆，一只老鼠（主体）悄悄地在书架间穿梭（环境描述），老鼠的尾巴在昏暗的灯光下显得格外细长（动作）。背景是一排排静谧的书架。",
    "清晨的果园，一只松鼠（主体）忙碌地在果树间跳跃（环境描述），松鼠的尾巴在晨露中显得格外蓬松（动作）。背景是一片生机勃勃的果园。",
    "黄昏的草原，一只野马（主体）自由地奔跑在广阔的草地上（环境描述），马的鬃毛在风中飘扬，显得格外狂野（动作）。背景是一望无垠的草原。",
    "深夜的森林，一只狐狸（主体）悄悄地穿过茂密的灌木丛（环境描述），狐狸的耳朵在月光下显得格外灵敏（动作）。背景是一片神秘的森林。"
]
    
    total_elapsed_time = 0
    for p in prompt:
        elapsed_time = generate_video(p)
        total_elapsed_time += elapsed_time
    
    average_elapsed_time = total_elapsed_time / len(prompt)
    print(f"平均视频生成耗时: {average_elapsed_time:.2f} 秒")