def word_counter(fname):
    try:
        with open(fname,'r')as file:
            text=file.read()
            words=text.split()
            print(f"Number of words in '{fname}: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found.")
fname=input("Enter the file name:")
word_counter(fname)
