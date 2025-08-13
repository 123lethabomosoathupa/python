from pathlib import Path
contents = "Jackie Chan was here\n"
contents += "He loves to kick enemies\n"
contents += "He is the original stuntman actor\n"
path = Path('H:\CodeCollege\WebDev\Python\python_work\classwork\chap10\programming.txt')
path.write_text(contents)