while True:
    operate = int(input('\n1- Read the notes\n2- Input note\n3- Save the points (?/100) \n4- Exit\n->'))

    def inputNote():
        name = input('\nStudent name: ')
        sName = input('Student surname: ')
        note1 = input('1st Note: ')
        note2 = input('2nd Note: ')
        note3 = input('3rd Note: ')

        with open("exam_notes.txt","a",encoding="utf-8") as file:
            file.write(name + ' ' + sName + ':' + note1+','+note2+','+note3+'\n')
            print(f"-----Saved {name}'s Notes-----\n")


    def calcNotes(lines):
        lines = lines[:-1] # For not choose the blanks (\n)
        linesList = lines.split(':') # seperate the line as name and notes
        
        student = linesList[0]
        notes = linesList[1].split(',')

        n1 = int(notes[0])
        n2 = int(notes[1])
        n3 = int(notes[2])
        mean = (n1+n2+n3)/3

        return student , round(mean,2)


    def readNotes():
        op = int(input("\n1- See the final points\n2- See the all exams points\n->"))
        if op == 1:    
            with open("exam_notes.txt","r",encoding="utf-8") as file:
                for lines in file:
                    lines = lines[:-1] # For not choose the blanks (\n)
                    linesList = lines.split(':') # seperate the line as name and notes
        
                    student = linesList[0]
                    notes = linesList[1].split(',')
                    
                    if len(notes) >= 3:
                        calcs = list(calcNotes(lines))
                        print(f"{calcs[0]}: {calcs[1]}")
                    else:
                        print(f"\t [!] {student}'s exams not finished yet")
        
        if op == 2:
            with open("exam_notes.txt","r",encoding="utf-8") as file:
                file.seek(0)
                print(file.read())
        

    def saveNotes():
        with open("exam_notes.txt","r",encoding="utf-8") as file:
            eList = []
            for i in file:
                eList.append(calcNotes(i))
            # print(eList[2][1])

            with open("exam_results.txt","w",encoding="utf-8") as file2:
                for i in eList:
                    file2.write(i[0] + ':' + str(i[1]) + '\n')
                print("-----Notes Saved-----\n")


    if operate == 1:
        readNotes()
    
    elif operate == 2:
        inputNote()
    
    elif operate == 3:
        saveNotes()
    
    else:
        break