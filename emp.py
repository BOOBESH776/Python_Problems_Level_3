def emp(emp_n,emp_s):
    m = emp_n[0]
    c = 0
    for i in range(0,len(emp_s)):
        if m < em_n[i]:
            m = em_n[i]
            c = i

    return emp_n[i]

em_n = ['Arun','priya','Karthik','Divya']
em_s = [25000,40000,30000,45000]
print(emp(em_n,em_s))