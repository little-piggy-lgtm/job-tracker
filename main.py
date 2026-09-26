from storage import load
from storage import save
from model import Application

VALID_STATUSES = ["已投", "笔试", "面试", "挂", "Offer"]
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
def main():
    records = load()
    while True:
        print("1.添加申请记录")
        print("2.查看申请记录")
        print("3.修改申请记录")
        print("4.删除申请记录")
        print("5.统计")
        print("6.退出")
        choice = input_non_empty("请输入操作编号：")
        if choice == "1":
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
        elif choice == "2":
            if len(records)==0:
                print("还没有记录")
            else:
                for i,record in enumerate(records,start=1):
                    print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")
        elif choice == "3":
            if len(records)==0:
                print("还没有记录")
            else:
                for i,record in enumerate(records,start=1):
                    print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")
                num=input_int("输入要修改的记录：")
                if 1<=num<=len(records):
                    field=input_non_empty("请输入要修改的项目：(company/position/date/status)")
                    if field=="company":
                        new_company=input_non_empty("请输入更新的公司：")
                        records[num-1]["company"]=new_company
                    elif field=="position":
                        new_position=input_non_empty("请输入新岗位：")
                        records[num-1]["position"]=new_position
                    elif field=="date":
                        new_date=input_non_empty("请输入新的日期：")
                        records[num-1]["date"]=new_date
                    elif field=="status":
                        while True:
                            status_input = input_non_empty("请输入状态（已投/笔试/面试/挂/Offer）：")
                            if status_input in VALID_STATUSES:
                                break
                            print("状态不合法，请重新输入")
                        records[num-1]["status"]=status_input
                    else:
                        print("输入修改项目不合法")
                else:
                    print("编号不存在")
                save(records)
                print("修改成功")
        elif choice == "4":
            if len(records)==0:
                print("还没有记录")
            else:
                for i,record in enumerate(records,start=1):
                    print(f"{i}.{record['company']}|{record['position']}|{record['date']}|{record['status']}")
                num=input_int("输入要删除的记录：")
                if 1<=num<=len(records):
                    del records[num-1]
                else:
                    print("编号不存在")
                save(records)
                print("删除成功")
        elif choice=="5":
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
        elif choice == "6":
            break
        else:
            print("无效的操作编号，请重新输入。")

