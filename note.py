class Note():
    def __init__(self, title, desc, date, isimportant,onetime):
        self.title=title
        self.desc=desc
        self.date=date
        self.isimportant=isimportant
        self.isonetime=onetime

    def __str__(self):
        result=""
        result += "title: " + self.title + "\n"
        result += "desc: " + self.desc + "\n"
        result += "date: " + self.date + "\n"
        return result
        