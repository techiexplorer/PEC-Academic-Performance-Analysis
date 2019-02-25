from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def by_grade(file):
    plot_nos = [521,522,523,524,525,526,527,528,529,5210]
    global grades,students,subjects    
    final_subjects = []
    #file = r'I year II sem Regular April 2017.xls'
    df = pd.read_excel(file, skiprows=list(range(3)))
    subjects = df['Sub Name'].unique()
    grades = list(df['Grade'].unique())
    students = len(df['HT No'].unique())

    num_subjects = len(list(subjects))
        
    final_plots = []
    for i in range(num_subjects):
            final_plots.append("p"+str(i))
    #print("lol: ", final_plots)
    fig = plt.figure(figsize=(5,2))
    #fig.set_title(file)

    

    
    #print(final_plots)
    #sub=subjects[0]
    axis_subjects = []
    global part
    part = 0
    def cal(sub):
        global part,grades,subjects,students
    #for sub in list(subjects):
        #print('part: ',part)

        part+=1
        #print("Subject: ", sub)
        num_grades=[]
        row = []
        rows = len(df['HT No'])
        num_grades=[]
        for i in range(rows):
            #print("i ",i)
            q = df.iloc[i]
            if(q[3]==sub):
                #print(q[3])
                row.append(list(q))
            else:
                pass
        #print(grades)
        #print(sub)
        for grad in grades:
            #print("Grade: ", grad)
            temp = []
            for record in row:
            #for grad in grades:
                val = record.count(grad)
                if(val==1):
                    temp.append(val)
            #print("Num of students: ",len(temp))
            num_grades.append(len(temp))
        
        # Plotting inside

        #print("f: ",final_plots, "  p: ",plot_nos)

        #if(part>0):
        #    final_plots.remove(final_plots[part])
        #    print("final plots : ",final_plots )
        
        #print('part no.',part)
        #final_plots[part] = fig.add_subplot(plot_nos[part])
        if(plot_nos[part-1]==5210):
            catch = fig.add_subplot(5,2,10)
            catch.set_title(list(subjects)[len(list(subjects))-1])
        else:
            catch = fig.add_subplot(plot_nos[part-1])

            catch.set_title(list(subjects)[part-1])
            
            #catch.set_yticks(num_grades[part])
            #catch.title(sub)
        return (catch,grades,num_grades)

        #print(plot_nos[part-1])
    for sub in list(subjects):
        tup = cal (sub)
        return_catch = tup[0]
        grades = tup[1]
        num_grades = tup[2]

        new_xlabel = []
        for i in range(len(grades)):
            new_xlabel.append(str(grades[i])+str(' - ')+str(num_grades[i]))
        
        #rects = 
        #labels = tup[2]

        #return_catch.set_yticks(num_grades)
        return_catch.bar( new_xlabel, num_grades)
        #return_catch.title(sub)
        #final_plots[part].plot(grades, num_grades)
        #final_plots[part].title(sub)

        #print("Hello")
        #print(final_plots[part-1],final_plots[0])

    #plt.title(file)
    plt.subplots_adjust(left=0.04, bottom=0.06, right=0.98, top=0.96, wspace=0.07, hspace=0.66)
    plt.show()
    #print(final_plots[1])

#file = 'III year I sem Regular Oct 2018.xls'
#by_grade('I year II sem Regular April 2017.xls')




