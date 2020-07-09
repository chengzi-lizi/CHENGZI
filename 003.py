# coding=utf-8

from __future__ import division
import random

scores = [random.randint(0,100) for i in range(40)]     #生成满足条件的列表
print(scores)
                             
average_score = sum(scores)/len(scores)                 #计算平均成绩                   
low_number = len([score for score in scores if score<average_score])
                                                        #低于平均成绩的人数                  
print("The average score is:%.1f." % average_score)
print("There are %d students less than average." % low_number)

print(sorted(scores, reverse=True))                      #排序成绩
