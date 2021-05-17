#with open('how.docx', encoding ='latin-1') as f: #dont work, why?
f = open("how.docx", encoding="latin-1")
m_string = f.read()
count_the = m_string.count('the')
count_e = m_string.count('e')
count_if = m_string.count('if')
f.close()
res_file = open("statistics.txt", "w")
res_file.write("Count of 'the' = " + str(count_the) + '\n')
res_file.write("Count of 'if' = " + str(count_e) + '\n')
res_file.write("Count of 'e' = " + str(count_if) + '\n')
res_file.close()
# next 3 line printed the result for see in terminal
print(count_the)
print(count_e)
print(count_if)



