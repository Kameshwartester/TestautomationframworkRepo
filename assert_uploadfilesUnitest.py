from itertools import count

import pytest
import pandas as pd
def test_checkDuplicate():
    target_df=pd.read_csv("target.csv",sep=",")
    count=target_df.duplicated().sum()
    assert count==0,"Duplicate-please check once"
def test_dataCompletness():
    target_df=pd.read_csv('target.csv')
    assert not target_df.empty," please check files "
def testDepartmentforNull_value():
    target_df=pd.read_csv('target.csv')
    isdeptnoNull=target_df['deptno'].isnull().any()
    assert isdeptnoNull==False,"Department is having null please check"
def test_employeenoUniquevalue():
    target_df=pd.read_csv('target.csv')
    totalcount=target_df['eno'].count()
    print(f"\n total count: {totalcount}")
    emplyoeeUniqecount=len(target_df['eno'].unique())
    print(f"total emp unique : {emplyoeeUniqecount}")
    assert totalcount==emplyoeeUniqecount,"Employee's isnot unique"