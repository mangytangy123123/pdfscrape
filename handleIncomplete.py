def extractIncomplete(text, infoTable):
    stuff = [x for x in infoTable]
    print("incomplete report")
    # dob telephone occupation id#

    clientSlice = text[0][text[0].index("3a. 24-hour-rule indicator:"):] + text[1]
    stuff.append(clientSlice[clientSlice.index("3. Given name:")+1] + " " + clientSlice[clientSlice.index("2. Surname:")+1])
    stuff.append(clientSlice[clientSlice.index("5. Street address:")+1] + " " + (clientSlice[clientSlice.index("9. Postal or zip code:")+1]))

    if clientSlice[clientSlice.index("11. Date of birth:")+1] == "12. Occupation:":
        stuff.append("unfilled")
    else:
        stuff.append(clientSlice[clientSlice.index("11. Date of birth:")+1])

    if clientSlice[clientSlice.index("10. Telephone number:")+1] == "11. Date of birth:":
        stuff.append("unfilled")
    else:
        stuff.append(clientSlice[clientSlice.index("10. Telephone number:")+1])

    if clientSlice[clientSlice.index("12. Occupation:")+1] == "13. Client's account number:":
        stuff.append("unfilled")
    else:
        stuff.append(clientSlice[clientSlice.index("12. Occupation:")+1])

    if clientSlice[clientSlice.index("14. Identifier:")] == "Other":
            stuff.append(clientSlice[clientSlice.index("14a. If \'Other\', please specify:")+1])
    else:
            stuff.append(clientSlice[clientSlice.index("14. Identifier:")+1])

    stuff.append(clientSlice[clientSlice.index("15. ID number:")+1])
    
    return stuff