#The probe then sends the data back to Earth, consisting of three  integer  values. The firstvalue is the number of rowsin the image (height). The secondvalue is
#the number of columnsin the image (width). Finally, the binary sequence is converted to its decimal equivalent, and that number is sent as the third value.


bseq = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 

#convert decimal to binary complement no func

def binary_complement(bseq):
    bseq = [1 if x == 0 else 0 for x in bseq]
    return bseq

binary_complement(bseq)





#The probe then sends the data back to Earth, consisting of three  integer  values. The firstvalue is the number of rowsin the image (height). The secondvalue is
#the number of columnsin the image (width). Finally, the binary sequence is converted to its decimal equivalent, and that number is sent as the third value.
