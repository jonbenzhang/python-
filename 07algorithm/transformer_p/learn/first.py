from transformers import pipeline

# classifier = pipeline("sentiment-analysis")
from transformers import AutoTokenizer, AutoModel

p = "/Users/zhangmeng/myproject/source_code/python/model/chatglm-6b"
c = pipeline( model=p)
c("你好")
# tokenizer = AutoTokenizer.from_pretrained(p, trust_remote_code=True)
