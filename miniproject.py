# Importing RegEx module
import re


# Creating Class
class file_search:
    # Creating method and it contains self, string arguments.
    def search_word(self, string):
        # creating attribute
        self.string = string
        # Opening input text file
        input_file = open("input.txt", 'rt')
        #  Reading text in the input file
        text = input_file.read()
        #  finding the string, irrespective of cases
        result = re.findall(string, text, re.M | re.I)
        i = 0
        x = []
        m = 0
        while i < len(result):
            # Searching first string of the output file
            if i == 0:
                f = re.search(result[i], text)
                i += 1
                k = f.span()
                m = k[1]
                # Appending the strings to output file
                x.append(text[k[0]-9:k[0]]+' '+string+' '+text[k[1]+1:k[1]+9])
            else:
                # Searching remaining strings of the output file
                f = re.search(result[i], text[m+1:])
                i += 1
                k = f.span()
                m = k[1]
                # Appening the strings to output file
                x.append(text[k[0]-9:k[0]]+' '+string+' '+text[k[1]+1:k[1]+9])
        y = []
        y.append(str(len(result)))
        for z in range(1, len(x)+1):
            y.append(str(z) + ": " + x[z-1].strip())
        #  Creating output file
        dest = string+".txt"
        #  Opening output file
        with open(dest, 'a') as a:
            #  Writing the lines into output file
            a.writelines('\n'.join(y))
# Creating Main function
if __name__ == "__main__":
    #    creating object
    object_search = file_search()
    #  Enter the input string to search
    string = input("enter a string to search: ")
    #   Searching the required string
    object_search.search_word(string)