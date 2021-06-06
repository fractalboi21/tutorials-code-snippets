from pywebio.output import put_text, put_table
import json
import temp
from numerize import numerize

data = []
vid = ["owe9cPEdm7k","B1ouIlaGlQg","sW9npZVpiMI"]
for i in vid:
    val = temp.getParsedJsonResponse(i)
    val["view_count"] = numerize.numerize(int(val["view_count"]))
    data.append(val)

# put_table([
#     {"Course":"OS", "Score": "80"},
#     {"Course":"DB", "Score": "93"},
# ], header=["Course", "Score"])
put_table(data,header=["video_title","duration","view_count","like_count", "dislike_count"])


