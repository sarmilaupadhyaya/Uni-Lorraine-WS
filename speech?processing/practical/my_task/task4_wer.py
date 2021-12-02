from matplotlib import pyplot as plt
import math


def get_confidence_interval(wer, words):
    x = wer/100
    print(x)
    return round(1.96 * math.sqrt((x * (1-x))/words), 2) * 100


# this was for man with 35 SNR db data with 5 different models
language_models = ["SNR35", "SNR25", "SNR15", "SNR05"]
wer = [10.5,11.5, 18, 62.5]
words = [200,200,200,200,200]
#some confidence interval
ci = [ get_confidence_interval(w,i) for w, i in zip(wer, words)]

fig, ax = plt.subplots()


ax.errorbar(x=language_models, y=wer, yerr=ci, color="red", capsize=5,
             linestyle="None",
             marker="s", markersize=7, mfc="green", mec="blue")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.xlabel("Noise level", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to noise level for 1 digit", fontsize=12)
plt.savefig('my_task/task_4_1digit.png',dpi=300)
plt.show()


# this was for man with 35 SNR db data with 5 different models
language_models = ["SNR35", "SNR25", "SNR15", "SNR05"]
wer = [15,16.6,19.67,64.33]
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

plt.xlabel("Noise level", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to noise level for 3 digits", fontsize=12)
plt.savefig('my_task/task_4_3digit.png',dpi=300)
plt.show()


# this was for man with 35 SNR db data with 5 different models
language_models = ["SNR35", "SNR25", "SNR15", "SNR05"]
wer = [11.2,11.4,16.08,57.2]
words = [200,200,200,200,200]
#some confidence interval
ci = [ get_confidence_interval(w,i) for w, i in zip(wer, words)]

fig, ax = plt.subplots()


ax.errorbar(x=language_models, y=wer, yerr=ci, color="red", capsize=5,
             linestyle="None",
             marker="s", markersize=7, mfc="green", mec="blue")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.xlabel("Language Models", fontsize=12)

plt.ylabel("Word Error Rate (%)", fontsize=12)
plt.title("Performance of ASR System with respect to noise level for 5 digits", fontsize=12)
plt.savefig('my_task/task_4_5digit.png',dpi=300)
plt.show()

