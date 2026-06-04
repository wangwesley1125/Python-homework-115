'''
4.	Ask the user to enter 10 students’ name and 3 scores, and put every student’s [name, score1, score2, score3, average] 
into a list, e.g., list1= [['tom', 60,70,65,65], ['marry', 85,90,80,85], …].
Sort list1 according to students’ average scores, and print rank, name, average

1 	marry 	85
2 	jane  	83

'''

list1 = [['tom', 60, 70, 65, 65], 
         ['marry', 85, 90, 80, 85],
         ['jane', 80, 85, 84, 83],
         ['bob', 70, 75, 80, 75],
         ['alice', 90, 95, 92, 92],
         ['john', 65, 70, 68, 67.67],
         ['susan', 88, 92, 90, 90],
         ['mike', 78, 82, 80, 80],
         ['lisa', 85, 87, 90, 87.33],
         ['dave', 72, 78, 75, 75]]

list1.sort(key=lambda x: x[4], reverse=True)

rank = 0 # 排名

for row in list1:
    rank += 1
    print(str(rank) + "\t" + str(list1[rank-1][0]) + "\t" + str(list1[rank-1][4]))
    