# encoding=utf-8
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

Texts = ''
f = open('inputtext/input.txt','r',encoding='utf-8')
for i in f:
    Texts += f.read()

result = jieba.analyse.textrank(Texts, topK=1000,withWeight=True)

keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)
id = 0
image = Image.open('backgroundimage/color'+str(id+1)+'.jpg')
graph = np.array(image)
print(graph.shape)

wc = WordCloud(font_path='msyhbd.ttc',background_color='white',max_words=1000,mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis('off')
plt.show()
wc.to_file('outputimage/answer'+str(id+1)+'.png')