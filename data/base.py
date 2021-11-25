
with open("Isaac_Academy.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

raw_text = raw_text.lower()
raw_text = raw_text.replace('\n\n', '\n')
for i in range(40,200):
    text = raw_text[:256]
    raw_text = raw_text[257:]
    text = text[text.find(' ') + 1:text.rfind(' ')]
    with open("./raw_text/novel/{0}.txt".format(i), "w") as out_:
        out_.write(text)
