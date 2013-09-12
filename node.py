__author__ = 'shengyinwu'

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

class node:
    def __init__(self, content):
        self.content = content
        self.lcs = ''
        self.pureness = 0
        self.prefix_ratio = 1
        self.lcs_length = 0

    def calculate_LCS(self, head_title):
        self.lcs = longest_common_substring(self.content, head_title)
        self.lcs_length = len(self.lcs)

    def calculate_pureness(self, head_title):
        self.pureness = float(self.lcs_length) / (len(head_title))

    def calculate_prefix_ratio(self):
        try:
            self.prefix_ratio = self.content.find(self.lcs)
        except(ValueError):
            self.prefix_ratio = 1000000
