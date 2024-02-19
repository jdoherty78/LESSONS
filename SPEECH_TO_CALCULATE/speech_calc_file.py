def SpeechCalcFile(total, calc, folder="MATH"):
        import os, datetime as dt
        timestamp = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        folder = "MATH"
        if not os.path.exists(folder): # TRUE
            os.mkdir(folder)
        with open(folder + os.sep + "math.txt", "a") as f:
            f.write("\nTime Stamp: {}".format(timestamp))
            f.write("\nTotal: {}".format(total))
            f.write("\n{}".format(str(calc)))
            f.write("\n")
