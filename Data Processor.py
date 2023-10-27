import csv  # imports the csv reading and writing package

f = open("test results.csv", "w")  # this opens the test results file for writing

def processing(Qnumber):
    """
    This function will process the data based on what question it has been given
    :param Qnumber: Question Number 
    :return: will return a dictionary of the processed response of a question
    """
    global header  # a global variable for storing the Question itself
    header = []  # declaring header as a list, so it become a list of question titles
    with open('CPS 412 - Assignment 1 - Form Responses 2.csv', mode='r') as data:  # this opens the csv file of the
        # responses
        data = csv.reader(data)  # reads the responses into a list called data
        response = []  # to store the responses to a question
        for lines in data:
            if 'Timestamp' in lines:  # this will check which line has the question titles
                header = lines.copy()  # copies that line into the header and continues
                continue
            if Qnumber == 1 or Qnumber == 9:  # questions 1 and 9 are responses that consist of numbers
                response.append(int(lines[Qnumber]))
            elif Qnumber == 2 or 3 <= Qnumber <= 8 or Qnumber >= 10:  # questions 2 3 -> 8 and 10-17 are responses that
                # are words
                if (lines[Qnumber] == ""):
                    print("sdf")
                    response.append("No Answer")
                else:
                    response.append(lines[Qnumber])

    writeInRes = {}  # this is the dictionary that will be returned at the end

    if Qnumber >= 10 or Qnumber == 6 or Qnumber == 7:  # yes no {yes or no: number of people}
        writeInRes["Yes"] = response.count("Yes")  # counts number of yes's
        writeInRes["No"] = response.count("No")  # counts number of no's
        print(str(Qnumber) + ": ", writeInRes)
        return writeInRes
    elif Qnumber == 9:  # scale {scale: number of people}
        for choice in range(0, 11):
            writeInRes[choice] = (response.count(choice))  # counts the number of the specified number in choice
        print(str(Qnumber) + ": ", writeInRes)
        return writeInRes
    elif Qnumber == 8:
        num = 0
        writeInRes = {  # predefines the dictionary with the 5 choices question 8 has
            "To Learn New Things": 0,
            "Education (Help with Assignments / Projects)": 0,
            "Entertainment": 0,
            "Generating Creative Ideas and Content": 0,
            "Get feedback on Writing or Work": 0

        }
        for lines in response:  # why do you use it {choice: number of people}
            num += 1
            if "To Learn New Things" in lines:  # counts the different responses ~~count was counting wrong~~
                writeInRes["To Learn New Things"] += 1
            if "Education (Help with Assignments / Projects)" in lines:
                writeInRes["Education (Help with Assignments / Projects)"] += 1
            if "Entertainment" in lines:
                writeInRes["Entertainment"] += 1
            if "Generating Creative Ideas and Content" in lines:
                writeInRes["Generating Creative Ideas and Content"] += 1
            if "Get feedback on Writing or Work" in lines:
                writeInRes["Get feedback on Writing or Work"] += 1
        print(str(Qnumber) + ": ", writeInRes)
        return writeInRes
    elif Qnumber == 5:  # what is your cultural background {background: number of people}
        background = {}  # dictionary for cultural background
        for lines in response:  # searches through responses to count the number of cultural backgrounds
            if background.get(
                    lines) is None:  # if this background is not in the dictionary then add it to the dictionary
                background[lines] = 1
            else:
                background[lines] += 1

        for lines in background:  # copies background dictionary into the writeInRes dictionary
            writeInRes[lines] = background.get(lines)
        print(writeInRes)
        return writeInRes
    elif Qnumber == 4:  # what is your gender {gender: number of people}
        gender = {}  # dictionary of genders
        for lines in response:
            if gender.get(lines) is None:  # if this gender is not in the dictionary add it into the dictionary
                gender[lines] = 1
            else:
                gender[lines] += 1

        for lines in gender:  # copy the gender dictionary into the writeInRes
            writeInRes[lines] = gender.get(lines)
        print(writeInRes)
        return writeInRes
    elif Qnumber == 3:  # what year are you in {year: number of people}
        tempArr = []  # temporary array to store the responses of Q3
        for lines in response:
            if lines == "Graduate Student":  # if their response is graduate student change it to "6"
                tempArr.append(6)
            else:
                tempArr.append(int(lines))  # adds their response into the tempArr

        for choice in range(1, 7):
            writeInRes[choice] = (tempArr.count(choice))  # copies tempArr into writeInRes
        print(str(Qnumber) + ": ", writeInRes)
        return writeInRes

    elif Qnumber == 2:  # what is your program {program: number of people}
        program = {}  # program dictionary
        for lines in response:  # counts how many programs and people in those programs and stores int program dict
            if program.get(lines) is None:  # if this program isn't in the program dictionary add it in
                program[lines] = 1
            else:
                program[lines] += 1

        for lines in program:  # copies the program dictionary into writeInRes
            writeInRes[lines] = program.get(lines)
        print(writeInRes)
        return writeInRes
    elif Qnumber == 1:  # what is your age {age: number of people}
        for choice in range(min(response), max(response)+1):  # counts how many people are a certain age
            writeInRes[choice] = (response.count(choice))
        print(str(Qnumber) + ": ", writeInRes)
        return writeInRes


results = open("test results.txt", 'w')  # opens the test results file for writing
headerWritten = False  # boolean variable to see if the question titles have been written in
for questions in range(1, 18):
    writeIn = processing(questions)  # produces the processed responses
    if not headerWritten:  # if the header has not been written then write it in and turn headerWritten into True
        for question in header:
            results.write(question + ",")
        results.write("\n")
        headerWritten = True
    for answer in writeIn:  # for each answer/response in the processed writeIn, write it into the results file
        print(answer)
        results.write(str(answer) + ":" + str(writeIn.get(answer)) + ",")
    results.write("\n")

results.close()  # closes the results file

