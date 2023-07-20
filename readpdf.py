import pdfreader

def createPDFobj(dir):
    fd = open(dir, "rb")
    return pdfreader.SimplePDFViewer(fd)
   

def getPagesText (pdfOBJ, dir):
    textpages = []
    for i in range(1, 4):
        pdfOBJ.navigate(i)
        pdfOBJ.render()
        textpages.append(pdfOBJ.canvas.strings)
    return textpages


def scanForInfo(txt,point = 1, *pages):
    for i,page in enumerate(pages):
            if txt in page:
                return page[page.index(txt)+1]
            else:
                return "n/a"
        

infotable = []
def extractText(text, pdfOBJ,dir):
    infotable = []
    stuff =['External report number:','2. Date of transaction:','3. Amount of transaction:','4. Transaction currency:']
    if not "Electronic funds transfer - Incoming (EFTI)" in text[0]:
        print("this is not an incoming transaction")
        exit()

    point = text[0].index("The client ordering the EFT")
    #report summary
    for i,v in enumerate(text[0]):
         if v in stuff:
              infotable.append(text[0][i+1])

    if scanForInfo('7. Country:',0,text[0]) != 'Canada':

        newText = text[2][text[2].index("The client to whose benefit payment is made"):len(text[2])-1]
        infotable.append(newText[newText.index("3. Given name:")+1])
        infotable.append(newText[newText.index("2. Surname:")+1])
        infotable.append(newText[newText.index("5. Street address:")+1] + " " + (newText[newText.index("9. Postal or zip code:")+1]))
        infotable.append(newText[newText.index("11. Date of birth:")+1])
        infotable.append(newText[newText.index("10. Telephone number:")+1])
        infotable.append(newText[newText.index("12. Occupation:")+1])
        infotable.append(newText[newText.index("14. Identifier:")+1])
 

    #client info
    clientSlice = text[0][text[0].index("The client ordering the EFT"):len(text[0])] + text[1][0:text[1].index("The individual or entity sending the payment instructions for the EFT")]
    print(clientSlice)
    infotable.append(clientSlice[clientSlice.index("3. Given name:")] + ' '.join(clientSlice[clientSlice.index("2. Surname:")]))
    infotable.append(clientSlice[clientSlice.index("5. Street address:")] + ' '.join(clientSlice[clientSlice.index("9. Postal or zip code:")]))
    infotable.append(clientSlice[clientSlice[text.index("11. Date of birth:")]])
    infotable.append(clientSlice[clientSlice.index("10. Telephone:")])         
    infotable.append(clientSlice[clientSlice.index("12. Occupation:")])

    if clientSlice[clientSlice.index("14. Identifier:")] == "Other":
            infotable.append(clientSlice[clientSlice.index("14a. If \'Other\', please specify:")])
    else:
            infotable.append(scanForInfo("14. Identifier:",0,text[1]))

    infotable.append(clientSlice[clientSlice.index("15. ID number:")])

    print(infotable)
    return infotable
