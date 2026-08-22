import requests
from urllib.parse import urlparse
import threading
path_url = (".mp3",".m4a",".wav",".flac",".aac",".ogg")

class DownloadMypackage:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.info = []
        self.is_exiting = True
    def should_exit(self):
            return self.is_exiting
    @staticmethod
    def is_url(url):
        res = urlparse(url)
        if not(res.scheme in ["http","https"] and res.netloc):
            return False
        path = res.path.lower()
        if path.endwith(path_url):
            return True
        return False
        
    def add_url(self):
        while self.should_exit():
            try:
                music_name = input("请输入音乐名称 输入q 退出:")
                if music_name.lower() =="q":
                    break
                music_url = input("请输入下载的音乐链接:")

                music_dict = {"name":music_name
                                  ,"url":music_url}
                if self.is_url(music_url):
                        self.info.append(music_dict)
                        print("继续输入:")
                else:
                    print("请重新输入:")
            except Exception as ex:
                print(f"输入错误:{ex}")
                return
            if not self.should_exit():
                break
    def download(self,name,url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(name + ".mp3".lower(),"wb") as f:
                    f.write(response.content)
        except Exception as ex:
            print(f"{self.name}下载失败:{ex}")
        return f"{self.name}下载完成"



if __name__ == "__main__":
    s = DownloadMypackage(name="",url="")
    s.add_url()
    thread = []
    for music_list in s.info:
        t = threading.Thread(target=s.download, args=(music_list["name"], music_list["url"]))
        thread.append(t)
        t.start()
    for t in thread:
        t.join()
        print("下载完成")




