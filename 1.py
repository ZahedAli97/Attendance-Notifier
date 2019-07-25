import csv


def cal(row):
    # print(len(row))
    x=1
    res=0
    while(x<len(row)):
        # print(type(row[x]))
        if(row[x]!=''):
            res = res + int(row[x])
        # print(res)
        x+=1
    actlen = len(row)-1
    per = (float(res)/actlen)*100
    print(res,actlen,int(per))
    # if(per<75):
    #     perint = int(per)
    #     # print(row[0]+" has less attendance. It is only "+str(int(per))+"%.")
    #     maily(row[0],perint)


def maily(name,percentage):
   with open("mails.csv", "r") as file:
        msg_reader = csv.reader(file, delimiter=',')
        # print(msg_reader)
        # msg_reader.next()
        
        for row in msg_reader:
            if(row[0]==name):
                print(row[1],percentage)






def main():
   with open("mailtry.csv", "r") as file:
        msg_reader = csv.reader(file, delimiter=',')
        # print(msg_reader)
        # msg_reader.next()
        
        for row in msg_reader:
            cal(row)




if __name__ == '__main__':
     main()