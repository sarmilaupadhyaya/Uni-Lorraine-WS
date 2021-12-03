from matplotlib import pyplot as plt
import math


def get_confidence_interval(wer, words):
    x = wer/100
    print(x)
    return round(1.96 * math.sqrt((x * (1-x))/words), 2) * 100


# this was for man with 35 SNR db data with 5 different models
language_models = ["Man", "Woman","Girl","Boy"]
wer = [10.5,10.5, 24, 17.5]
words = [200,200,200,200]
#some confidence interval
ci = [ get_confidence_interval(w,i) for w, i in zip(wer, words)]

fig, ax = plt.subplots()


ax.errorbar(x=language_models, y=wer, yerr=ci, color="red", capsize=5,
             linestyle="None",
             marker="s", markersize=7, mfc="green", mec="blue")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.xlabel("Speaker Group", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to speaker group for 1 digit", fontsize=12)
plt.savefig('results/figures/task_2_1.png',dpi=300)
plt.show()




# this was for man with 35 SNR db data with 5 different models
language_models = ["Man", "Woman","Girl","Boy"]
wer = [15,10, 22.6, 20]
words = [300,300,300,300]
#some confidence interval
ci = [ get_confidence_interval(w,i) for w, i in zip(wer, words)]

fig, ax = plt.subplots()


ax.errorbar(x=language_models, y=wer, yerr=ci, color="red", capsize=5,
             linestyle="None",
             marker="s", markersize=7, mfc="green", mec="blue")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.xlabel("Speaker Group", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to speaker group for 3 digits", fontsize=12)
plt.savefig('results/figures/task_2_2.png',dpi=300)
plt.show()


# this was for man with 35 SNR db data with 5 different models
language_models = ["Man", "Woman","Girl","Boy"]
wer = [11.31,7.8,26.8,18]
words = [200,200,200,200]
#some confidence interval
ci = [ get_confidence_interval(w,i) for w, i in zip(wer, words)]

fig, ax = plt.subplots()


ax.errorbar(x=language_models, y=wer, yerr=ci, color="red", capsize=5,
             linestyle="None",
             marker="s", markersize=7, mfc="green", mec="blue")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.xlabel("Speaker Group", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to speaker group for 5 digits", fontsize=12)
plt.savefig('results/figures/task_2_3.png',dpi=300)
plt.show()
