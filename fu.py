import pdfplumber
import csv
import synonym

def check(li,str):
    for i in li:
        if i in str:
            return True
    return False

# Open the PDF file using pdfplumber
def file_procees(file_path):
# Define the PDF file path
    pdf_file_path = file_path

# Create a dictionary to store questions and answers
    qa_dict = {}
    q=0
    output=""
    csv_file = 'Ddataset._newcsv.csv'
    with pdfplumber.open(pdf_file_path) as pdf:
        # Iterate through each page of the PDF
        for page in pdf.pages:
            # Extract the text from the page
            page_text = page.extract_text()

            # Split the text into lines (assuming each question and answer is on a separate line)
            lines = page_text.split('\n')
            score=0
            # Iterate through the lines to identify and store questions and answers
            i = 0
            while i < len(lines):
                # Check if the line is a question (you can modify this condition based on your PDF structure)
                if lines[i].endswith('?'):
                    question = lines[i]
                    i += 1

                    # Initialize an empty string to store the answer
                    answer = ""

                    # Keep adding lines to the answer until the next question is encountered
                    while i < len(lines) and not lines[i].endswith('?'):
                        answer += lines[i] + ' '
                        i += 1

                    # Remove leading and trailing whitespace from the answer
                    answer = answer.strip()

                    # Add the question and answer to the dictionary
                    
                    question=question[question.find(' ')+1:len(question)]
                    question=question.lower()
                    answer=answer[answer.find(' ')+1:len(answer)]
                    answer=answer.lower()
                    # print(question)
                    # print(answer)
                    target_keyword = question
                    q=q+2
                    sc =score
                    with open(csv_file, 'r') as file:
                        csv_reader = csv.reader(file)
                        for row in csv_reader:
                            if target_keyword in row:
                                l=(row[1].split('; '))
                                count=0
                                for keyword in l:
                                    if keyword in answer or check(synonym.get_synonyms(keyword),answer):
                                        count=count+1
                                if(count>=4 or count/len(l)>=0.4):
                                    score=score+2
                                else:
                                    score=score+count/2
                    if(score-sc==1 or score-sc==2):
                        output=output+str(f"{int(q/2)}. {int(score-sc)}/2")+"\n"
                    else:
                        output=output+str(f"{int(q/2)}. {score-sc}/2")+"\n"
                    
        output=output+str(f"Evaluated Score: {score}/{q}")
        return output

                            
