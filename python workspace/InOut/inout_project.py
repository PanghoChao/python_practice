
for week in range(1,51):
    report_file = open("{0}주차.txt".format(week), "w", encoding="utf8")
   
    # print("부서 :",file=report_file)
    # print("이름 :",file=report_file)
    # print("업무요약 :",file=report_file)
    report_file.write("--{0}주차 보고 --".format(week))
    report_file.write("\n부서 :")
    report_file.write("\n이름 :")
    report_file.write("\n업무요약 :")
    report_file.close()


