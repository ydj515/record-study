import re

"""
텍스트, 정규식 -> []
bs_obj.text, "셀트리온[가-힣0-9a-zA-Z]*" -> ["셀트론", "셀트리온", "셀트리온스킨큐어" ...]
"""

def find_matched_texts(text, regexp):
    matched = re.findall(regexp, text)
    # print(len(matched))
    return matched