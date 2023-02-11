char=input("Enter any character : ")

match char.lower():
    case 'a'|'e'|'i'|'o'|'u':
        print("Vowel")
    case _:
        print("Consonant")

        
