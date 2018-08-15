import pandas as pso


Student={'Name':["ASAD","Tanveer","Ejaz"],'Programme':["BSCS","BSEE","LLB"]}

x=pso.DataFrame(Student)
x.to_csv('student.csv')
