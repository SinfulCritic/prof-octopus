#defines function for use with main file
def txt_count(file):
    #opens userspecified file and adds content to 'text'
    text = open(file, 'r')

    #defines dictionary list
    d = dict()

    #Goes through every line in the text and strips it and lowers it creating individual words.
    for line in text:
        line = line.strip()

        line = line.lower()

        words = line.split(" ")

    #counts the word occurences
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

    #outputs text to console, needs better fix
    end_dict = sorted(d.items() ,  key=lambda x: x[1])
    for elem in end_dict:
        print(elem[0], " ::", elem[1] )