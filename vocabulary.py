import easygui as g
import random
import pickle

g.msgbox("哎呦，不错呦！知道学习了",ok_button="那绝对是当然的了！")
flag=g.buttonbox(msg='那么现在你想干什么哪？',choices=('背单词','添加新单词','听写单词'))
if flag=='背单词':
    pickle_file = open("word_list.pkl", "rb")
    temp = pickle.load(pickle_file)
    word_list_len = len(temp)
    temp_flag = 0
    while True:
        if temp_flag == 0:
            num = random.randint(1, word_list_len) - 1
        temp3 = g.enterbox(msg=temp[num], title='请输入单词')
        temp1 = temp[num].split()
        temp2 = temp1[0]
        # print(temp3)
        if temp3 == temp2:
            g.msgbox("答对了哦！", ok_button="继续")
            temp_flag = 0
        elif temp3 == None:
            temp_flag = 0
            break
        else:
            temp_flag = 1

elif flag=='添加新单词':
    while True:
        try:
            pickle_file1 = open("word_list.pkl", "rb")
            word_list = pickle.load(pickle_file1)
            pickle_file2 = open("word_list.pkl", "wb")
        except :
            word_list = []
            pickle_file2 = open("word_list.pkl", "wb")
        finally:
            word = g.enterbox(msg='请输入单词', title='添加单词')
            if word==None:
                pickle.dump(word_list, pickle_file2)
                pickle_file2.close()
                break
            elif word=='':
                pickle.dump(word_list, pickle_file2)
                pickle_file2.close()
            else:
                word_list = word_list + [word]
                pickle.dump(word_list, pickle_file2)
                pickle_file2.close()

elif flag=="听写单词":
    pickle_file = open("word_list.pkl", "rb")
    temp = pickle.load(pickle_file)
    word_list_len = len(temp)
    temp_flag = 0
    while True:
        if temp_flag == 0:
            num = random.randint(1, word_list_len) - 1
        temp1 = temp[num].split()
        temp2 = temp1[0]
        temp3 = g.enterbox(msg=temp1[1], title='请输入单词')
        # print(temp3)
        if temp3 == temp2:
            g.msgbox("答对了哦！", ok_button="继续")
            temp_flag = 0
        elif temp3 == None:
            temp_flag = 0
            break
        else:
            temp_flag = 1




