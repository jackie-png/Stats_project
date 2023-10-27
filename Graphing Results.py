import matplotlib.pyplot as plt  # imports matplotlib

results = open("test results.txt", "r")  # opens the results file for reading

titleList = []
questionList = []


class Question:  # a small class to hold the question's title, choices, and its values
    def __init__(self, name):
        self.Qname = name
        self.Qheader = []
        self.Qvalues = []


p = results.readline()

# cuts up the title list for writing
titles = p.split(",")
titles.remove("\n")
titles.remove("Timestamp")
for title in titles:
    titleList.append(title)  # writes question title into titleList

for Q in range(0, 17):  # writes in the question responses into a Question class
    questionList.append(Question(titleList[Q]))  # reads into question title (Graph Title)
    t = results.readline()
    responses = t.split(",")
    responses.remove("\n")
    for ele in responses:  # for each element in responses assign it to the Question header and value variables
        s = ele.split(":")
        if Q == 1 or Q == 4:  # question 2 and 4 have spacing issues while graphing, so I replaced the spaces with \n
            temp = s[0].replace(" ", "\n")
            questionList[Q].Qheader.append(temp)  # reads into question header (X Axis Labels)
        else:
            questionList[Q].Qheader.append(s[0])
        questionList[Q].Qvalues.append(int(s[1]))  # reads into question values (Y Axis Labels)

while True:  # display program
    try:
        lines = int(
            input("Question?: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17\n"))  # what question do you want to view
        print("alrighty then, getting results for", end=" ")
        if lines > 17:  # there are no questions beyond question 17 so all numbers 18 up will be considered as 17
            lines = 17
        print("Question:", lines)
    except ValueError:  # how to exit the program, type anything that isn't an integer
        print("exiting")
        break

    # Graphing

    # run window text
    print("Responses: ", responses)
    print("X Axis: ", questionList[lines - 1].Qheader)
    print("Y Axis: ", questionList[lines - 1].Qvalues)

    plt.bar(questionList[lines - 1].Qheader, questionList[lines - 1].Qvalues)  # initializes bar graph
    plt.ylabel("Number of Responses")  # title for Y axis
    plt.xlabel("Choices")  # title for X axis
    plt.title(questionList[lines - 1].Qname)  # gets graph title
    plt.xticks(fontsize=8)  # change font size

    plt.tight_layout()  # tight layout fits better for labels
    plt.show()  # graphs graph
