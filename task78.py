import zlib
text='hello world!hello world!hello world!hello world!'
data=zlib.compress(text.encode("utf-8"))
print (data, "\n")

sata=zlib.compress(text.encode("utf-16"))
print (sata,"\n")
ata=zlib.decompress(data)
print(ata,"\n")
