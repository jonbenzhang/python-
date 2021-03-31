"""
68. 文本左右对齐
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
"""
"""
方式1 贪心算法
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results = []
        result = []
        counts = 0
        i = 0
        while i < len(words):
            word_len = len(words[i])
            if word_len + counts + len(result) <= maxWidth:
                counts += word_len
                result.append(words[i])
                i += 1
            else:
                if i != len(words):
                    space_num = maxWidth - counts
                    if len(result) == 1:
                        results.append(result[0] + " " * (maxWidth - counts))
                    else:
                        a, b = divmod(space_num, len(result) - 1)
                        results.append((" " * (a + 1)).join(result[:b + 1]) + " " * a + (" " * a).join(result[b + 1:]))
                    counts = 0
                    result = []
                    continue
            if i == len(words):
                results.append(" ".join(result) + " " * (maxWidth - counts-len(result)+1))
        return results


if __name__ == '__main__':
    a = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    b = 20
    s = Solution()
    print(s.fullJustify(a, b))
