import re
import jieba
import getpass
import requests
import wxpy
from pyquery import PyQuery
from mymodule import stats_word

response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()
text=content
    
#引入变量words和count，为图像化函数做好参数引入
dict_text=dict(stats_word.stats_text_cn(text,10)) #把结果转化字典
key_words=list(dict_text.keys())#把字典的key和对应值转换为列表
count_values=list(dict_text.values()) #把字典的value和对应值转换为列表

    
#用matplotlib把words和count图像化
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()
fig,ax = plt.subplots()
plt.rcParams['font.sans-serif']=['SimHei'] 
ax.barh(key_words,count_values, align = "center", color = "blue")
ax.set_yticks(key_words)
ax.set_yticklabels(key_words)
ax.invert_yaxis()
ax.set_xlabel(count_values)
ax.set_title('Top 10 words sorted by frequency')
plt.show()
plt.savefig('result.png')
