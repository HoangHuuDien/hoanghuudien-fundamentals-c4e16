import pyexcel

a_list_of_dictionaries = [
  {
      "title" : "hôm nay trời đẹp",
      "link" : "https://www.google.com.vn/?hl=vi"
  },
  {
      "title" : "hôm nay trời đẹp",
      "link" : "https://www.google.com.vn/?hl=vi"
  },
  {
      "title" : "hôm nay trời đẹp",
      "link" : "https://www.google.com.vn/?hl=vi"
  },
]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="text.xlsx")
