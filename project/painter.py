
import json        # 词典：负责把文本变成 Python 能看懂的“列表”
import requests    # 快递员：负责去网上把图片取回来
import urllib.parse # 翻译官：负责把网址里的空格、逗号变成网址能懂的编码

def 画师_Pollinations(剧本串):
    # 【第一步：亮出身份】
    # sk_ 是你的 Secret Key (秘密钥匙)。Bearer 后面必须有个空格！
    API_KEY = "sk_G2JmbnGveMqKRZZqrYdbtLtrBvtRkqmg" 
    请求头 = {
        "Authorization": f"Bearer {API_KEY}"
    }

    # 【第二步：拆解剧本】
    # 把 Gemini 给你的那串文字变成真正的“任务清单”
    任务清单 = json.loads(剧本串)
    
    # 【第三步：排队领画】
    for 任务 in 任务清单:
        序号 = 任务["序号"]
        描述 = 任务["画面描述"]
        
        # 3a. 翻译描述：网址里不能有空格，quote 会把它变成 %20 之类的代码
        画风 = "stickman style, white background, "
        编码后的描述 = urllib.parse.quote(画风 + 描述)
        
        # 3b. 拼凑地址：这就是官网说的那个 URL
        网址 = f"https://gen.pollinations.ai/image/{编码后的描述}"
        
        print(f"🎨 正在画第 {序号} 张...")

        # 3c. 派快递员去拿图：因为不需要代理，直接 get(网址, headers=请求头)
        响应 = requests.get(网址, headers=请求头)
        
        # 【第四步：把画收进抽屉】
        # 如果响应码是 200 (代表成功)，就保存图片

        with open(f"step_{序号}.png", "wb") as 文件:
            文件.write(响应.content) # 把下载的二进制数据写进文件
        print(f"✅ 第 {序号} 张画好了！")





画师_Pollinations(
"""[
    {
        "序号": 1,
        "画面描述": "A man holds a long rope at a tree. A goat is at the grass, and the rope is at the goat.",
        "英文句子": "The man holds the long rope at the tree and the goat."
    },
    {
        "序号": 2,
        "画面描述": "The goat goes away from the tree. The rope is tight and short. The goat is not at the grass.",
        "英文句子": "The goat goes away, but the rope is short."
    },
    {
        "序号": 3,
        "画面描述": "The man uses the rope to tether the goat at the tree. The goat is at the tree.",
        "英文句子": "The man tethers the goat at the tree."
    },
    {
        "序号": 4,
        "画面描述": "The goat goes away, but the rope is at the tree and the goat. The goat is not away.",
        "英文句子": "The goat is tethered; the goat is not away."
    }
]"""
)
