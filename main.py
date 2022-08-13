# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Create a variable to hold the story of Dracula 
draculaText = readBook()
# Create a variable to convert whole text to lowercase
draculaText = draculaText.lower()
#create a variable to hold individual words in the text 
words = draculaText.split()


#------------- Main Body of Text -----------------------# 

print("=== Results ===")
print()
# set variable for the count and set to 0
four_letter_count = 0
# use len function for any item of text (word) that is 4 char
for word in words: 
  if len(word) == 4:
     four_letter_count += 1 # add it to the variable 
                 
print(f"~ There are {four_letter_count} words that are four letters long.")
print()
  
#------------------------------------------------------#     

# Create an empty dictionary 
draculaDict = {}

# For every 'item' word in the text 'words':
for word in words:
  # Check if the word is already in dictionary
  if word in draculaDict:
    # Adding new count of 1 occurance to dictionary
    draculaDict[word] = draculaDict[word] + 1
    
  else:
    # Add the word to dictionary with count 1
    draculaDict[word] = 1
    
print(f"~ The following words show up 500 or more times throughout the text:")
print()

# Print the contents of dictionary if occur over 500 times
for key in list(draculaDict.keys()):
  if draculaDict[key] >= 500:
    print(f"{key} - {draculaDict[key]}")

# -----------------------------------------------------#
print()
# Variable for most appearances 'largest' & set to 0 
largest = 0
print()
for key in list(draculaDict.keys()):
  # compare the key to varible 'largest' and if bigger:
  if draculaDict[key] > largest:
    # set 'largest' to equal to the key dictionary
    largest = draculaDict[key]
    print(f" ~  '{key}' appears {largest} amount of times")