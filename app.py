from bs4 import BeautifulSoup
from flask import Flask
import  requests

app = Flask(__name__)
app.secret_key = 'replace later'

@app.route('/')
def index():
    html = requests.get("https://tuyensinh.ctu.edu.vn/chuong-trinh-dai-tra/841-danh-muc-nganh-va-chi-tieu-tuyen-sinh-dhcq.html").text
    soup = BeautifulSoup(html, 'html5lib')

    new_feed = soup.find('section', class_='article-content clearfix').find_all('a')
    ND = soup.find('section', class_='article-content clearfix').find('p')
    divs_TieuDe = soup("html", "com_content view-article itemid-285 j36 mm-hover")
    divs_DL = soup("p", "MsoNormal")

    DL = soup.find('section', class_='article-content clearfix').find_all('p')

    TieuDe = divs_TieuDe[0].find("title").text
    TieuDe1 = divs_TieuDe[0].find("h4").text
    DuLieu = divs_DL[7].text

    Ma_CN = divs_DL[6].text
    Ten_CN = divs_DL[7].text
    ToHop_CN = divs_DL[8].text
    ChiTieu_CN = divs_DL[9].text
    TT19_CN = divs_DL[10].text
    TT18_CN = divs_DL[11].text
    TT17_CN = divs_DL[12].text
    print(Ma_CN, Ten_CN, ToHop_CN,
          ChiTieu_CN,
          TT19_CN,
          TT18_CN,
          TT17_CN)
    return 'I am a live'

if __name__ == '__main__' :

    app.run(debug=True)