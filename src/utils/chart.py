import numpy as np
import matplotlib.pyplot as plt

# data: { values[], labels: [], colors: [] }
def create_pie_chart(data):
    print(data)

    plt.pie(data['values'], labels=data['labels'], counterclock=False, startangle=90, colors=data['colors'])
    plt.show()
    