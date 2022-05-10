while True:
    operate = input('1- Read the notes\n2- Input note\n3-Save the notes\n 4- Exit')

    def readMean():
        name = input('Student name: ')
        sName = input('Student surname: ')
        note1 = input('1st Note: ')
        note2 = input('2nd Note: ')
        note3 = input('3rd Note: ')

        with open("exam_notes.txt","a",encoding="utf-8") as file:


    def inputNote():
        pass

    if operate == 1:
        readMean()
    
    elif operate == 2:
        inputNote()
    
    elif operate == 3:
        saveNote()
    
    else:
        break