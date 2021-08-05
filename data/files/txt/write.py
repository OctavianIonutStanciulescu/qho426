
def search(books):
  print("Searching...")
  sections = []
  books = []
  with open("data/files/txt/books.txt") as file:
    data = file.readlines()
    for line in data:
      if line.startswith("Section"):
        sections.append(line.strip("Section:").strip("\n"))
      else:
        books.append(line.strip().strip("'"))
  print ("...Done")
  return (sections, books)
  
def save(section_books,tuplex):
  tuplex = search(1)
  print(tuplex)
  print("Saving...Done")
  with open("data/files/txt/section_books.txt", "w") as file:
    lines = (f"Sections: {tuplex[0]}\n Books: {tuplex[1]}")
    file.writelines(lines)
  
def run():
  data = search("data/files/txt/books.txt")
  save(data,1)

run()