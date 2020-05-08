from bs4 import BeautifulSoup
from flask import Flask
import  requests
import psycopg2

app = Flask(__name__)
app.secret_key = 'replace later'

@app.route('/')
def index():
    crawle()
    connect()
    return 'I am a live'

def crawle ():
    html = requests.get("https://tuyensinh.ctu.edu.vn/chuong-trinh-dai-tra/841-danh-muc-nganh-va-chi-tieu-tuyen-sinh-dhcq.html").text
    soup = BeautifulSoup(html, "lxml")

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

def connect() :
    try:
        connection = psycopg2.connect(user="eecggdupfmuiyf",
                                      password="9e43ebc95ea8c477df591eabeb26a42bfa7b77386ed2581c6acb6b74354e2176",
                                      host="ec2-54-86-170-8.compute-1.amazonaws.com",
                                      port="5432",
                                      database="d3lhnjrp51u6dl")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == '__main__' :

    app.run(debug=True)