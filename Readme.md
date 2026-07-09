#My learning Diary
Part 1: The Cipher Engine (caesar_cipher function)This block defines the core mathematical function that does the heavy lifting of shifting characters.
Python
def caesar_cipher(text, shift, mode='encrypt'):
def: Tells Python we are creating a custom reusable tool (a function) named caesar_cipher.(text, shift, mode='encrypt'): These are the inputs it needs. If you don't specify a mode, it automatically defaults to 'encrypt'.Python    if mode == 'decrypt':
        shift = -shift
if mode == 'decrypt':: Checks if the user wants to decrypt a message.shift = -shift: 

If they do, it flips the math. Shifting forward by 4 becomes shifting backward by -4, which naturally reverses the encryption process using the exact same formula.Python    result = []

Creates an empty list called result. As we process the message letter by letter, we will drop the new shifted characters into this list.Python    for char in text:
A loop that pulls out every individual character (char) from your message, one by one, from left to right.

Python 
       if char.isupper():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(shifted_char)
if char.isupper():: Checks if the current character is a capital letter ($A-Z$).ord(char): Converts that capital letter into its raw ASCII number (e.g., 'A' becomes 65, 'Z' becomes 90).- 65: Subtracts 65 to shift the range down to $0-25$. This aligns the alphabet perfectly with mathematical index numbers ($A=0, B=1, \dots, Z=25$).+ shift: Adds your key number to move the letter forward or backward.% 26: The modulo operator handles the wrap-around. If a calculation hits 26, it loops back to 0 (the letter A). This ensures the math never spills out into weird punctuation characters.+ 65: Adds 65 back to restore the number into the proper uppercase ASCII neighborhood.chr(...): Converts that final math number back into a readable text character.result.append(...): Saves that newly shifted character into our result list.
Python
        elif char.islower():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result.append(shifted_char)
Does the exact same operation as above, but uses 97 as the baseline baseline subtraction/addition because lowercase letters ($a-z$) live in the ASCII range of $97-122$.Python        else:
            result.append(char)
else:: If the character isn't an uppercase or lowercase letter (like a space, a number, a period, or a colon), it skips all the math entirely and drops it straight into the result list unchanged.Python    return "".join(result)
"".join(result): Takes all the separate characters sitting inside our result list and glues them back together into one single string of text.return: Hands that final scrambled or unscrambled message back to the program.Part 2: The Interactive LoopThis block manages the continuous menu layout in your terminal.

Python
if __name__ == "__main__":
    print("=== Continuous Caesar Cipher Tool ===")
if __name__ == "__main__":: The control switch we discussed. It tells Python to execute the following menu code only if you are running this specific file directly.Python    while True:
        print("\n-----------------------------------")
while True:: Starts an infinite loop. Everything indented under this line will repeat forever until we manually force it to stop.print("\n-----------------------------------"): Prints a clean separator line with a new-line spacing (\n) to make the menu easy to read on every cycle.

Python
        choice = input("Type 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").strip().upper()
input(...): Pauses the terminal and waits for you to type something..strip(): Automatically cuts off any accidental spaces you might type before or after your entry..upper(): Automatically turns what you typed into a capital letter. (If you type a lowercase 'e', it instantly converts it to an uppercase 'E' so the code doesn't get confused).Python        if choice == 'Q':
            print("Exiting tool. Goodbye!")
            break
Checks if you typed Q. If you did, it prints a goodbye message and runs break, which smashes out of the infinite while loop and shuts the program down cleanly.Python        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue
If you type something completely wrong (like 'X' or 'hello'), it warns you and runs continue. This immediately stops processing the rest of the lines and jumps right back up to the top of the while loop to ask the main question again.Python        user_text = input("Enter your message: ")
        user_key_input = input("Enter shift key number (e.g., 4): ").strip()
Prompts you to type out the secret message you want to process, followed by the shift key number.
Python
        if user_key_input.isdigit() or (user_key_input.startswith('-') and user_key_input[1:].isdigit()):
            user_key = int(user_key_input)
        else:
            print("Invalid number. Using default shift of 4.")
            user_key = 4
This is a safety check. It verifies if your shift input is a valid positive digit (.isdigit()) or a valid negative number (starts with -).If it is safe, it converts the text string into an actual integer using int(). If you type junk like "abc", it falls back to a default key of 4 instead of crashing the loop with an error.Python        if choice == 'E':
            output = caesar_cipher(user_text, user_key, mode='encrypt')
            print(f"\nEncrypted Result:\n{output}")
        else:
            output = caesar_cipher(user_text, user_key, mode='decrypt')
            print(f"\nDecrypted Result:\n{output}")
Looks at your initial choice. If you picked E, it sends your text and key to the cipher engine with mode='encrypt'. If you picked D, it runs it as mode='decrypt'.Finally, it prints the processed output onto the screen, hits the end of the while loop block, and circles right back to the top to ask for your next command!
## Technical Details: The math breakdown
Here is exactly how the script processes characters under the hood:
- function defination
-de/en crypt
-treat lower/upper case letters
-character skipping
