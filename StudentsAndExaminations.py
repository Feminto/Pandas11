# Method 1
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    id_sub = {}
    for i in range(len(students)):
        stu = students['student_id'][i]
        name = students['student_name'][i]
        
        for n in range(len(subjects)):
            sub = subjects['subject_name'][n]
            id_sub[(stu,sub)] = name
    
    print(id_sub)

    exm = {}
    for i in range(len(examinations)):
        st = examinations['student_id'][i]
        sb = examinations['subject_name'][i]

        if (st,sb) in exm:
            exm[(st,sb)] += 1
        else:
            exm[(st,sb)] = 1

    print(exm)
    
    result = []
    for k,v in id_sub.items():
        cnt = 0
        if k in exm:
            cnt = exm[k]
        result.append([k[0],v,k[1],cnt])
    
    return pd.DataFrame(result, columns = ['student_id','student_name','subject_name','attended_exams']).sort_values(['student_id','subject_name'])


# Method 2
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    stu_sub = students.merge(subjects, how = 'cross')
    
    exm_cnt = examinations.groupby(['student_id','subject_name']).size().reset_index(name = 'attended_exams')

    df = stu_sub.merge(exm_cnt, on = ['student_id','subject_name'], how = 'left')
    df['attended_exams'] = df['attended_exams'].fillna(0)
    
    return df.sort_values(['student_id','subject_name'])