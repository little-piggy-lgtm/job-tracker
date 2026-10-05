from storage import save,load
from model import Application

VALID_STATUSES = ["已投","笔试","面试","挂","Offer"]

def input_non_empty(prompt):
    while True:
        user_input=input(prompt)
        user_input=user_input.strip()
        if user_input!="":
            return user_input
        else:
            print("输入不能为空")

def input_int(prompt):
    while True:
        try:
            user_input=int(input(prompt))
            return user_input
        except ValueError:
            print("请输入数字")

def add_record():
    records=load()
    company = input_non_empty("请输入公司名称：")
    position = input_non_empty("请输入职位名称：")
    date = input_non_empty("请输入申请日期（格式：YYYY-MM-DD）：")
    while True:
        status_input = input_non_empty("请输入状态（已投/笔试/面试/挂/Offer）：")
        if status_input in VALID_STATUSES:
            break
        print("状态不合法，请重新输入")
    app = Application(company, position, date, status_input)
    app = app.to_dict()
    records.append(app)
    save(records)
    print("添加成功")

def view_records():
    records=load()
    if len(records)==0:
        print("还没有记录")
    else:
        for i,record in enumerate(records,start=1):
            print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")

def update_record():
    records=load()
    if len(records)==0:
        print("还没有记录")
    else:
        for i,record in enumerate(records,start=1):
            print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")
        while True:
            num=input_int("输入要修改的记录：")
            if 1<=num<=len(records):
                break
            print("编号不存在")
        field=input_non_empty("请输入要修改的项目：(company/position/date/status)")
        if field=="company":
            new_company=input_non_empty("请输入更新的公司：")
            records[num-1]["company"]=new_company
            save(records)
            print("修改成功")
        elif field=="position":
            new_position=input_non_empty("请输入新岗位：")
            records[num-1]["position"]=new_position
            save(records)
            print("修改成功")
        elif field=="date":
            new_date=input_non_empty("请输入新的日期：")
            records[num-1]["date"]=new_date
            save(records)
            print("修改成功")
        elif field=="status":
            while True:
                status_input = input_non_empty("请输入状态（已投/笔试/面试/挂/Offer）：")
                if status_input in VALID_STATUSES:
                    break
                print("状态不合法，请重新输入")
            records[num-1]["status"]=status_input
            save(records)
            print("修改成功")
        else:
            print("输入修改项目不合法")

def delete_record():
    records=load()
    if len(records)==0:
        print("还没有记录")
    else:
        for i,record in enumerate(records,start=1):
            print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")
        while True:
            num=input_int("输入要删除的记录：")
            if 1<=num<=len(records):
                break
            print("编号不存在")
        del records[num-1]
        save(records)
        print("删除成功")

def show_stats():
    records=load()
    if len(records)==0:
        print("还没有记录")
    else:
        total=len(records)
        stats={}
        for record in records:
            status=record["status"]
            stats[status]=stats.get(status,0)+1
        print(f"总投递：{total}")
        for statu,num in stats.items():
                print(f"{statu}:{num}")

def search_records():
    records=load()
    if len(records)==0:
        print("还没有记录")
    keyword=input_non_empty("请输入关键词")
    results=[]
    for record in records:
        if keyword in record["company"] or keyword in record["position"]:
            results.append(record)
    if results==[]:
        print("没有匹配的记录")
    else:
        print(f"搜索结果为：{enumerate(results, start=1)}")
