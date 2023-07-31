from googlesearch import search

print("Welcome to GST (Google Search Tool)")
print()
query=input("What do you want to search on Google: ")

if query == "exit":
   quit()


for i in search(query, start=0, stop=6):
	print(i)
