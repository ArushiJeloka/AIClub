'''Make a code that conjugates regular spanish verbs in the present tense'''

def conjugate(tense,pronoun,verb):
    if len(verb) > 3:
        if tense == 'present':
          if verb.endswith("ar"):
            ar = {"yo": "o", "tu": "as", "usted": "a", "el": "a", "ella": "a", "nosotros": "amos", "vosotros": "ais", "ustedes": "an", "ellos": "an", "ellas": "an"}
            verb = verb[:-2] + ar[pronoun]
            return verb
          if verb.endswith("er") or verb.endswith("ir"):
            erDict = {"yo":"o", "tu":"es", "usted":"e", "el":"e", "ella":"e", "nosotros":"emos", "vosotros":"eis", "ustedes": "en", "ellos": "en", "ellas":"en"}
            irDict = {"nosotros":"imos", "vosotros":"is"}
            if (pronoun == "nosotros" or pronoun == "vosotros") and verb.endswith("ir"):
                verb = verb[:-2] + irDict[pronoun]
            else:
                verb = verb[:-2] + erDict[pronoun]
            return verb
        if tense == 'preterit':
            if verb.endswith("ar"):
                ar = {"yo": "e", "tu": "aste", "usted": "o", "el": "o", "ella": "o", "nosotros": "amos",
                      "vosotros": "asteis", "ustedes": "aron", "ellos": "aron", "ellas": "aron"}
                verb = verb[:-2] + ar[pronoun]
                return verb
            if verb.endswith("er") or verb.endswith("ir"):
                erDict = {"yo": "i", "tu": "iste", "usted": "io", "el": "io", "ella": "io", "nosotros": "imos",
                          "vosotros": "isteis", "ustedes": 'eron', "ellos": "eron", "ellas": "eron"}
                irDict = {"ustedes": "ieron", "ellos": "ieron", "ellas": "ieron"}
                if (pronoun == "ellos" or pronoun == "ellas" or pronoun == "ustedes") and verb.endswith("ir"):
                    verb = verb[:-2] + irDict[pronoun]
                else:
                    verb = verb[:-2] + erDict[pronoun]
                return verb

        if tense == 'imperfect':
            if verb.endswith("ar"):
                ar = {"yo": "aba", "tu": "abas", "usted": "aba", "el": "aba", "ella": "aba", "nosotros": "abamos",
                      "vosotros": "abeis", "ustedes": "aban", "ellos": "aban", "ellas": "aban"}
                verb = verb[:-2] + ar[pronoun]
                return verb
            if verb.endswith("er") or verb.endswith("ir"):
                erDict = {"yo": "ia", "tu": "ias", "usted": "ia", "el": "ia", "ella": "ia", "nosotros": "iamos",
                          "vosotros": "iais", "ustedes": "ian", "ellos": "ian", "ellas": "ian"}
                verb = verb[:-2] + erDict[pronoun]
                return verb
    if len(verb) < 3:
        print('this is irregular')

print(conjugate('preterit','tu', 'morir'))
print("remember that this code does not print accented letters or irregulars")

fruit = {"apple": "red", "banana": "yellow", "orange": "orange", "blueberries": "blue"}
fruit["red"]