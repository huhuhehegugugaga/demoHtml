
# from google import genai

# # 1. 准备：建立办事处
# # 记得换成你刚才申请的新 Key！
# client = genai.Client(api_key="AIzaSyBzwY0QOkxX2E9b9POfbsyAyJdwIDGhBxI")

# # 2. 加工：定义一个名为 translate_to_english 的函数
# def translate_to_english(chinese_text):
#     """
#     这个函数负责把中文翻译成地道的英文
#     """
#     # 构造一个强力的指令（Prompt Engineering）
#     prompt = f"直接翻译成英文和日文，不要有别的多余的东西：'{chinese_text}'"
    
#     # 发送给 Gemini
#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=prompt
#     )
    
#     # 返回翻译结果
#     return response.text

# # 3. 产出：调用函数并看结果
# my_word = "我要炸地球"
# english_result = translate_to_english(my_word)

# print(f"中文：{my_word}")
# print(f"{english_result}")




from google import genai
import json

# 初始化你的 Gemini 办事处
client = genai.Client(api_key="AIzaSyBzwY0QOkxX2E9b9POfbsyAyJdwIDGhBxI")

def 编剧_Gemini(已知词库, 正在学的新词):
    """
    这个函数负责命令 Gemini 造句。
    输入示例：已知词库=["I", "am", "a", "man"], 新词="here"
    """
    
    # --- 核心：编写“铁律”指令 (Prompt) ---
    prompt = f"""
    你现在是一名严格的《English Through Pictures》教材编剧。
    
    【已知词库】：{已知词库}
    【正在学的新词】：{正在学的新词}
    
    任务要求：
    1. 造一个简单的英文句子，必须包含新词：'{正在学的新词}'。
    2. 铁律：句子中的每一个单词，必须【只能】来自“已知词库”或“正在学的新词”。
    3. 为这个句子设计一个极简的火柴人动作（Stickman），用来解释这个句子的意思。
    

    请严格按照以下 JSON 格式回答，不要有任何废话：
    {{
        "英文句子": "生成的句子",
        "画面描述": "描述火柴人的动作"
    }}
    """

    # --- 调用 Gemini ---
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    # --- 把 AI 返回的字符串变成 Python 字典 ---
    # 去掉 AI 可能带有的 ```json 这种外壳
    # 清理后的内容 = response.text.replace("```json", "").replace("```", "").strip()
    # return json.loads(清理后的内容)
    return response.text

# --- 让我们测试一下这个“编剧” ---
# 我的词库 = ["I", "am", "a", "man", "is", "it"]
# 新词 = "here"
我的词库 = ["this", "is" ,"are","fly","they","are","kill","zombie","very","when","people","die","war","sad","run","what","how","dream","drink","driver"]
新词 = "authority"

结果 = 编剧_Gemini(我的词库, 新词)

# print(f"生成的句子：{结果['英文句子']}")
# print(f"给画师的指令：{结果['画面描述']}")

print(结果)