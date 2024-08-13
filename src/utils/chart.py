import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.font_manager
# print([f.name for f in matplotlib.font_manager.fontManager.ttflist])

plt.rcParams['font.family'] = 'Yu Gothic'

# data: { values[], labels: [], colors: [] }
def get_double_pie_chart(data1, data2, output_path):

    # outer pie chart
    plt.pie(
        data2['values'],
        counterclock=False,
        startangle=90,
        radius=1,
        colors=data2['colors'],
    )
    plt.axis('equal')

    # inner pie chart
    plt.pie(
        data1['values'],
        # labels=data1['labels'],
        counterclock=False,
        startangle=90,
        radius=0.7,
        # labeldistance=0.7,
        colors=data1['colors'],
        # wedgeprops={'linewidth': 2,'edgecolor':"white"},
        # textprops={'color': "black", 'fontsize':8},
        pctdistance=0.5,
        # autopct="%.1f%%",
    )
    plt.axis('equal')

    # center white circle
    center_circle = plt.Circle((0,0),0.4,color='white', fc='white',linewidth=1.25) #中心(0,0)に40%の大きさで円を描画
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    plt.savefig(output_path)

# data: { values[], labels: [], colors: [] }
def get_pie_chart(data1, output_path):
    plt.clf()

    # inner pie chart
    plt.pie(
        data1['values'],
        labels=data1['labels'],
        counterclock=False,
        startangle=90,
        radius=0.7,
        labeldistance=1.3,
        colors= data1['colors'] if 'colors' in data1 else None,
        wedgeprops={'linewidth': 2,'edgecolor':"white"},
        textprops={'color': "black", 'fontsize':8},
        pctdistance=0.8,
        autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.5 else '',
    )


    plt.axis('equal')

    plt.savefig(output_path)
