import streamlit as st
from storage import init_db,load,save
from model import Application

init_db()
st.title("求职记录管理器")
company=st.text_input("请输入公司名：")
position=st.text_input("请输入岗位名：")
date=st.text_input("请输入日期：")
status=st.selectbox("状态",["已投","笔试","面试","挂","Offer"])

if st.button("添加记录"):
    if not company or not position or not date:
        st.error("公司、岗位、日期不能为空")
    else:
        record=Application(company,position,date,status)
        records=load()
        records.append(record.to_dict())
        save(records)
        st.success("添加成功")

st.subheader("所有记录")
records=load()
if not records:
    st.warning("还没有记录")
else:
    st.dataframe(records)

st.subheader("状态统计")
if records:
    stats={}
    for record in records:
        status=record["status"]
        stats[status]=stats.get(status,0)+1
    st.bar_chart(stats)
else:
    st.warning("还没有记录")
