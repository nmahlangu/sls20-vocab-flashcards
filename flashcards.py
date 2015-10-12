import os
import random

# these text files will be read into memory upon program start
chapters = ['chapter3.txt', 'chapter4.txt', 'chapter6.txt', 'chapter7.txt', 'chapter8.txt', 'chapter13.txt']

# converts a textfile into a dictionary
def chapter_to_dict(filename):
    path_to_chapters = "./chapters/"
    full_path = path_to_chapters + filename
    if not os.path.exists(full_path):
        raise Exception("File at %s does not exists" % (full_path))
    
    words = {}
    for line in open(path_to_chapters+filename,"r"):
        tmp = line.split(":")
        word = tmp[0]
        desc = tmp[1].replace("\n","").lstrip()
        words[word] = desc
    return words

# creates a dictionary where key is a chapter, value is a dictionary of words
# and definitions
def load_chapters():
    d = {}
    for chapter in chapters:
        d[chapter] = chapter_to_dict(chapter)
        print "Loaded Chapter %s" % (chapter.replace("chapter","").replace(".txt",""))
    return d

# randomly picks words from the dictionary to display to the user
def practice(chapter_num,d):
    keys = d.keys()
    print "*****************************************************************"
    print "Practicing with Chapter %d, there are %d vocabulary words" % (chapter_num,len(keys))
    print "Once the words is displayed, press any key to see the definition"
    print "*****************************************************************"
    while keys:
        key = random.choice(keys)
        print "%s" % (key),
        raw_input("")
        print "-> %s" % (d[key])
        del keys[keys.index(key)]
        raw_input("")
    print "********************************************"
    print "Done with Chapter %d, returning to main menu" % (chapter_num)
    print "********************************************"
 

# load chapters into memory
chapter_dict = load_chapters()

# repeatedly ask the user what chapter they want to practice with
print "****************************************"
while 1:
    print "Available chapters: ", [int(ch.replace("chapter","").replace(".txt","")) for ch in chapters]
    chapter_num = raw_input("Enter chapter number: ")
    try:
        chapter_num = int(chapter_num)
    except:
        print "Invalid input, enter a single number."
        continue

    if chapter_num not in [int(ch.replace("chapter","").replace(".txt","")) for ch in chapters]:
        print "Invalid number, try again."
    else:
        chapter_key = "chapter" + str(chapter_num) + ".txt"
        practice(chapter_num, chapter_dict[chapter_key])
