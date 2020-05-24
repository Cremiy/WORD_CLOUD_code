# encoding=utf-8
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

Texts = ''
f = open('inputtext/englishtext.txt','r',encoding='utf-8').read()


for id in range(3,20,1):
    image = Image.open('backgroundimage/color'+str(id+1)+'.jpg')
    graph = np.array(image)
    print(graph.shape)

    wc = WordCloud(font_path='Fonts/timesbd.ttf',background_color='white',max_words=1000,mask=graph).generate(f)

    image_color = ImageColorGenerator(graph)

    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis('off')
    plt.show()
    wc.to_file('outputimage/englishanswer'+str(id+1)+'.png')
