
# coding: utf-8

# In[13]:


import string
def main(filename) :
    txtfile = open(filename)
    text = txtfile.read()
    from collections import Counter
    unprocess_file=list(text.replace("\n", " ").split(" "))
    list_file = []
    translator = str.maketrans('', '', string.punctuation)
    for word in unprocess_file:
        word = word.translate(translator)
        if word != "" :
            list_file.append(word)
    counter = Counter(list_file)
    counter.most_common()
    import csv
    with open('wordcount.csv', 'w', newline='') as fin:
        writer = csv.writer(fin, delimiter=',')
        writer.writerow(['word','count'])
        for idx, val in counter.most_common():
            writer.writerow([idx, val])
            
    import json
    json.dump(counter.most_common(), open("wordcount.json", 'w'))
            
    import pickle
    with open('wordcount.pkl', 'wb') as fil:
        pickle.dump(counter.most_common(), fil)
            
if __name__ == '__main__':
    main("i_have_a_dream.txt")

