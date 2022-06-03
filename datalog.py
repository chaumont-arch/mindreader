class Datalog:
    def __init__(self,id,timecode):
        self.id = id
        self.timecode = timecode
        self.validate_file()
        self.log_timecode()

    def validate_file(self):
        try:
            f = open("datalogs/{}.csv".format(self.id),"a")
        except:
            f = open("datalogs/{}.csv".format(self.id),"w")
        f.close()

    def log_timecode(self):
        f = open("datalogs/{}.csv".format(self.id),"a")
        f.write("round,player move,ai move,score,p-value,equal,{}\n".format(self.timecode))
        f.close()

    def write(self,value,end):
        f = open("datalogs/{}.csv".format(self.id),"a")
        f.write(value)
        if end:
            f.write("\n")
        f.close()
