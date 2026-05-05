from dictionary import get_meaning, get_synonym
from spell_check import spelling_correct
from next_word_predict import predict_next_words

def main():

    print("\nSmart Text Assistant Started (type 'exit' to quit)\n")

    while True:

        text = input("Enter a word or a sentence : ").strip()

        if text.lower() == "exit":
            print("Goodbye")
            break

        if not text:
            print("Invalid input\n")
            continue

        final_text = text
        # SPELL CORRECTION
        
        if len(text.split()) == 1:

            suggestions = spelling_correct(text)
            final_text = text

            for word in suggestions:
                choice = input(f"Did you mean '{word}'? (y/n): ").strip().lower()

                if choice == 'y':
                    final_text = word
                    break

        # NEXT WORD SUGGESTION
       
        if len(final_text.split()) > 1:
            suggestions = predict_next_words(final_text)
            print("Suggestions : ", ",".join(suggestions) if suggestions else "Not found")
            print()
            continue

        # MEANING + SYNONYM
        
        meaning = get_meaning(final_text)
        synonym = get_synonym(final_text)

        print("Meaning : ", meaning)

        if synonym:
            print("Synonyms:", ", ".join(synonym))
        else:
            print("Synonyms: Not found")

        print()

main()