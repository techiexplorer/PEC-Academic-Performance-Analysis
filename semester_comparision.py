from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def compare(file_list):

    

    f_list=[]
    df_list=[]

    for i in range(len(file_list)):
        f_list.append("f"+str(i))
        df_list.append("df"+str(i))
    print(f_list,df_list)

    

    for i in range(len(file_list)):
        f_list[i] = file_list[i]
        df_list[i] = pd.read_excel(f_list[i], skiprows=list(range(3)))

    percentages = []
    #semesters = [df1, df2, df3, df4, df5]
    semesters = [i for i in df_list]

    se = ['1-1','1-2','2-1','2-2','3-1','3-2','4-1','4-2']
    for all in semesters:
        cgpa = list((all['CGPA']))
        num_subjects = len(set(all['Sub Code']))
        num_students = len(set(all['HT No']))
        #subjects = list(all['Sub Name'].unique())
        count=0
        for i in cgpa:
            if(np.isnan(i)):
                count=count+1
        failed = count/num_subjects
        passed = num_students - failed
        pass_per = (passed/num_students)*100
        percentages.append(pass_per)


        
    plt.plot([se[i] for i in range(len(file_list))], percentages)
    #plt.title(i for i in subjects)
    plt.xlabel('Subject Codes')
    plt.ylabel('Percentage of students who passed all subjects')
    plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
    plt.title('Overall Performance of students in previous semesters')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

# ['C:/Users/farha/Documents/Confidential - Copy/I year I sem Regular Nov 2016.xls', 'C:/Users/farha/Documents/Confidential - Copy/I year II sem Regular April 2017.xls']

#compare(['C:/Users/farha/Documents/Confidential - Copy/I year I sem Regular Nov 2016.xls', 'C:/Users/farha/Documents/Confidential - Copy/I year II sem Regular April 2017.xls'])







