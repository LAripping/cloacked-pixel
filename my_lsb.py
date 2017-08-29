#!/usr/bin/python

from PIL import Image

import sys
import struct

def extract(in_file, out_file):
	# Process source image
	img = Image.open(in_file)
	(width, height) = img.size
	conv = img.convert("RGBA").getdata()
	print "[+] Image size: %dx%d pixels." % (width, height)

	# Extract LSBs
	v = []
	for h in range(height):
		for w in range(width):
			(r, g, b, a) = conv.getpixel((w, h))
			v.append(r & 1)
			v.append(g & 1)
			v.append(b & 1)

        print "[+] Size of bit-vector: " + str(len(v))		
	data_out = assemble(v)

	# Decrypt
	#cipher = AESCipher(password)
	#data_dec = cipher.decrypt(data_out)
        
        print "[+] Size of data: "+ str(len(data_out))
        data_dec = data_out

	# Write decrypted data
	out_f = open(out_file, "wb")
	out_f.write(data_dec)
	out_f.close()
	
	print "[+] Written extracted data to %s." % out_file

# Statistical analysis of an image to detect LSB steganography



# Assemble an array of bits into a binary file
def assemble(v):    
	bytes = ""

	length = len(v)
	for idx in range(0, len(v)/8):
		byte = 0
		for i in range(0, 8):
			if (idx*8+i < length):
				byte = (byte<<1) + v[idx*8+i]                
		bytes = bytes + chr(byte)

        print "[+] Total bytes: "+ str(len(bytes)) 
        return bytes


if __name__ == "__main__":
    extract(sys.argv[1],sys.argv[2])
