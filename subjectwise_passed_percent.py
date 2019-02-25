from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd

def subjectwise_passed_percentage(filename):
    file = filename
    df = pd.read_excel(file, skiprows=list(range(3)))
    subjects = list(df['Sub Code'].unique())
    passes = []
    passes_nums = []
    haha = []
    total_students = len(set(df['HT No']))
    for sub in subjects:
        sub_code = df["Sub Code"] == sub
        passed = df['Status'] == "PASS"
        z = df[sub_code & passed]
        nums=len(z)
        passes.append((nums/total_students)*100)
        passes_nums.append(nums)
        pass_value = [round(i,1) for i in passes] 
        subjects, pass_value
    ax = plt.subplot()
    ax.bar(subjects, pass_value, width=0.2, color='r',align='center')
    plt.title(filename + "  -  Subjectwise Pass% of Students")
    rects = ax.patches

    labels = zip(pass_value,passes_nums)

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, label,
                ha='center', va='bottom')
    plt.xticks(rotation=45)
    plt.yticks([i for i in range(0,110,10)])
    plt.ylabel(str('%') + " of Passed Students")
    #mng = plt.get_current_fig_manager()
    #mng.frame.Maximize(True)
    plt.show()

    
#subjectwise_passed_percentage('I year II sem Regular April 2017.xls')
