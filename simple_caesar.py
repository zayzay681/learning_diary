def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
        
    result = []
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result.append(shifted_char)
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == "__main__":
    print("=== Continuous Caesar Cipher Tool ===")
    
    # This loop keeps the program running indefinitely
    while True:
        print("\n-----------------------------------")
        choice = input("Type 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting tool. Goodbye!")
            break  # This breaks the loop and closes the program cleanly
            
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue  # Skips the rest of the loop and starts over at the top

        user_text = input("Enter your message: ")
        user_key_input = input("Enter shift key number (e.g., 4): ").strip()

        if user_key_input.isdigit() or (user_key_input.startswith('-') and user_key_input[1:].isdigit()):
            user_key = int(user_key_input)
        else:
            print("Invalid number. Using default shift of 4.")
            user_key = 4

        if choice == 'E':
            output = caesar_cipher(user_text, user_key, mode='encrypt')
            print(f"\nEncrypted Result:\n{output}")
        else:
            output = caesar_cipher(user_text, user_key, mode='decrypt')
            print(f"\nDecrypted Result:\n{output}")