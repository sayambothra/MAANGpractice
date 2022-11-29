from translate import Translator
with open("C:/Users/Sayam/Desktop/translator.txt",mode="r") as myfile:
  translator=Translator(to_lang="ja")
  for each in myfile:
     translation=translator.translate(each)
     print(translation)
