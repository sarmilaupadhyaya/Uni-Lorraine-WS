from matplotlib import pyplot as plt
import math


def get_confidence_interval(wer, words):
    x = wer/100
    print(x)
    return round(1.96 * math.sqrt((x * (1-x))/words), 2) * 100


# this was for man with 35 SNR db data with 5 different models
language_models = ["N-gram","1-Digit","3-Digit", "5-Digit", "DigitLoop"]
wer = [12,10.5,15,11.2,27]
words = [1000,200,300,500,1000]
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
plt.title("Performance of ASR System with respect to Langauge Model", fontsize=12)
plt.show()
