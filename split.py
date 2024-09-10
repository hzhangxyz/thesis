import os

with open("main.tex", "r") as file:
    content = file.read()

front, *chapters, back = content.split("\\chapter")
chapters = ["\\chapter" + chapter for chapter in chapters]
back = "\\chapter" + back

with open("main.tex", "w") as file:
    print(front, file=file)
    for i, chapter in enumerate(chapters):
        print(f"\\input{{chapter-{i+1}.tex}}", file=file)
        with open(f"chapter-{i+1}.tex", "w") as f:
            print(chapter, file=f)
    print(back, file=file)
