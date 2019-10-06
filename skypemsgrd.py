from skpy import Skype
from skpy import SkypeTextMsg
import re

sk = Skype(user = "oneteam.dev", pwd = "yourpassword")

for con in sk.contacts["live:3e61b0bd8642cb01"].chat.getMsgs():
    if con.type == "RichText":
        stm = SkypeTextMsg()
        stm.content = con.content
        text = re.sub(r"</?(e|b|i|ss?|pre|quote|legacyquote)\b.*?>", "", con.content)
        text = re.sub(r"""<a\b.*?href="(.*?)">.*?</a>""", r"\1", text)
        text = re.sub(r"""<at\b.*?id="8:(.*?)">.*?</at>""", r"@\1", text)
        text = (text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", "\"").replace("&apos;", "'"))
        print text
