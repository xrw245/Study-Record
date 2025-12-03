# 暴力求解，两次遍历
# 以每个字符作为起点，添加新的字符到新字符串中，到重复的字符串截至
# 比较字符串的长度，选择最大的，即得到最长的不重复字符串长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        str_length_max = 0
        for i in range(0, length):
            s_temp = ""
            for j in range(i, length):
                if s[j] not in s_temp:
                    s_temp += s[j]
                else:
                    break
            str_length_max = len(s_temp) if len(s_temp) > str_length_max else str_length_max
        return str_length_max

# 一次遍历
# 寻找相同字母的间隔,并将最后一个字母的位置储存在字典中
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res
  
