import sys
def main():
	for line in sys.stdin:
	    lista = []
	    string1 = line
	    lenstring = len(string1)
	    if string1 == '':
	        break
	    for i in range(0,lenstring) :
	        if string1[i] == 'A' or string1[i] == 'B' or string1[i] == 'C':
	            lista.insert(i,'2')
	            
	        elif string1[i] == 'D' or string1[i] == 'E' or string1[i] == 'F':
	            lista.insert(i,'3') 
	            
	        elif string1[i] == 'G' or string1[i] == 'H' or string1[i] == 'I':
	            lista.insert(i,'4') 
	            
	        elif string1[i] == 'J' or string1[i] == 'K' or string1[i] == 'L':
	            lista.insert(i,'5') 
	            
	        elif string1[i] == 'M' or string1[i] == 'N' or string1[i] == 'O':
	            lista.insert(i,'6') 
	            
	        elif string1[i] == 'P' or string1[i] == 'Q' or string1[i] == 'R' or string1[i] == 'S' :
	            lista.insert(i,'7') 
	            
	        elif string1[i] == 'T' or string1[i] == 'U' or string1[i] == 'V':
	            lista.insert(i,'8') 
	            
	        elif string1[i] == 'W' or string1[i] == 'X' or string1[i] == 'Y' or string1[i] == 'Z':
	            lista.insert(i,'9') 
	            
	        elif string1[i] == '1':
	            lista.insert(i,'1') 
	            
	        elif string1[i] == '0':
	            lista.insert(i,'0') 
	            
	        elif string1[i] == '-':
	            lista.insert(i,'-')
	    lista = "".join(lista)
	    print(lista)
main()
