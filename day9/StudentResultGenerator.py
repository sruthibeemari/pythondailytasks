class Results:
    def avgOfResults(self,sub1,sub2,sub3=None):
        if sub3==None:
            total=sub1+sub2
            avg=total/2
            print("Total Marks (two subjects): ",total)
            print("Average of two subjects: ",avg)
        else:
            total=sub1+sub2+sub3
            avg=total/3
            print("Total Marks (three subjects): ",total)
            print("Average of three subjects: ",avg)
r=Results()
r.avgOfResults(60,90)
r.avgOfResults(70,60,80)



    