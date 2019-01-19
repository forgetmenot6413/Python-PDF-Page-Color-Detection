#!/usr/bin/env python
import os.path
import sys, getopt
import subprocess
import collections

def main(argv):
        print "Easy Color Detection."
        if len(sys.argv) > 1:							
	        input_file = str(sys.argv[1])
	        if os.path.isfile(input_file):
			# use ghostscript to find pages containing color stuff
			# https://tex.stackexchange.com/questions/53493/detecting-all-pages-which-contain-color/61216#61216
			# If the CMY values are not 0 then the page is color.
			# e.g. page one is bw, page two has colours
				#Page 1
				#0.00000  0.00000  0.00000  0.02230 CMYK OK
				#Page 2
				#0.02360  0.02360  0.02360  0.02360 CMYK OK
			bashCommand = "gs -o - -sDEVICE=inkcov " + input_file
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()
			if error != None:
				print "There was an error parsing the input file " + input_file
				sys.exit(2)
			
			result = collections.OrderedDict()
			lastPage = ''
			for line in output.splitlines():
				line = line.strip()
				if line.startswith("Page"):
					lastPage = line
				elif line.find("CMYK") != -1:
				        i = 0
                                        CMYK = [0.0, 0.0, 0.0, 0.0]
					for value in line.split():
                                                if value in "OK":
                                                    i = -1
                                                if i == 0:
                                                    CMYK[i] = float(value)
                                                elif i == 1:
                                                    CMYK[i] = float(value)
                                                elif i == 2:
                                                    CMYK[i] = float(value)
                                                elif i == 3:
                                                    CMYK[i] = float(value) 
                                                elif i == -1:
                                                    print 'C : ' + str(CMYK[0]) + 'M : ' + str(CMYK[1]) + 'Y : ' + str(CMYK[2]) + 'K : ' + str(CMYK[3])
                                                    if len(set(CMYK)) != 1:
                                                        result[lastPage] = "Color"
                                                    elif len(set(CMYK)) == 1:
					                result[lastPage] = "BlackAndWhite"
                                                i += 1
			colorpages = ""
			colorpagescounter = 0
			for key, value in result.iteritems():
				if value == "Color":
					colorpages = colorpages + key.replace("Page ","") + ", "
					colorpagescounter += 1
			print(colorpages)
		else:
			print str(input_file) + " is not a valid file."

	else:
		print 'How to use: script.py <input.pdf>'
		sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])
