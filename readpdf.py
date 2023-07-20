import pdfreader
from handleIncomplete import extractIncomplete

things = ['1. Full name of entity:','12. Occupation:',"13. Client's account number:",'15. ID number:',"11. Date of birth:","4. Other/initial: 3. Given name:"]

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
                return False
        

infotable = []
def extractText(text, pdfOBJ,dir):
    infotable = []
    stuff =['External report number:','2. Date of transaction:','3. Amount of transaction:','4. Transaction currency:']
    if not "Electronic funds transfer - Incoming (EFTI)" in text[0]:
        print(dir, "could not read")
        return ['unable to extract:',dir]
    point = text[0].index("The client ordering the EFT")
    #report summary
    for i,v in enumerate(text[0]):
         if v in stuff:
              infotable.append(text[0][i+1])
    
    if text[0][text[0].index("Report process status:")+1] == "Incomplete":
        infotable = extractIncomplete(text,infotable)
        print(infotable)
        return infotable

    if scanForInfo('7. Country:',0,text[0]) != 'Canada':
        print('beneficiary')
        newText = text[2][text[2].index("The client to whose benefit payment is made"):len(text[2])-1]
        infotable.append(newText[newText.index("3. Given name:")+1] + " " + newText[newText.index("2. Surname:")+1])
        infotable.append(newText[newText.index("5. Street address:")+1] + " " + (newText[newText.index("9. Postal or zip code:")+1]))
        infotable.append(newText[newText.index("11. Date of birth:")+1])
        infotable.append(newText[newText.index("10. Telephone number:")+1])
        infotable.append(newText[newText.index("12. Occupation:")+1])
        infotable.append(newText[newText.index("14. Identifier:")+1])
        infotable.append("unfilled")
        x = ["unfilled" if x in things else x for x in infotable]
        print(x)

        # plastem packaging edge case:
        # if no beneficary given and surname, then check full name of entity
        # or if no beneficary name then use ordering client information
        return x
 

    #client info
    clientSlice = text[0][text[0].index("3a. 24-hour-rule indicator:"):] + text[1]
    #print(clientSlice)
    infotable.append(clientSlice[clientSlice.index("3. Given name:")+1] + ' ' + clientSlice[clientSlice.index("2. Surname:")+1])
    infotable.append(clientSlice[clientSlice.index("5. Street address:")+1] + ' ' + (clientSlice[clientSlice.index("9. Postal or zip code:")+1]))
    if clientSlice[clientSlice.index("11. Date of birth:")+1] == '12. Occupation:':
        print(dir)
        #print(text[0])
    infotable.append(clientSlice[clientSlice.index("11. Date of birth:")+1])
    infotable.append(clientSlice[clientSlice.index("10. Telephone number:")+1])         
    infotable.append(clientSlice[clientSlice.index("12. Occupation:")+1])

    if clientSlice[clientSlice.index("14. Identifier:")] == "Other":
            infotable.append(clientSlice[clientSlice.index("14a. If \'Other\', please specify:")+1])
    else:
            infotable.append(clientSlice[clientSlice.index("14. Identifier:")+1])

    infotable.append(clientSlice[clientSlice.index("15. ID number:")+1])

    filtered = ["unfilled" if x in things else x for x in infotable]
    print(filtered)
    return filtered
