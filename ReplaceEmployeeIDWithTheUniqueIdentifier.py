# Method 1
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    uni_dict = {}
    for i in range(len(employee_uni)):
        uni_dict[employee_uni['id'][i]] = employee_uni['unique_id'][i]
    
    print(uni_dict)

    result = []
    for i in range(len(employees)):
        id = employees['id'][i]
        name = employees['name'][i]

        if id in uni_dict:
            result.append([uni_dict[id],name])
        else:
            result.append([None, name])
    
    return pd.DataFrame(result, columns = ['unique_id','name'])



# Method 2
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, on = 'id', how = 'left')

    return df[['unique_id','name']]