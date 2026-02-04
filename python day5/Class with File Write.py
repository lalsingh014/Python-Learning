class Note:
    def __init__(self,text):
        self.text = text
    def save(self):
        with open("notes.txt", "a") as f:
            f.write(self.text + "\n")
            
n = Note("This is OOP note")
n.save()