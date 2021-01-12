def txt_count(file):
    text = open(file, 'r')

    d = dict()

    for line in text:
        line = line.strip()

        line = line.lower()

        words = line.split(" ")

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1


    end_dict = sorted(d.items() ,  key=lambda x: x[1])
    for elem in end_dict:
        print(elem[0], " ::", elem[1] )