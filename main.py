import PyPDF2  # library used to read pdf
import pyttsx3  # use to speak text


def read_pdf() -> str:
    """
    Read the text from a PDF file and return the text in string
    :return: string
    """

    # variable used to keep pdf text
    extracted_text: str = ""
    # make file object in context manager
    with open("sample.pdf", "rb") as file:
        # get PdfFileReader object
        pdf_reader = PyPDF2.PdfFileReader(file)
        # iterate over all pages of pdf and read text
        for page in range(pdf_reader.numPages):
            # read each page text and append into the variable
            extracted_text += pdf_reader.getPage(page).extractText()
    # return the text
    return extracted_text


def speak(text, rate=150, gender=2):
    """
    Function that text, rate of speak, and gender of voice as parameter and read PDF accordingly.
    :param text: string
    :param rate: integer
    :param gender: integer
    """
    # making pyttsx3 object to speak text
    engine = pyttsx3.init()
    # setting rate of speak
    engine.setProperty('rate', rate)
    if gender == 2:  # set female voice, default is male
        engine.setProperty('voice', 'f3')
    # speak
    engine.say(text)
    engine.runAndWait()


def main():
    """
    Main function that run and control the flow of program
    """
    # read pdf and get the text back
    pdf_text = read_pdf()
    # select gender for voice
    gender: int = int(input("Enter voice\n1.Male\n2.Female\n"))
    # speak pdf
    speak(pdf_text, gender=gender)


if __name__ == "__main__":
    main()
