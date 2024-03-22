from spellchecker import SpellChecker
import language_tool_python
import cv2
import pytesseract
from PIL import Image
import csv

def write_to_files(texts):
    # Write to text file
    with open('output.txt', 'w') as text_file:
        for text in texts:
                text_file.write(text )
               # text_file.write(text + '\n')

    # Write to CSV file
    with open('output.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Text'])
        for text in texts:
            writer.writerow([text])

def open_camera():
    # Open default camera (usually the first one available)
    cap = cv2.VideoCapture(0)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Loop to continuously capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, display it
        if ret:
            cv2.imshow('Camera', frame)
            ret, frame = cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(Image.fromarray(img))
            if len(text) > 1:
                print(text)
                print("Texts have been written to output.txt and output.csv")
                write_to_files(text)
                break

        # Check for 'q' key pressed, to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    return text


# Initialize spell checker and language tool
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')


def is_proper_english(text):
    # Check for spelling errors
    misspelled = spell.unknown(text.split())

    # Check for grammar errors
    matches = tool.check(text)

    # If there are no spelling or grammar errors, return True
    return len(misspelled) == 0 and len(matches) == 0


def main():
    texts = [
        open_camera()
    ]

    for text in texts:
        if is_proper_english(text):
            print("Proper English:", text)
        else:
            print("Improper English:", text)


if __name__ == "__main__":
    main()
