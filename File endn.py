def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? ").lower()
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path for the output file: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice == 'e':
        encrypt_file(input_file, output_file, key)
    elif choice == 'd':
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
