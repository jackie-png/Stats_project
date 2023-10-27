import csv
import numpy as np
import matplotlib.pyplot as mpl


# when shower thought moment said lets rewrite everything yes

class response:
    """
    This class represents a respondent and what they answered



    """

    def __init__(self, age, program, year, gender, backgrd, ):  # response constructor, age, program, year, background,
        # and gender will be held in separate variables whereas all other questions will be held in a list
        self.age = age
        self.gender = gender
        self.program = program
        self.year = year
        self.backgrd = backgrd
        self.respList = []  # answers for questions not relating to personal information ei, the actual survey questions

    def toString(self):  # a toString method to display the object's info
        return "Age: " + str(self.age) + "| Gender: " + str(self.gender) + "| Program: " + str(
            self.program) + "| Background: " + \
               str(self.backgrd) + "| Year: " + str(self.year) + "| Response to questions: " + str(self.respList)


answerList = []  # holds a list of response classes
answerListInd = 0

with open('CPS 412 - Assignment 1 - Form Responses 2.csv', mode='r') as data:  # this opens the csv file of the
    # responses
    data = csv.reader(data)  # reads the responses into a list called data
    for lines in data:
        if 'Timestamp' in lines:  # this will check which line has the question titles
            header = lines.copy()  # copies that line into the header and continues
            header.pop(0)
            continue
        lines.pop(0)
        Q3choices = lines[7].split(", ")  # gets question 3 and splits it along commas
        Q3answers = []  # to hold the answers for question 3

        for choice in Q3choices:  # to process the answers for question3, the one that asked what you used Chatgpt for
            if "To Learn New Things" in choice:  # if Q3 consisted of one of these statements then it would add a number
                # corresponding to that answer
                Q3answers.append(1)
            if "Education (Help with Assignments / Projects)" in choice:
                Q3answers.append(2)
            if "Entertainment" in choice:
                Q3answers.append(3)
            if "Generating Creative Ideas and Content" in choice:
                Q3answers.append(4)
            if "Get feedback on Writing or Work" in choice:
                Q3answers.append(5)

        answerList.append(response(int(lines[0]), lines[1].lower(), int(lines[2]), lines[3].lower(),
                                   lines[4].lower()))  # adds a new response object with
        # the age, gender, program, year, and background defined by what they answered on the survey

        for remove in range(0, 5):  # removes the elements that represent the age, gender, background, year, and program
            # since they have been recorded and processed
            lines.pop(0)

        for ans in range(0, len(lines)):  # to add the rest of the answers into the current response object
            if ans == 2:  # Question 3 has already been processed beforehand, just add it into the list
                answerList[answerListInd].respList.append(Q3answers)
            else:
                print(lines[ans])
                if lines[ans].isdigit():
                    answerList[answerListInd].respList.append(int(lines[ans]))
                else:
                    lines[ans] = str(lines[ans]).lower()
                    answerList[answerListInd].respList.append(lines[ans])

        answerListInd += 1  # increments to the next response in answerList

for answer in answerList:
    print(answer.toString())


def Pfilter(trait, ansList):
    """
    This function will act as the filter system, so we can separate the data based on what responders have answered

    :param trait: will tell the program what to filter based on a specified person trait. ie, age, gender, etc

    :param ansList: the unfiltered answer list of all responses

    :return: will return a list of response objects that contains the responses that have been picked out by the filter
    """

    filterList = []

    if str(trait).lower() == "age":  # if filter for age

        print("Lower age range to filter: ")
        lower = int(input())  # gets lower bound of age

        print("Higher age range to filter: ")
        higher = int(input())  # gets upper bound of age
        filterTag.append(
            trait + ": " + str(lower) + "-" + str(higher))  # adds lower age to upper age to filter tag list

        for ans in ansList:
            if lower <= int(ans.age) <= higher:  # if the age of t respondent is between the lower and upper bound age
                filterList.append(ans)  # add them to the filtered list

        return filterList

    if str(trait).lower() == "gender":  # if filter for gender
        print("Gender to filter for: ")
        genderFil = str(input())  # input gender, look for gender to filter in the data
        filterTag.append(trait + ": " + genderFil)  # adds filtered gender to filter tags list
        for ans in ansList:
            if genderFil.lower() == ans.gender:  # if gender of respondent matches with specified gender to filter for
                filterList.append(ans)  #
        return filterList

    if str(trait).lower() == "year":  # if filter for year
        lower = int(input("Lower year to filter for : "))  # lower bound year
        higher = int(input("Higher year to filter for :"))  # upper bound year
        filterTag.append(trait + ": " + str(lower) + "-" + str(higher))  # adds them to the filter tag list
        for ans in ansList:
            if lower <= ans.year <= higher:  # if respondent school year is between lower and upper bound of year
                filterList.append(ans)  # add them to the filterlist
        return filterList

    if str(trait).lower() == "program":  # if filter for program
        print("Program to filter for: ")  # specify which program to filter, look in data for the program name
        profil = str(input())  # gets program
        filterTag.append(trait + ": " + profil)  # adds to the filter tag list

        for ans in ansList:
            if profil == ans.program:  # if respondent's program matches the specified program
                filterList.append(ans)  # add to filter list
        return filterList

    if str(trait).lower() == "background":  # if filtering for cultural background
        print(
            "background to filter for: ")  # specify which background you want to filter for, look in data for
        # background
        backfil = str(input())
        filterTag.append(trait + ": " + backfil)  # adds to filter tag
        for ans in ansList:
            if backfil == ans.backgrd:  # if respondent's background  matches the specified background
                filterList.append(ans)
        return filterList


def Qfilter(question, ansList):
    """
    This function will act as the filter system, so we can separate the data based on what responders have answered

    :param question: will tell the program what filter based on question given

    :param ansList: the unfiltered answer list of all responses

    :return: will return a list of response objects that contains the responses that have been picked out by the filter
    """
    filterList = []
    if 1 <= question <= 2 or 5 <= question <= 12:  # if you want to filter for Yes or No questions: 1, 2, 5 to 12 are
        # yes No
        print(header[question + 4])
        choice = str(input("Filter for Yes or No: ").lower())  # filter for if they answered yes or no
        filterTag.append(header[question + 4] + ": " + choice)
        for ans in ansList:
            if ans.respList[question - 1] == choice:  # if respondent matches yes or No
                filterList.append(ans)

    elif question == 3:  # if you want to filter for what respondents answered for the multichoice question
        print(header[question + 4])
        MchoiceList = []  # holds which choice to filter for
        while True:
            Mchoice = int(
                input("Filter from which answer \n1. To Learn New Things \n2. Education (Help with Assignments / "
                      "Projects) \n3. Entertainment\n4. Generating Creative Ideas and Content\n5. Get feedback "
                      "on Writing or Work\ntype 6 to stop\n>"))
            # gets which choice to filter for
            if Mchoice == 6:
                break
            MchoiceList.append(Mchoice)
        filterTag.append(header[question + 4] + ": " + str(MchoiceList))  # adds choices to filter list
        print(MchoiceList)
        for answ in filtered:  # for all answers in the filtered list
            for ch in answ.respList[question - 1]:  # for all choices in the respondents question 3 response list
                if ch in MchoiceList:  # if the choice matches 1 of the choice filtering for
                    if ch not in filterList:  # then if the ch isn't already in the filtered list
                        filterList.append(answ)  # add to the filter list
                        break
                    else:
                        continue  # else skip and move to the next choice


    elif question == 4:  # if you want to filter for the 0-10 question
        print(header[question - 4])
        lower = int(input("Lower range: 0 - 10"))  # lower bound of answers
        higher = int(input("Higher Range: 0 - 10"))  # upper bound of answers
        filterTag.append(header[question + 4] + ": " + str(lower) + "-" + str(higher))
        for ans in ansList:
            if lower <= ans.respList[question - 1] <= higher:  # if respondent answer to Q4 is between lower and upper range
                filterList.append(ans)

    return filterList


# cut another file (filters)
def consoleDisplay(ansList):
    """
    To help display respondents in console / run window during graphing
    :param ansList: list of respondents
    """
    for ans in ansList:
        print(ans.toString())


def func(pct, allvals):  # puts values onto the pie graph
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"


filtered = answerList
filterTag = []
graphing = True
while graphing:
    print("Graph Boi 9000 V2")  # sick title
    choice = input("Filter for something?, type filter: (press enter to not filter)")

    filtering = True
    if choice == "filter":  # if you choose to filter for a question or person trait
        while filtering:
            option = input("Person Traits or Question or reset to reset data: ").lower()
            if option == "person":  # filter for a person trait
                choice = str(input("Age, year, program, background, gender"))
                if choice == "out":  # get out of filtering
                    filtering = False

                filtered = Pfilter(choice, filtered)  # sends the list of answers to Pfilter to filter for person trait

            elif option == "question":  # filter for what people answered
                choice = input("question filter: 1 2 3 4 5 6 7 8 9 10 12: ")
                if choice == "out":
                    filtering = False
                filtered = Qfilter(int(choice), filtered)  # sends list of answers to filter for a question
            elif option == "out":  # get out of filtering
                filtering = False
            elif option == "reset":  # if you want to reset the filtered list
                filtered = answerList  # sets the filtered list back to the original data set
                filterTag = []  # resets tag list

    whichGraph = int(input("Which Question to graph: 1 2 3 4 5 6 7 8 9 10 11 12"))

    if 1 <= whichGraph <= 2 or 5 <= whichGraph <= 12:  # graphing for yes no questions
        print(header[(whichGraph - 1) + 5])
        # yes no questions will be pie charts
        yesNo = []
        xValue = ["Yes", "No"]  # Pie slice labels
        yValue = []  # Pie slice size
        explode = (0.1, 0.05)  # separates slices based on offset values
        tag = input("Extra Tag on Graph Title? (press enter if no): \n>")  # extra title for graph?
        for ans in filtered:
            yesNo.append(ans.respList[whichGraph - 1])  # gets the data for the yes or no question
        consoleDisplay(filtered)
        yValue.append(yesNo.count("yes"))  # counts how many people answered yes
        yValue.append(yesNo.count("no"))  # counts how many people answered no
        print(yValue)
        print(filterTag)
        mpl.title(header[(whichGraph + 4)] + "\n" + tag)  # title of graph
        mpl.pie(yValue, explode=explode, shadow=True, labels=xValue,
                autopct=lambda pct: func(pct, yValue))  # makes pie graph
        mpl.show()  # displays graph

    elif whichGraph == 3:  # graphing the multichoice question
        print(header[(whichGraph - 1) + 5])
        print("multichoice")  # this will be a bar graph
        consoleDisplay(filtered)  # displays filtered data list
        xValue = []  # holds x values
        yValue = []  # holds y valuesw
        answers = {}  # holds answer and how many people answered it
        for ans in filtered:  # for all answers in filtered list
            for choices in ans.respList[whichGraph - 1]:  # for all choices in the list fo answers for question 3
                if answers.get(choices) is None:  # if the answer dictionary doesn't contain that answer, put it in
                    answers[choices] = 1
                else:
                    answers[choices] += 1  # else add 1 to the value of that element

        print(answers)

        temp = dict(sorted(answers.items()))  # sorts the answer and turns it back into a dictionary
        yValue = list(temp.values())  # values of the dictionary is the height of the graph
        xLabels = ["To Learn\nNew Things", "Education\n(Help with\nAssignments/Projects)", "Entertainment",
                   "Generating Creative\nIdeas and Content", "Get feedback on\nWriting or Work"]

        print(xLabels)
        print(yValue)
        print(filterTag)
        mpl.title(header[whichGraph + 4])  # title of graph
        bars = mpl.bar(xLabels, yValue)  # makes bar graph
        for bar in bars:
            height = bar.get_height()
            mpl.text(bar.get_x() + 0.35, height + 0.2, height)  # puts text on top of the bars of the bar graph
        mpl.xlabel("Number of people")  # x axis title
        mpl.ylabel("Choices")  # y axis title
        mpl.show()  # display graph




    elif whichGraph == 4:  # graphing the 0-10 question
        print("0-10")  # this will be a bar graph
        print(header[(whichGraph - 1) + 5])
        consoleDisplay(filtered)
        xValue = []  # stores x axis labels
        yValue = []  # stores y value of bars/ height of bar
        answers = {}  # stores the answers and how many people answered each answer
        for ans in filtered:
            if answers.get(
                    str(ans.respList[whichGraph - 1])) is None:  # if the answer isnt in the dictionary, put it in
                answers[str(ans.respList[whichGraph - 1])] = 1
            else:
                answers[str(ans.respList[whichGraph - 1])] += 1  # else add 1 to the value of that element
        print(answers)

        temp = dict(sorted(answers.items()))  # sorts the answer based on increasing order[1,2,3,4,5...]
        xValue = list(temp.keys())  # keys of dictionary are the x values
        yValue = list(temp.values())  # values of the dictionary are the y values

        print(xValue)
        print(yValue)
        print(filterTag)
        bars = mpl.bar(xValue, yValue)  # makes bar graph
        for bar in bars:
            height = bar.get_height()
            mpl.text(bar.get_x() + 0.2, height + 0.2, height)  # puts text onto the bar graph

        mpl.xlabel("scale of 1-10")  # x axis title
        mpl.ylabel("Number of respondents")  # y axis title
        mpl.title(header[(whichGraph - 1) + 5])  # graph title
        mpl.show()  # display graph

# cut for another file (graphing/main)
