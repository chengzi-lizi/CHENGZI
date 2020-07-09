# coding=utf-8

from __future__ import division

def average_score(grade_table):
    """
    平均分.
    """
    scores = [score for score in grade_table.values()]
    average = sum(scores)/len(scores)
    return average

def rank_score(grade_table):
    """
    对成绩从高到低排序.
    """
    new_table = [(grade_table[score],score) for score in grade_table]
    rank_table = sorted(new_table, reverse=True)
    return rank_table

def max_score(grade_table):
    """
    第一名.
    """
    first = rank_score(grade_table)
    max_score = first[0][0]
    return [(i,j) for i in grade_table if i==max_score]

def min_score(grade_table):
    """
    倒数第一名.
    """
    end = rank_score(grade_table)
    min_score = end[-1][0]
    return [(i,j) for i in grade_table if i==min_score]

examine_scores = {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}

ave = average_score(examine_scores)
print("平均成绩: ",ave)

sor = rank_score(examine_scores)
print("成绩表: ",sor)

xueba = max_score(examine_scores)
print("第一名是: ",xueba)

xuezha = min_score(examine_scores)
print("最后一名是: ",xuezha)
