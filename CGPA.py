import csv;
def dualDegree():
    seat_available = {"A1":7,"A2":8,"A3":13,"A4":10,"A7":22,"A8":5,"AA":13,"AB":5}
    seat_allotted = {"A1":0,"A2":0,"A3":0,"A4":0,"A7":0,"A8":0,"AA":0,"AB":0}
    cg_csv = open("file.csv", 'r');
    dualAllotPrint = open("file1.csv", "w");
    dualWriter = csv.writer(dualAllotPrint);
    row_count = 0;
    id_row = True;
    #approach each of the students preference records row by row.
    for row in cg_csv:
        string = str(row);
        string = string.split(',');
        row_count = row_count + 1;
        option = 1;
        if(id_row == True):
            id_row = False;
            dualAllotPrint.write(row);
            continue;
        for i in range(2, len(string), 1):
            if(seat_allotted[string[option + 1]] < seat_available[string[option + 1]]):
                seat_allotted[string[option + 1]] = seat_allotted[string[option + 1]] + 1;
                if(int(string[0]) < 10):
                    print "ID no. ", string[0], "  is allotted: ", string[option + 1], " remaining seats: ", seat_available[string[option + 1]] - seat_allotted[string[option + 1]],
                else:
                    print "ID no. ", string[0], " is allotted: ", string[option + 1], " remaining seats: ", seat_available[string[option + 1]] - seat_allotted[string[option + 1]],
                string[11] = string[option + 1];
                option = 1;
                break;
            else:
                option = option + 1;
        print string;
        for x in range(0, 12, 1):
            dualAllotPrint.write(str(string[x]) + ',');
        dualAllotPrint.write('\n');

    dualAllotPrint.close();
    cg_csv.close();
            
dualDegree();
