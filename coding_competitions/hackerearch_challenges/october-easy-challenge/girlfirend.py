# Parsing input arguements
demand = raw_input()
demand_len = len(demand)
num_questions = int(raw_input())
indexes = [(0, 0)] * num_questions
for one_question in range(num_questions):
    indexes[one_question] = (int(i) - 1 for i in raw_input().split())

# Computing yess and nos
#print "demand = %s\nnum_questions = %d" %(demand, num_questions)
#print "indexes are the following:", indexes

for (i, j) in indexes:
    if demand[i%demand_len] == demand[j%demand_len]:
        print 'Yes'
    else:
        print 'No'

