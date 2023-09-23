# Checks if any of the elements in the list contains another class as element (making the parent class polymorphic and thus returning a list of empty string)
def containsKey(l, d):
  return any(i in d for i in l)


# Returns the list of probable words from a dictionary object (with a text matching using the last statement component if possible)
def findProbableWordsDict(dictionaryObj,
                          filterFlag,
                          textToMatch = None):
  varNames = sorted(list(dictionaryObj.keys()))
  filteredVarNames = varNames
  # Filter based on the last statement component i.e. the text matching component
  if filterFlag == True:
    filteredVarNames = list(
      filter(lambda x: x.startswith(textToMatch), varNames))
  idx = 5 if len(filteredVarNames) > 5 else len(filteredVarNames)
  return (filteredVarNames[:idx])


# Returns the list of probable words from a list object (with a text matching using the last statement component if possible)
def findProbableWordsList(listObj,
                          filterFlag: bool,
                          textToMatch: str = None):
  varNames = sorted(listObj)
  filteredVarNames = varNames
  # Filter based on the last statement component i.e. the text matching component
  if filterFlag == True:
    filteredVarNames = list(
      filter(lambda x: x.startswith(textToMatch), varNames))
  idx = 5 if len(filteredVarNames) > 5 else len(filteredVarNames)
  return (filteredVarNames[:idx])


# Assumptions made:
# 1. A class has only one name i.e. has only one key for it's values
# 2. A class doesn't extend container datatypes and thus we cannot have classA<string> datatype
# 3. A statement without a '.' would cause a word search on the class list
# 4. Any statement which does not have a possible solution returns the solution of list of empty string
def getNextProbableWords(classes, statements):

  # Output dictionary to store solutions for statements
  output = {}

  # Make the list of classes into a dict where each class is a key (since each class can only have one key)
  dictClasses = {k: v for clazz in classes for k, v in clazz.items()}

  # Loop through each statement
  for statement in statements:

    # Flag to see if text search is needed at the end or only key search
    keySearchFlag = statement.endswith('.')

    # Case for if no '.' is mentioned to allow for text matching search on class list
    if "." in statement:
      statementComponents = statement.split(".")
      # Guard case to check if class exists within the class list
      if statementComponents[0] in dictClasses:
        tempSearch = dictClasses[statementComponents[0]]
      else:
        output[statement] = [""]
        continue
    else:
      statementComponents = ["", statement]
      tempSearch = dictClasses

    # Loop through statement components and navigate through the objects using tempSearch as a variable to store the current object
    for i in range(1, len(statementComponents)):

      # Boolean variables to store if object is currently a list or a dict
      isDict = isinstance(tempSearch, dict)
      isStr = isinstance(tempSearch, str)

      # End case to perform suggestion of probable words
      if i == len(statementComponents) - 1:
        # Only empty strings exist so return list of empty string
        if isStr:
          output[statement] = [""]
          break

        # keySearchFlag == True suggests only suggested words need to be taken without text matching
        if keySearchFlag == True:
          if isDict:
            output[statement] = findProbableWordsDict(tempSearch, False)

          else:
            if containsKey(tempSearch, dictClasses):
              output[statement] = [""]

            else:
              output[statement] = findProbableWordsList(tempSearch, False)

        # Else case suggests we need to perform text matching
        else:
          if isDict:
            output[statement] = findProbableWordsDict(tempSearch, True,
                                                      statementComponents[i])

          else:
            if containsKey(tempSearch, dictClasses):
              output[statement] = [""]

            else:
              output[statement] = findProbableWordsList(
                tempSearch, True, statementComponents[i])

      elif statementComponents[i] not in tempSearch:
        output[statement] = [""]
        break

      # Progress by setting the new object to be worked on to tempSearch
      else:
        search = statementComponents[i]
        # If dict find the value from the key value pair and only take the datatype within the container datatype
        if isDict:
          v = tempSearch[statementComponents[i]]
          search = v
          startIdx = v.rfind("<")
          endIdx = v.find(">")
          if startIdx != -1:
            search = v[startIdx + 1:endIdx]

        if search in dictClasses:
          tempSearch = dictClasses[search]

        else:
          output[statement] = [""]

  return output
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()