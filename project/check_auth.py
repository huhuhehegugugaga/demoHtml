# from google import genai

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client(api_key="AIzaSyBzwY0QOkxX2E9b9POfbsyAyJdwIDGhBxI")

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="你好"
# )
# print(response.text)


from google import genai

# 1. 准备：建立办事处
# 记得换成你刚才申请的新 Key！
client = genai.Client(api_key="AIzaSyBzwY0QOkxX2E9b9POfbsyAyJdwIDGhBxI")

# 2. 加工：定义一个名为 translate_to_english 的函数
def translate_to_english(chinese_text):
    """
    这个函数负责把中文翻译成地道的英文
    """
    # 构造一个强力的指令（Prompt Engineering）
    prompt = f"直接翻译成英文和日文，不要有别的多余的东西：'{chinese_text}'"
    
    # 发送给 Gemini
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    # 返回翻译结果
    return response.text

# 3. 产出：调用函数并看结果
my_word = "我要炸地球"
english_result = translate_to_english(my_word)

print(f"中文：{my_word}")
print(f"{english_result}")