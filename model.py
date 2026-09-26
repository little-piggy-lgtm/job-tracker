class Application:
    def __init__(self,company,position,date,status=True):
        self.company=company
        self.position=position
        self.date=date
        self.status = status

    def to_dict(self):
        return{
            "company":self.company,"position":self.position,"date":self.date,"status":self.status
        }

if __name__ == "__main__":
    app = Application("字节跳动", "后端开发实习", "2025-09-18")
    print(app.to_dict())

if __name__ == "__main__":
    app = Application("字节跳动", "后端开发实习", "2025-09-18",False)
    print(app.to_dict())