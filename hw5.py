
# coding: utf-8

# In[3]:


import string
def main(filename) :
    txtfile = open(filename)
    text = txtfile.read()
    from collections import Counter
    list_file = []
    for line in open(filename):
        line = line.strip()
        if not line:
            continue
        for word in line.split():
            word = word.strip(string.punctuation)
            if word:
                list_file.append(word)
    counter = Counter()
    counter.update(list_file)
    counter.most_common()
    import csv
    with open('wordcount.csv', 'w', newline='') as fin:
        writer = csv.writer(fin, delimiter=',', lineterminator='\n')
        writer.writerow(['word']+['count'])
        for idx, val in counter.most_common():
            writer.writerow([idx, val])
            
    import json
    json.dump(counter.most_common(), open("wordcount.json", 'w'))
            
    import pickle
    with open('wordcount.pkl', 'wb') as fil:
        pickle.dump(counter, fil)
            
if __name__ == '__main__':
    main("i_have_a_dream.txt")



