import pyperclip 

def link_prompt():
    title = input("enter text:")
    link = input("enter link:")
    md = f"[{title}]({link})"
    pyperclip.copy(md)
    return md


  """
  new ideas 
  csv to table markdown
  CRUD markdown application
  """
