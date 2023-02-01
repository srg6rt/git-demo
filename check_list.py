#!/usr/bin/env python
# coding: utf-8

# In[43]:


def read_song_file():
    with open('song.txt') as f:
        mylist = f.read().splitlines()
    return mylist


def read_readme_file():
    with open("README.md", "r") as fp:
        list_of_songs_from_readme = fp.readlines()
    return list_of_songs_from_readme


def write_to_readme_file(newLIst):
    with open("README.md", "w") as fp:
        fp.writelines(newLIst)


def update_readme_file():
    new_list_README = []
    list_of_songs = read_song_file()
    for i in list_of_songs:
        
        for count, value in enumerate(read_readme_file()):
            #Search song name in README.md
            if i in value: # If song name in README.md break statement for count number different from len(list_of_songs)
                new_list_README.append(value)
                break
            else:
                # Add song name witch NOT in README.md, by compare count number and len(list_of_songs)
                # If count number == len(list_of_songs) it's mean thet for loop search NOT find song name in README.md
                if len(read_readme_file()) == count+1:
                    new_list_README.append('- <a href=" " target="_blank">'+i+'</a>\n')
                    #print("RESULT ELSE - ",i)
                    #print(len(read_readme_file()), count+1)
                
    return list(dict.fromkeys(new_list_README))

write_to_readme_file(update_readme_file())


# In[ ]:




