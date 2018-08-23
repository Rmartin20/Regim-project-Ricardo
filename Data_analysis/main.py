import numpy as np
import matplotlib.pyplot as plt
import json

JSON_FILE = 'data.json'
_1 = 'method1'
_2 = 'exhaustive'
_3 = 'method3'
_4 = 'bspline1'
_5 = 'displacement'

with open(JSON_FILE) as f:
    data = json.load(f)

    data_1 = data[_1]
    data_2 = data[_2]
    data_3 = data[_3]
    data_4 = data[_4]
    data_5 = data[_5]

    samples = len(data_2)
    f.close()

data_1_norm = [(float(i)*10)/(-1) for i in data_1]
data_2_norm = [(float(i)*10)/(-1) for i in data_2]
data_3_norm = [(float(i)*10)/(-1) for i in data_3]
data_4_norm = [(float(i)*10)/(-1) for i in data_4]
data_5_norm = [(float(i)*10)/(-1) for i in data_5]

data_1_avg = sum(data_1_norm)/float(len(data_1_norm))
data_2_avg = sum(data_2_norm)/float(len(data_2_norm))
data_3_avg = sum(data_3_norm)/float(len(data_3_norm))
data_4_avg = sum(data_4_norm)/float(len(data_4_norm))
data_5_avg = sum(data_5_norm)/float(len(data_5_norm))

n_groups = 11

fig, ax = plt.subplots(1)

index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.4
error_config = {'ecolor': '0.3'}

rect_1 = ax.bar(index, data_2_norm, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label=_2)

rect_2 = ax.bar(index + bar_width, data_3_norm, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label=_3)

rect_3 = ax.bar(index + bar_width * 2, data_4_norm, bar_width,
                alpha=opacity, color='g',
                error_kw=error_config,
                label=_4)

rect_4 = ax.bar(index + bar_width * 3, data_5_norm, bar_width,
                alpha=opacity, color='m',
                error_kw=error_config,
                label=_5)

ax.set_xlabel('Sample')
ax.set_ylabel('Scores')
ax.set_title('Image registration metric analysis')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'))
ax.legend()

fig.tight_layout()
plt.show()

# ---------------------------------------------------------
n_groups = 1
fig, ax = plt.subplots(1)

index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.4
error_config = {'ecolor': '0.3'}
mean_1 = ax.bar(index, data_2_avg, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label=_2)

mean_2 = ax.bar(index + bar_width, data_3_avg, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label=_3)

mean_3 = ax.bar(index + bar_width * 2, data_4_avg, bar_width,
                alpha=opacity, color='g',
                error_kw=error_config,
                label=_4)

mean_4 = ax.bar(index + bar_width * 3, data_5_avg, bar_width,
                alpha=opacity, color='m',
                error_kw=error_config,
                label=_5)

ax.set_xlabel('Average')
ax.set_ylabel('Scores')
ax.set_title('Image registration metric analysis')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels('')
ax.legend()

fig.tight_layout()
plt.show()
