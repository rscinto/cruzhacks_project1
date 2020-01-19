# img_path = r"C:\Users\oranm\github\cruzhacks_project1\local_server\img\can.jpg"
import pathlib
import os,webbrowser


print(webbrowser._browsers)
def show_photo(name):
    name_ = name + ".jpg"
    img_path = pathlib.Path.cwd() / "local_server" / "img" / name_
    if img_path.is_file():
        iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                                "Internet Explorer\\IEXPLORE.EXE")
        browser = webbrowser.get(	"chromium")
        browser.open(str(img_path))
    else:
        print("Item not in database found")
# show_photo("bag")
show_photo("card")
