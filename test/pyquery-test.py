from pyquery import PyQuery as pq



with file("section05.html") as f:
    s = f.read()


doc = pq(s)


for ex in doc("div[data-type='example']"):
	listing_type = ex[0].attrib["data-code-language"]
	
	print(listing_type + "\n")
	print(ex[0].text)
	print("\n\n")

