def solution(s):

    # First we create a new list to save the characters and the spaces we will need later
    newp = list()

    # We create a loop to go to every character in our string.
    for i in range(len(s)):

        # The first character will be keep the same, this system is called lowerCamelCase.
        if i == 0:

            newp.append(s[i])

    # The next characters.
        else:

            # If the character is upper, we will add a space first and the character later to our list.
            # The space must be a space not a empty value, if this is not so we will have problems later.
            if s[i].isupper() == True:

                newp.append(" ")

                newp.append(s[i])

    # If it is not, we simply add it to the list.
            else:

                newp.append(s[i])

    # Finally, we create a string with the characters in our list using '.join'.
    result = ''.join(newp)

    return result
