from ltp import LTP
ltp = LTP() # 默认加载 LTP/Small 模型

from ltp import StnSplit
sents = StnSplit().split("汤姆生病了。他去了医院。")
# [
#   "汤姆生病了。",
#   "他去了医院。"
# ]

sents = StnSplit().batch_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])

print(sents)
# [
#   "他叫汤姆去拿外衣。",
#   "汤姆生病了。",
#   "他去了医院。"
# ]
