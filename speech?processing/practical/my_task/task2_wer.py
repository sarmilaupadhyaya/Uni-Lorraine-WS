from matplotlib import pyplot as plt
import math


def get_confidence_interval(wer, words):
    x = wer/100
    print(x)
    return round(1.96 * math.sqrt((x * (1-x))/words), 2) * 100


# this was for man with 35 SNR db data with 5 different models
language_models = ["Man-1digit","Man-3Digit","Man-5Digit", "Woman-1digit","Woman-3Digit","Woman-5Digit","Girl-1digit","Girl-3Digit","Girl-5Digit","Boy-1digit","Boy-3Digit","Boy-5Digit"]
wer = [10.5, 15, 11.2, 10.5, 10, 7.8, 24, 22.33, 26.8, 17.5,20,18]
words = [200,300,500,200,300,500,200,300,500,200,300,500]
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
plt.title("Performance of ASR System with respect to speaker group", fontsize=12)
plt.savefig('task_2.png',dpi=300)
plt.show()
