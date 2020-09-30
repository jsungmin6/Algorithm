#가장 흔한 단어

'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

#풀이 방법

'''
1.ban글자를 제외하고 단어 리스트를 만듬
2.단어리스트 중에 가장 많은 단어를 선택
3.출력
'''

# # # # # # # # # # # # # #

import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word]+=1

        return max(counts,key=counts.get)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[word for word in re.sub('[^\w]',' ',paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
