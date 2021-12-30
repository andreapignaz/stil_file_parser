#Read patterns from stil file

#Set up constants

#Line number where you find Pattern "_pattern_" or similar in the stil file
line_where_patterns_start = 6964
number_of_scan_chains = 18
number_of_patterns = 10

#Some variables for our beloved RAM memory

pattern_index = 0
line_index = 0
linea = ""

#Open the file
file = open("patterns.stil", "r")
fileout = open("output.txt","w")

for line_index in range(line_where_patterns_start - 1):
    file.readline()

#Discard the first lines
for line_index in range(6):
    file.readline()

#Read the header of the first pattern
linea = file.readline()
linea = linea.strip()
linea_toCompare = "\"pattern " + str(pattern_index) + "\": Call \"load_unload\" {"
if linea != linea_toCompare:
    print(linea)
    print("Error")
    quit()
print("Reading pattern number " + str(pattern_index))
fileout.write("Pattern Number " + str(pattern_index) + "\n")

#Read the pattern to put into the scan chain
for line_index in range(number_of_scan_chains):
    linea = file.readline()
    linea = linea.strip()
    stringa_divisa = linea.split('=')
    pattern = stringa_divisa[1]
    pattern = pattern.replace(';','')
    pattern = pattern.replace('}','')
    fileout.write("Scan chain input ")
    fileout.write(pattern + "\n")
    #Generated: the pattern as input of the scan chain.  

#Read and verifty the header of the capture
linea = file.readline()
linea = linea.strip()
linea_toCompare = "Call \"multiclock_capture\" {"
if linea != linea_toCompare:
    print(linea)
    print("Error when reading line " + linea)
    quit()

#Read pattern PIs and expected POs
linea = file.readline()
linea = linea.strip()
stringa_divisa = linea.split('=')
pattern = stringa_divisa[1]
pattern = pattern.replace(';','')
fileout.write("Primary Input ")
fileout.write(pattern + "\n")
#Generated: the pattern as input of the primary input.
linea = file.readline()
linea = linea.strip()
stringa_divisa = linea.split('=')
pattern = stringa_divisa[1]
pattern = pattern.replace(';','')
pattern = pattern.replace('}','')
pattern = pattern.replace('L','0')
pattern = pattern.replace('H','1')
fileout.write("Primary Output ")
fileout.write(pattern  + "\n")
#Generated: the pattern as output of the primary output.

for pattern_index in range(1,number_of_patterns):
    linea = file.readline()
    linea = linea.strip()
    linea_toCompare = "\"pattern " + str(pattern_index) + "\": Call \"load_unload\" {"
    if linea != linea_toCompare:
        print(linea)
        print("Error")
        quit()
    print("Reading pattern number " + str(pattern_index))
    fileout.write("\nPattern Number: " + str(pattern_index) + "\n") 
    for line_index in range(number_of_scan_chains):
        linea = file.readline()
        linea = linea.strip()
        stringa_divisa = linea.split('=')
        pattern = stringa_divisa[1]
        pattern = pattern.replace(';','')
        pattern = pattern.replace('}','')
        pattern = pattern.replace('L','0')
        pattern = pattern.replace('H','1')
        fileout.write("Expected Scan Chain Output ")
        fileout.write(pattern + "\n")
        #Generated: the pattern as output of the scan chain.
    for line_index in range(number_of_scan_chains):
        linea = file.readline()
        linea = linea.strip()
        stringa_divisa = linea.split('=')
        pattern = stringa_divisa[1]
        pattern = pattern.replace(';','')
        pattern = pattern.replace('}','')
        fileout.write("Scan Chain Input ")
        fileout.write(pattern + "\n")
        #Generated: the pattern as input of the scan chain.
    #Read pattern PIs and expected POs
    #Read and verifty the header of the capture
    linea = file.readline()
    linea = linea.strip()
    linea_toCompare = "Call \"multiclock_capture\" {"
    if linea != linea_toCompare:
        print(linea)
        print("Error when reading line " + linea)
        quit()
    linea = file.readline()
    linea = linea.strip()
    stringa_divisa = linea.split('=')
    pattern = stringa_divisa[1]
    pattern = pattern.replace(';','')
    fileout.write("Primary Input ")
    fileout.write(pattern + "\n")              
    #Generated: the pattern as input of the primary input.
    linea = file.readline()
    linea = linea.strip()
    stringa_divisa = linea.split('=')
    pattern = stringa_divisa[1]
    pattern = pattern.replace(';','')
    pattern = pattern.replace('}','')
    pattern = pattern.replace('L','0')
    pattern = pattern.replace('H','1')
    fileout.write("Primary Output ")
    fileout.write(pattern + "\n")
    #Generated: the pattern as output of the primary output.
      



