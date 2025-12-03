def consonants_check(text):
    consonants = "бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxyz"
    text_verify = text.lower
    consonants_count = 0

    for i in text_verify:
        if i in consonants:
            consonants_count += 1

    print("Количество согласных в тексте:", consonants_count)

test_text = "макан андрей"
consonants_check(test_text)