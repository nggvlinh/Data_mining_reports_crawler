# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from flask import Flask
import  requests as rq
import psycopg2


app = Flask(__name__, template_folder='template')
app.secret_key = 'replace later'

@app.route('/')
def index():
    #print(crawler_chitiet())
    #print(crawler_tennganh())
    connect()
    #print(demo())

    return 'successfully'

# xoa khoang trang
def spacee(sp):
    return  sp.strip()

# xoa dau -
def dele(de):
  return de.replace('-','')

# cao thong tin co ban nganh
def crawler_tennganh ():
    html = rq.get("https://tuyensinh.ctu.edu.vn/chuong-trinh-dai-tra/841-danh-muc-nganh-va-chi-tieu-tuyen-sinh-dhcq.html/gioi-thieu-nganh/551-cong-nghe-ky-thuat-hoa-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')
    # new_feed1 = soup.find('section', class_='article-content clearfix').find_all('p')

    # Công nghệ kỹ thuật hóa học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    GT2 = new_feed[9].text
    s = GT + GT1 + GT2
    # TDVT  = new_feed[10].text

    VT = new_feed[11].text
    VT1 = new_feed[12].text
    VT2 = new_feed[13].text
    VT3 = new_feed[14].text
    s1 = VT + VT1 + VT2 + VT3
    # print(TDVT+"\n")
    # print(VT +"\n")
    # print(VT1+"\n")
    # print(VT2 +"\n")
    # print(VT3+"\n")

    TDNLV = new_feed[15].text
    NLV = new_feed[16].text
    NLV1 = new_feed[17].text
    NLV2 = new_feed[18].text
    s2 = NLV + NLV1 +NLV2

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/490-ky-thuat-co-dien-tu").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật cơ - điện tử
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s3 = GT + GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    VT6 = new_feed[16].text
    s4 = VT + VT1 +VT2 +VT3


    TDNLV = new_feed[17].text
    NLV = new_feed[18].text
    NLV1 = new_feed[19].text
    NLV2 = new_feed[20].text
    NLV3 = new_feed[21].text
    NLV4 = new_feed[22].text
    NLV5 = new_feed[23].text
    NLV6 = new_feed[24].textVT3
    s5 = NLV +NLV1 +NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/489-ky-thuat-dien").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật điện
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    s6 = GT

    TDVT = new_feed[8].text
    VT = new_feed[9].text
    VT1 = new_feed[10].text
    VT2 = new_feed[11].text
    VT3 = new_feed[12].text
    s7 = VT + VT1+VT2

    TDNLV = new_feed[13].text
    NLV = new_feed[14].text
    NLV1 = new_feed[15].text
    NLV2 = new_feed[16].text
    NLV3 = new_feed[17].text
    NLV4 = new_feed[18].text
    NLV5 = new_feed[19].text
    NLV6 = new_feed[20].text
    NLV7 = new_feed[21].text
    s8 = NLV + NLV1+NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/486-ky-thuat-dien-tu-vien-thong").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật điện tử - viễn thông
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s9 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s10 = VT+VT1+VT2+VT3
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s11 = NLV+NLV1+NLV2

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/488-ky-thuat-dieu-khien-va-tu-dong-hoa").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # KT điều khiển và tự động hóa
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s12 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s13 = VT +VT1+VT2+VT3
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s14 = NLV +NLV2+NLV1

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/752-ky-thuat-may-tinh").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật máy tính
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s15 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s16 = VT + VT3+VT2+VT1
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s17 = NLV +NLV1 +NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/485-ky-thuat-xay-dung").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật xây dựng
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s18 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s19 = VT +VT1 +VT2+VT3
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s20 =NLV +NLV1 +NLV2

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/744-ky-thuat-vat-lieu").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật Vật liệu
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    GT2 = new_feed[9].text
    s21 = GT +GT1+GT2
    TDVT = new_feed[10].text
    VT = new_feed[11].text
    VT1 = new_feed[12].text
    VT2 = new_feed[13].text
    s22 =VT +VT1+VT2
    TDNLV = new_feed[14].text
    NLV = new_feed[15].text
    NLV1 = new_feed[16].text
    NLV2 = new_feed[17].text
    NLV3 = new_feed[18].text
    NLV4 = new_feed[19].text
    s23 = NLV +NLV1+NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/754-ky-thuat-xay-dung-cong-trinh-giao-thong").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # KTXD công trình giao thông
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s24 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s25 = VT+VT1+VT2
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    NLV4 = new_feed[21].text
    NLV5 = new_feed[22].text
    s26 = NLV +NLV1+NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/753-ky-thuat-xay-dung-cong-trinh-thuy").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # KT xây dựng công trình thủy
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    s27 = GT

    TDVT = new_feed[8].text
    VT = new_feed[9].text
    VT1 = new_feed[11].text
    VT2 = new_feed[11].text
    VT3 = new_feed[12].text
    s28 = VT+VT1+VT2
    TDNLV = new_feed[13].text
    NLV = new_feed[14].text
    NLV1 = new_feed[15].text
    NLV2 = new_feed[16].text
    NLV3 = new_feed[17].text
    NLV4 = new_feed[18].text
    s29 = NLV3+NLV+NLV2

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/491-quan-ly-cong-nghiep").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Quản lý công nghiệp
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s30 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s31 = VT +VT2+VT1
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    NLV4 = new_feed[21].text
    s32 = NLV2+NLV+NLV3+NLV1

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/496-cong-nghe-thong-tin").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Công nghệ thông tin
    TDGT = new_feed[7].text
    GT = new_feed[8].text
    GT1 = new_feed[9].text
    s33 =GT +GT1
    TDVT = new_feed[10].text
    VT = new_feed[11].text
    VT1 = new_feed[12].text
    VT2 = new_feed[13].text
    VT3 = new_feed[14].text
    s34 = VT +VT1 +VT2
    TDNLV = new_feed[15].text
    NLV = new_feed[16].text
    NLV1 = new_feed[17].text
    NLV2 = new_feed[18].text
    s35 = NLV1 +NLV+ NLV2

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/552-he-thong-thong-tin").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Hệ thống thông tin
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s36 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s37 = VT +VT1 + VT2+VT3

    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s38 = NLV +NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/493-khoa-hoc-may-tinh").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Khoa học máy tính
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s39 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s40 = VT +VT1+VT2
    TDNLV = new_feed[16].text
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    s41 = NLV +NLV3 +NLV2 +NLV1

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/495-ky-thuat-phan-mem").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Kỹ thuật phần mềm
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s42 = GT+GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    VT6 = new_feed[16].text
    VT7 = new_feed[17].text
    s43 = VT+VT2+VT1+VT3+VT4
    TDNLV = new_feed[18].text
    NLV = new_feed[19].text
    NLV1 = new_feed[20].text
    NLV2 = new_feed[21].text
    NLV3 = new_feed[22].text
    NLV4 = new_feed[23].text
    s44 = NLV1 +NLV+NLV2+NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/494-m-ng-may-tinh-va-truy-n-thong-d-li-u").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Mạng MT và Truyền thông DL

    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s42 = GT+GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    s43 = VT +VT1+VT3

    TDNLV = new_feed[14].text
    NLV = new_feed[15].text
    NLV1 = new_feed[16].text
    NLV2 = new_feed[17].text
    s44 = NLV+NLV2+NLV1
    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/539-chinh-tri-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Chính trị học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s45 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    s46 = VT + VT1 + VT2

    TDNLV = new_feed[15].text
    NLV = new_feed[16].text
    NLV1 = new_feed[17].text
    NLV2 = new_feed[18].text
    NLV3 = new_feed[19].text
    NLV4 = new_feed[20].textVT2
    s47= NLV + NLV1 + NLV2+ NLV3
    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/538-triet-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Triết học
    GT = new_feed[6].text
    GT1 = new_feed[7].text
    GT2 = new_feed[8].text
    GT3 = new_feed[9].text
    s48 = GT +GT1 +GT2+GT3
    VT = new_feed[10].text
    s49= VT
    NLV = new_feed[11].text
    s50 = NLV

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/546-cong-nghe-sinh-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Công nghệ sinh học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s51 = GT + GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    VT6 = new_feed[16].text
    VT7 = new_feed[17].text
    s52 = VT +VT1 +VT2+VT3

    TDNLV = new_feed[18].text
    NLV = new_feed[19].text
    NLV1 = new_feed[20].text
    NLV2 = new_feed[21].text
    NLV3 = new_feed[22].text
    NLV4 = new_feed[23].text
    s53 = NLV + NLV1 +NLV2
    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/745-hoa-duoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Hóa dược
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s54 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    s55 = VT +VT1 + VT2 +VT3
    TDNLV = new_feed[15].text
    NLV = new_feed[16].text
    NLV1 = new_feed[17].text
    NLV2 = new_feed[18].text
    NLV3 = new_feed[19].text
    NLV4 = new_feed[20].text
    s56 = NLV+ NLV1 +NLV2 +NLV3

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/525-hoa-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Hóa học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s57 = GT

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    s58 = VT
    NLV = new_feed[17].text
    NLV1 = new_feed[18].text
    NLV2 = new_feed[19].text
    NLV3 = new_feed[20].text
    NLV4 = new_feed[21].text
    NLV5 = new_feed[22].text
    NLV6 = new_feed[23].text
    s59 = NLV

    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/766-sinh-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Sinh học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s60 = GT +GT1

    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    VT6 = new_feed[16].text
    s61 = VT+VT1+VT2+VT3

    TDNLV = new_feed[17].text
    NLV = new_feed[18].text
    NLV1 = new_feed[19].text
    NLV2 = new_feed[20].text
    NLV3 = new_feed[21].text
    NLV4 = new_feed[22].text
    s62 = NLV+NLV1+NLV2
    html = rq.get("https://tuyensinh.ctu.edu.vn/gioi-thieu-nganh/766-sinh-hoc").text
    soup = BeautifulSoup(html, 'html5lib')
    new_feed = soup.find('section', class_='article-content clearfix').find_all('p')

    # Sinh học
    TDGT = new_feed[6].text
    GT = new_feed[7].text
    GT1 = new_feed[8].text
    s63 = GT +GT1
    TDVT = new_feed[9].text
    VT = new_feed[10].text
    VT1 = new_feed[11].text
    VT2 = new_feed[12].text
    VT3 = new_feed[13].text
    VT4 = new_feed[14].text
    VT5 = new_feed[15].text
    VT6 = new_feed[16].text
    s64 = VT +VT1+VT2+VT3

    TDNLV = new_feed[17].text
    NLV = new_feed[18].text
    NLV1 = new_feed[19].text
    NLV2 = new_feed[20].text
    NLV3 = new_feed[21].text
    NLV4 = new_feed[22].text
    s65 = NLV1 +NLV +NLV2+NLV3
    return s , s1 , s3
# cao nganh chi tiet
def crawler_chitiet ():
    html = rq.get("https://tuyensinh.ctu.edu.vn/chuong-trinh-dai-tra/841-danh-muc-nganh-va-chi-tieu-tuyen-sinh-dhcq.html").text
    soup = BeautifulSoup(html, "lxml")

    new_feed = soup.find('section', class_='article-content clearfix').find_all('a')
    ND = soup.find('section', class_='article-content clearfix').find('p')
    divs_TieuDe = soup("html", "com_content view-article itemid-285 j36 mm-hover")
    divs_DL = soup("p", "MsoNormal")

    DL = soup.find('section', class_='article-content clearfix').find_all('p')

    TieuDe = divs_TieuDe[0].find("title").text
    TieuDe1 = divs_TieuDe[0].find("h4").text
    DuLieu = divs_DL[7].text
    # Công nghệ kỹ thuật hóa học
    Ma_CN = divs_DL[6].text
    Ten_CN = divs_DL[7].text
    ToHop_CN = divs_DL[8].text
    ChiTieu_CN = divs_DL[9].text
    TT19_CN = divs_DL[10].text
    TT18_CN = divs_DL[11].text
    TT17_CN = divs_DL[12].text

    # Kỹ thuật cơ điện tử
    Ma_CN1 = divs_DL[13].text
    Ten_CN1 = divs_DL[14].text
    ToHop_CN1 = divs_DL[15].text
    ChiTieu_CN1 = divs_DL[16].text
    TT19_CN1 = divs_DL[17].text
    TT18_CN1 = divs_DL[18].text
    TT17_CN1 = divs_DL[19].text

    # Kỹ thuật cơ khí
    Ma_CN2 = divs_DL[20].text
    Ten_CN2 = divs_DL[21].text
    TenCn_CN2 = divs_DL[22].text
    TenCn1_CN2 = divs_DL[23].text
    ToHop_CN2 = divs_DL[24].text
    ChiTieu_CN2 = divs_DL[25].text
    TT19_CN2 = divs_DL[26].text
    TT18_CN2 = divs_DL[27].text
    TT17_CN2 = divs_DL[28].text

    # ky thuat dien
    Ma_CN3 = divs_DL[29].text
    Ten_CN3 = divs_DL[30].text
    ToHop_CN3 = divs_DL[31].text
    ChiTieu_CN3 = divs_DL[32].text
    TT19_CN3 = divs_DL[33].text
    TT18_CN3 = divs_DL[34].text
    TT17_CN3 = divs_DL[35].text

    # ky thuat dien tu - vien thong
    Ma_CN4 = divs_DL[36].text
    Ten_CN4 = divs_DL[37].text
    ToHop_CN4 = divs_DL[38].text
    ChiTieu_CN4 = divs_DL[39].text
    TT19_CN4 = divs_DL[40].text
    TT18_CN4 = divs_DL[41].text
    TT17_CN4 = divs_DL[42].text
    #Kỹ thuật điều khiển và tự động hóa
    Ma_CN5 = divs_DL[43].text
    Ten_CN5 = divs_DL[44].text
    ToHop_CN5 = divs_DL[45].text
    ChiTieu_CN5 = divs_DL[46].text
    TT19_CN5 = divs_DL[47].text
    TT18_CN5 = divs_DL[48].text
    TT17_CN5 = divs_DL[49].text
    # Kỹ thuật máy tính
    Ma_CN6 = divs_DL[50].text
    Ten_CN6 = divs_DL[51].text
    ToHop_CN6 = divs_DL[52].text
    ChiTieu_CN6 = divs_DL[53].text
    TT19_CN6 = divs_DL[54].text
    TT18_CN6 = divs_DL[55].text
    TT17_CN6 = divs_DL[56].text
    # Kỹ thuật xây dựng
    Ma_CN7 = divs_DL[57].text
    Ten_CN7 = divs_DL[58].text
    ToHop_CN7 = divs_DL[59].text
    ChiTieu_CN7 = divs_DL[60].text
    TT19_CN7 = divs_DL[61].text
    TT18_CN7 = divs_DL[62].text
    TT17_CN7 = divs_DL[63].text
    # Kỹ thuật vật liệu
    Ma_CN8 = divs_DL[64].text
    Ten_CN8 = divs_DL[65].text
    ToHop_CN8 = divs_DL[66].text
    ChiTieu_CN8 = divs_DL[67].text
    TT19_CN8 = divs_DL[68].text
    TT18_CN8 = divs_DL[69].text
    TT17_CN8 = divs_DL[70].text
    # Kỹ thuật xây dựng công trình giao thông
    Ma_CN9 = divs_DL[71].text
    Ten_CN9 = divs_DL[72].text
    ToHop_CN9 = divs_DL[73].text
    ChiTieu_CN9 = divs_DL[74].text
    TT19_CN9 = divs_DL[75].text
    TT18_CN9 = divs_DL[76].text
    TT17_CN9 = divs_DL[77].text
    # Kỹ thuật xây dựng công trình thủy
    Ma_CN10 = divs_DL[78].text
    Ten_CN10 = divs_DL[79].text
    ToHop_CN10 = divs_DL[80].text
    ChiTieu_CN10 = divs_DL[81].text
    TT19_CN10 = divs_DL[82].text
    TT18_CN10 = divs_DL[83].text
    TT17_CN10 = divs_DL[84].text
    # Quản lý công nghiệp
    Ma_CN11 = divs_DL[85].text
    Ten_CN11 = divs_DL[86].text
    ToHop_CN11 = divs_DL[87].text
    ChiTieu_CN11 = divs_DL[88].text
    TT19_CN11 = divs_DL[89].text
    TT18_CN11 = divs_DL[90].text
    TT17_CN11 = divs_DL[91].text
    # Công nghệ thông tin
    Ma_CNTT = divs_DL[92].text
    Ten_CNTT = divs_DL[93].text
    TenCn_CNTT = divs_DL[94].text
    TenCn1_CNTT = divs_DL[95].text
    ToHop_CNTT = divs_DL[96].text
    ChiTieu_CNTT = divs_DL[97].text
    TT19_CNTT = divs_DL[98].text
    TT18_CNTT = divs_DL[99].text
    TT17_CNTT = divs_DL[100].text
    # Hệ thống thông tin
    Ma_CNTT1 = divs_DL[101].text
    Ten_CNTT1 = divs_DL[102].text
    ToHop_CNTT1 = divs_DL[103].text
    ChiTieu_CNTT1 = divs_DL[104].text
    TT19_CNTT1 = divs_DL[105].text
    TT18_CNTT1 = divs_DL[106].text
    TT17_CNTT1 = divs_DL[107].text
    # Khoa học máy tính
    Ma_CNTT2 = divs_DL[108].text
    Ten_CNTT2 = divs_DL[109].text
    ToHop_CNTT2 = divs_DL[110].text
    ChiTieu_CNTT2 = divs_DL[111].text
    TT19_CNTT2 = divs_DL[112].text
    TT18_CNTT2 = divs_DL[113].text
    TT17_CNTT2 = divs_DL[114].text
    # Kỹ thuật phần mềm
    Ma_CNTT3 = divs_DL[115].text
    Ten_CNTT3 = divs_DL[116].text
    ToHop_CNTT3 = divs_DL[117].text
    ChiTieu_CNTT3 = divs_DL[118].text
    TT19_CNTT3 = divs_DL[119].text
    TT18_CNTT3 = divs_DL[120].text
    TT17_CNTT3 = divs_DL[121].text
    # Mạng máy tính và truyền thông dữ liệu
    Ma_CNTT4 = divs_DL[122].text
    Ten_CNTT4 = divs_DL[123].text
    ToHop_CNTT4 = divs_DL[124].text
    ChiTieu_CNTT4 = divs_DL[125].text
    TT19_CNTT4 = divs_DL[126].text
    TT18_CNTT4 = divs_DL[127].text
    TT17_CNTT4 = divs_DL[128].text
    # Chính trị học
    Ma_CT = divs_DL[129].text
    Ten_CT = divs_DL[130].text
    ToHop_CT = divs_DL[131].text
    ChiTieu_CT = divs_DL[132].text
    TT19_CT = divs_DL[133].text
    TT18_CT = divs_DL[134].text
    TT17_CT = divs_DL[135].text
    # Triết học
    Ma_CT1 = divs_DL[136].text
    Ten_CT1 = divs_DL[137].text
    ToHop_CT1 = divs_DL[138].text
    ChiTieu_CT1 = divs_DL[139].text
    TT19_CT1 = divs_DL[140].text
    TT18_CT1 = divs_DL[141].text
    TT17_CT1 = divs_DL[142].text
    # Công nghệ sinh học
    Ma_KHTN = divs_DL[143].text
    Ten_KHTN = divs_DL[144].text
    ToHop_KHTN = divs_DL[145].text
    ChiTieu_KHTN = divs_DL[146].text
    TT19_KHTN = divs_DL[147].text
    TT18_KHTN = divs_DL[148].text
    TT17_KHTN = divs_DL[149].text
    # Hóa dược
    Ma_KHTN1 = divs_DL[150].text
    Ten_KHTN1 = divs_DL[151].text
    ToHop_KHTN1 = divs_DL[152].text
    ChiTieu_KHTN1 = divs_DL[153].text
    TT19_KHTN1 = divs_DL[154].text
    TT18_KHTN1 = divs_DL[155].text
    TT17_KHTN1 = divs_DL[156].text
    # Hóa học
    Ma_KHTN2 = divs_DL[157].text
    Ten_KHTN2 = divs_DL[158].text
    ToHop_KHTN2 = divs_DL[159].text
    ChiTieu_KHTN2 = divs_DL[160].text
    TT19_KHTN2 = divs_DL[161].text
    TT18_KHTN2 = divs_DL[162].text
    TT17_KHTN2 = divs_DL[163].text
    # Sinh học
    Ma_KHTN3 = divs_DL[164].text
    Ten_KHTN3 = divs_DL[165].text
    ToHop_KHTN3 = divs_DL[166].text
    ChiTieu_KHTN3 = divs_DL[167].text
    TT19_KHTN3 = divs_DL[168].text
    TT18_KHTN3 = divs_DL[169].text
    TT17_KHTN3 = divs_DL[170].text
    # Toán ứng dụng
    Ma_KHTN4 = divs_DL[171].text
    Ten_KHTN4 = divs_DL[172].text
    ToHop_KHTN4 = divs_DL[173].text
    ChiTieu_KHTN4 = divs_DL[174].text
    TT19_KHTN4 = divs_DL[175].text
    TT18_KHTN4 = divs_DL[176].text
    TT17_KHTN4 = divs_DL[177].text
    # Vật lý kỹ thuật
    Ma_KHTN5 = divs_DL[178].text
    Ten_KHTN5 = divs_DL[179].text
    ToHop_KHTN5 = divs_DL[180].text
    ChiTieu_KHTN5 = divs_DL[181].text
    TT19_KHTN5 = divs_DL[182].text
    TT18_KHTN5 = divs_DL[183].text
    TT17_KHTN5 = divs_DL[184].text
    # Ngôn ngữ Anh
    Ma_KHXH = divs_DL[185].text
    Ten_KHXH = divs_DL[186].text
    TenCn_KHXH = divs_DL[187].text
    TenCn1_KHXH = divs_DL[188].text
    ToHop_KHXH = divs_DL[189].text
    ChiTieu_KHXH = divs_DL[190].text
    TT19_KHXH = divs_DL[191].text
    TT18_KHXH = divs_DL[192].text
    TT17_KHXH = divs_DL[193].text
    # Ngôn ngữ Pháp
    Ma_KHXH1 = divs_DL[194].text
    Ten_KHXH1 = divs_DL[195].text
    ToHop_KHXH1 = divs_DL[196].text
    ChiTieu_KHXH1 = divs_DL[197].text
    TT19_KHXH1 = divs_DL[198].text
    TT18_KHXH1 = divs_DL[199].text
    TT17_KHXH1 = divs_DL[200].text
    # Thông tin - thư viện
    Ma_KHXH2 = divs_DL[201].text
    Ten_KHXH2 = divs_DL[202].text
    ToHop_KHXH2 = divs_DL[203].text
    ChiTieu_KHXH2 = divs_DL[204].text
    TT19_KHXH2 = divs_DL[205].text
    TT18_KHXH2 = divs_DL[206].text
    TT17_KHXH2 = divs_DL[207].text
    # Văn học
    Ma_KHXH3 = divs_DL[208].text
    Ten_KHXH3 = divs_DL[209].text
    ToHop_KHXH3 = divs_DL[210].text
    ChiTieu_KHXH3 = divs_DL[211].text
    TT19_KHXH3 = divs_DL[212].text
    TT18_KHXH3 = divs_DL[213].text
    TT17_KHXH3 = divs_DL[214].text
    # Việt Nam học
    Ma_KHXH4 = divs_DL[215].text
    Ten_KHXH4 = divs_DL[216].text
    TenCn_KHXH4 = divs_DL[217].text
    ToHop_KHXH4 = divs_DL[218].text
    ChiTieu_KHXH4 = divs_DL[219].text
    TT19_KHXH4 = divs_DL[220].text
    TT18_KHXH4 = divs_DL[221].text
    TT17_KHXH4 = divs_DL[222].text
    # Xã hội học
    Ma_KHXH5 = divs_DL[223].text
    Ten_KHXH5 = divs_DL[224].text
    ToHop_KHXH5 = divs_DL[225].text
    ChiTieu_KHXH5 = divs_DL[226].text
    TT19_KHXH5 = divs_DL[227].text
    TT18_KHXH5 = divs_DL[228].text
    TT17_KHXH5 = divs_DL[229].text
    # Kế toán
    Ma_KT = divs_DL[230].text
    Ten_KT = divs_DL[231].text
    ToHop_KT = divs_DL[232].text
    ChiTieu_KT = divs_DL[233].text
    TT19_KT = divs_DL[234].text
    TT18_KT = divs_DL[235].text
    TT17_KT = divs_DL[236].text
    # Kiểm toán
    Ma_KT1 = divs_DL[237].text
    Ten_KT1 = divs_DL[238].text
    ToHop_KT1 = divs_DL[239].text
    ChiTieu_KT1 = divs_DL[240].text
    TT19_KT1 = divs_DL[241].text
    TT18_KT1 = divs_DL[242].text
    TT17_KT1 = divs_DL[243].text
    # Kinh doanh quốc tế
    Ma_KT2 = divs_DL[244].text
    Ten_KT2 = divs_DL[245].text
    ToHop_KT2 = divs_DL[246].text
    ChiTieu_KT2 = divs_DL[247].text
    TT19_KT2 = divs_DL[248].text
    TT18_KT2 = divs_DL[249].text
    TT17_KT2 = divs_DL[250].text
    # Kinh doanh thương mại
    Ma_KT3 = divs_DL[251].text
    Ten_KT3 = divs_DL[252].text
    ToHop_KT3 = divs_DL[253].text
    ChiTieu_KT3 = divs_DL[254].text
    TT19_KT3 = divs_DL[255].text
    TT18_KT3 = divs_DL[256].text
    TT17_KT3 = divs_DL[257].text
    # Kinh tế
    Ma_KT4 = divs_DL[258].text
    Ten_KT4 = divs_DL[259].text
    ToHop_KT4 = divs_DL[260].text
    ChiTieu_KT4 = divs_DL[261].text
    TT19_KT4 = divs_DL[262].text
    TT18_KT4 = divs_DL[263].text
    TT17_KT4 = divs_DL[264].text
    # Kinh tế nông nghiệp
    Ma_KT5 = divs_DL[265].text
    Ten_KT5 = divs_DL[266].text
    ToHop_KT5 = divs_DL[267].text
    ChiTieu_KT5 = divs_DL[268].text
    TT19_KT5 = divs_DL[269].text
    TT18_KT5 = divs_DL[270].text
    TT17_KT5 = divs_DL[271].text
    # Kinh tế tài nguyên thiên nhiên
    Ma_KT6 = divs_DL[272].text
    Ten_KT6 = divs_DL[273].text
    ToHop_KT6 = divs_DL[274].text
    ChiTieu_KT6 = divs_DL[275].text
    TT19_KT6 = divs_DL[276].text
    TT18_KT6 = divs_DL[277].text
    TT17_KT6 = divs_DL[278].text
    # Marketing
    Ma_KT7 = divs_DL[279].text
    Ten_KT7 = divs_DL[280].text
    ToHop_KT7 = divs_DL[281].text
    ChiTieu_KT7 = divs_DL[282].text
    TT19_KT7 = divs_DL[283].text
    TT18_KT7 = divs_DL[284].text
    TT17_KT7 = divs_DL[285].text
    # Quản trị dịch vụ du lịch và lữ hành
    Ma_KT8 = divs_DL[286].text
    Ten_KT8 = divs_DL[287].text
    ToHop_KT8 = divs_DL[288].text
    ChiTieu_KT8 = divs_DL[289].text
    TT19_KT8 = divs_DL[290].text
    TT18_KT8 = divs_DL[291].text
    TT17_KT8 = divs_DL[292].text
    # Quản trị kinh doanh
    Ma_KT9 = divs_DL[293].text
    Ten_KT9 = divs_DL[294].text
    ToHop_KT9 = divs_DL[295].text
    ChiTieu_KT9 = divs_DL[296].text
    TT19_KT9 = divs_DL[297].text
    TT18_KT9 = divs_DL[298].text
    TT17_KT9 = divs_DL[299].text
    # Tài chính - Ngân hàng
    Ma_KT10 = divs_DL[300].text
    Ten_KT10 = divs_DL[301].text
    ToHop_KT10 = divs_DL[302].text
    ChiTieu_KT10 = divs_DL[303].text
    TT19_KT10 = divs_DL[304].text
    TT18_KT10 = divs_DL[305].text
    TT17_KT10 = divs_DL[306].text
    # Luật
    Ma_L = divs_DL[307].text
    Ten_L = divs_DL[308].text
    TenCn_L = divs_DL[309].text
    TenCn1_L = divs_DL[310].text
    TenCn2_L = divs_DL[311].text
    ToHop_L = divs_DL[312].text
    ChiTieu_L = divs_DL[313].text
    TT19_L = divs_DL[314].text
    TT18_L = divs_DL[315].text
    TT17_L = divs_DL[316].text
    # Khoa học môi trường
    Ma_MT = divs_DL[317].text
    Ten_MT = divs_DL[318].text
    ToHop_MT = divs_DL[319].text
    ChiTieu_MT = divs_DL[320].text
    TT19_MT = divs_DL[321].text
    TT18_MT = divs_DL[322].text
    TT17_MT = divs_DL[323].text
    # Kỹ thuật môi trường
    Ma_MT1 = divs_DL[324].text
    Ten_MT1 = divs_DL[325].text
    ToHop_MT1 = divs_DL[326].text
    ChiTieu_MT1 = divs_DL[327].text
    TT19_MT1 = divs_DL[328].text
    TT18_MT1 = divs_DL[329].text
    TT17_MT1 = divs_DL[330].text
    # Quản lý đất đai
    Ma_MT2 = divs_DL[331].text
    Ten_MT2 = divs_DL[332].text
    ToHop_MT2 = divs_DL[333].text
    ChiTieu_MT2 = divs_DL[334].text
    TT19_MT2 = divs_DL[335].text
    TT18_MT2 = divs_DL[336].text
    TT17_MT2 = divs_DL[337].text
    # Quản lý tài nguyên và môi trường
    Ma_MT3 = divs_DL[338].text
    Ten_MT3 = divs_DL[339].text
    ToHop_MT3 = divs_DL[340].text
    ChiTieu_MT3 = divs_DL[341].text
    TT19_MT3 = divs_DL[342].text
    TT18_MT3 = divs_DL[343].text
    TT17_MT3 = divs_DL[344].text
    # Bảo vệ thực vật
    Ma_NN = divs_DL[345].text
    Ten_NN = divs_DL[346].text
    ToHop_NN = divs_DL[347].text
    ChiTieu_NN = divs_DL[348].text
    TT19_NN = divs_DL[349].text
    TT18_NN = divs_DL[350].text
    TT17_NN = divs_DL[351].text
    # Chăn nuôi
    Ma_NN1 = divs_DL[352].text
    Ten_NN1 = divs_DL[353].text
    ToHop_NN1 = divs_DL[354].text
    ChiTieu_NN1 = divs_DL[355].text
    TT19_NN1 = divs_DL[356].text
    TT18_NN1 = divs_DL[357].text
    TT17_NN1 = divs_DL[358].text
    # Công nghệ sau thu hoạch
    Ma_NN2 = divs_DL[359].text
    Ten_NN2 = divs_DL[360].text
    ToHop_NN2 = divs_DL[361].text
    ChiTieu_NN2 = divs_DL[362].text
    TT19_NN2 = divs_DL[363].text
    TT18_NN2 = divs_DL[364].text
    TT17_NN2 = divs_DL[365].text
    # Công nghệ thực phẩm
    Ma_NN3 = divs_DL[366].text
    Ten_NN3 = divs_DL[367].text
    ToHop_NN3 = divs_DL[368].text
    ChiTieu_NN3 = divs_DL[369].text
    TT19_NN3 = divs_DL[370].text
    TT18_NN3 = divs_DL[371].text
    TT17_NN3 = divs_DL[372].text
    # Công nghệ rau hoa quả và cảnh quan
    Ma_NN4 = divs_DL[373].text
    Ten_NN4 = divs_DL[374].text
    ToHop_NN4 = divs_DL[375].text
    ChiTieu_NN4 = divs_DL[376].text
    TT19_NN4 = divs_DL[377].text
    TT18_NN4 = divs_DL[378].text
    TT17_NN4 = divs_DL[379].text
    # Khoa học cây trồng
    Ma_NN5 = divs_DL[380].text
    Ten_NN5 = divs_DL[381].text
    TenCn_NN5 = divs_DL[382].text
    TenCn1_NN5 = divs_DL[383].text
    ToHop_NN5 = divs_DL[384].text
    ChiTieu_NN5 = divs_DL[385].text
    TT19_NN5 = divs_DL[386].text
    TT18_NN5 = divs_DL[387].text
    TT17_NN5 = divs_DL[388].text
    # Khoa học đất
    Ma_NN6 = divs_DL[389].text
    Ten_NN6 = divs_DL[390].text
    TenCn_NN6 = divs_DL[391].text
    ToHop_NN6 = divs_DL[392].text
    ChiTieu_NN6 = divs_DL[393].text
    TT19_NN6 = divs_DL[394].text
    TT18_NN6 = divs_DL[395].text
    TT17_NN6 = divs_DL[396].text
    # Nông học
    Ma_NN7 = divs_DL[397].text
    Ten_NN7 = divs_DL[398].text
    ToHop_NN7 = divs_DL[399].text
    ChiTieu_NN7 = divs_DL[400].text
    TT19_NN7 = divs_DL[401].text
    TT18_NN7 = divs_DL[402].text
    TT17_NN7 = divs_DL[403].text
    # Sinh học ứng dụng
    Ma_NN8 = divs_DL[404].text
    Ten_NN8 = divs_DL[405].text
    ToHop_NN8 = divs_DL[406].text
    ChiTieu_NN8 = divs_DL[407].text
    TT19_NN8 = divs_DL[408].text
    TT18_NN8 = divs_DL[409].text
    TT17_NN8 = divs_DL[410].text
    # Thú y
    Ma_NN10 = divs_DL[411].text
    Ten_NN10 = divs_DL[412].text
    ToHop_NN10 = divs_DL[413].text
    ChiTieu_NN10 = divs_DL[414].text
    TT19_NN10 = divs_DL[415].text
    TT18_NN10 = divs_DL[416].text
    TT17_NN10 = divs_DL[417].text
    # Giáo dục Công dân
    Ma_SP = divs_DL[418].text
    Ten_SP = divs_DL[419].text
    ToHop_SP = divs_DL[420].text
    ChiTieu_SP = divs_DL[421].text
    TT19_SP = divs_DL[422].text
    TT18_SP = divs_DL[423].text
    TT17_SP = divs_DL[424].text
    # Giáo dục Thể chất
    Ma_SP1 = divs_DL[425].text
    Ten_SP1 = divs_DL[426].text
    ToHop_SP1 = divs_DL[427].text
    ChiTieu_SP1 = divs_DL[428].text
    TT19_SP1 = divs_DL[429].text
    TT18_SP1 = divs_DL[430].text
    TT17_SP1 = divs_DL[431].text
    # Giáo dục Tiểu học
    Ma_SP2 = divs_DL[432].text
    Ten_SP2 = divs_DL[433].text
    ToHop_SP2 = divs_DL[434].text
    ChiTieu_SP2 = divs_DL[435].text
    TT19_SP2 = divs_DL[436].text
    TT18_SP2 = divs_DL[437].text
    TT17_SP2 = divs_DL[438].text
    # Sư phạm Địa lý
    Ma_SP3 = divs_DL[439].text
    Ten_SP3 = divs_DL[440].text
    ToHop_SP3 = divs_DL[441].text
    ChiTieu_SP3 = divs_DL[442].text
    TT19_SP3 = divs_DL[443].text
    TT18_SP3 = divs_DL[444].text
    TT17_SP3 = divs_DL[445].text
    # Sư phạm Hóa học
    Ma_SP4 = divs_DL[446].text
    Ten_SP4 = divs_DL[447].text
    ToHop_SP4 = divs_DL[448].text
    ChiTieu_SP4 = divs_DL[449].text
    TT19_SP4 = divs_DL[450].text
    TT18_SP4 = divs_DL[451].text
    TT17_SP4 = divs_DL[452].text
    # Sư phạm Lịch sử
    Ma_SP5 = divs_DL[453].text
    Ten_SP5 = divs_DL[454].text
    ToHop_SP5 = divs_DL[455].text
    ChiTieu_SP5 = divs_DL[456].text
    TT19_SP5 = divs_DL[457].text
    TT18_SP5 = divs_DL[458].text
    TT17_SP5 = divs_DL[459].text
    # Sư phạm Ngữ văn
    Ma_SP6 = divs_DL[460].text
    Ten_SP6 = divs_DL[461].text
    ToHop_SP6 = divs_DL[462].text
    ChiTieu_SP6 = divs_DL[463].text
    TT19_SP6 = divs_DL[464].text
    TT18_SP6 = divs_DL[465].text
    TT17_SP6 = divs_DL[466].text
    # Sư phạm Sinh học
    Ma_SP7 = divs_DL[467].text
    Ten_SP7 = divs_DL[468].text
    ToHop_SP7 = divs_DL[469].text
    ChiTieu_SP7 = divs_DL[470].text
    TT19_SP7 = divs_DL[471].text
    TT18_SP7 = divs_DL[472].text
    TT17_SP7 = divs_DL[473].text
    # Sư phạm Tin học
    Ma_SP8 = divs_DL[474].text
    Ten_SP8 = divs_DL[475].text
    ToHop_SP8 = divs_DL[476].text
    ChiTieu_SP8 = divs_DL[477].text
    TT19_SP8 = divs_DL[478].text
    TT18_SP8 = divs_DL[479].text
    TT17_SP8 = divs_DL[480].text
    # Sư phạm tiếng Anh
    Ma_SP9 = divs_DL[481].text
    Ten_SP9 = divs_DL[482].text
    ToHop_SP9 = divs_DL[483].text
    ChiTieu_SP9 = divs_DL[484].text
    TT19_SP9 = divs_DL[485].text
    TT18_SP9 = divs_DL[486].text
    TT17_SP9 = divs_DL[487].text
    # Sư phạm tiếng Pháp
    Ma_SP10 = divs_DL[488].text
    Ten_SP10 = divs_DL[489].text
    ToHop_SP10 = divs_DL[490].text
    ChiTieu_SP10 = divs_DL[491].text
    TT19_SP10 = divs_DL[492].text
    TT18_SP10 = divs_DL[493].text
    TT17_SP10 = divs_DL[494].text
    # Sư phạm Toán học
    Ma_SP11 = divs_DL[495].text
    Ten_SP11 = divs_DL[496].text
    ToHop_SP11 = divs_DL[497].text
    ChiTieu_SP11 = divs_DL[498].text
    TT19_SP11 = divs_DL[499].text
    TT18_SP11 = divs_DL[500].text
    TT17_SP11 = divs_DL[501].text
    # Sư phạm Vật lý
    Ma_SP12 = divs_DL[502].text
    Ten_SP12 = divs_DL[503].text
    ToHop_SP12 = divs_DL[504].text
    ChiTieu_SP12 = divs_DL[505].text
    TT19_SP12 = divs_DL[506].text
    TT18_SP12 = divs_DL[507].text
    TT17_SP12 = divs_DL[508].text
    # Bệnh học thủy sản
    Ma_TS = divs_DL[509].text
    Ten_TS = divs_DL[510].text
    ToHop_TS = divs_DL[511].text
    ChiTieu_TS = divs_DL[512].text
    TT19_TS = divs_DL[513].text
    TT18_TS = divs_DL[514].text
    TT17_TS = divs_DL[515].text
    # Công nghệ chế biến thủy sản
    Ma_TS1 = divs_DL[516].text
    Ten_TS1 = divs_DL[517].text
    ToHop_TS1 = divs_DL[518].text
    ChiTieu_TS1 = divs_DL[519].text
    TT19_TS1 = divs_DL[520].text
    TT18_TS1 = divs_DL[521].text
    TT17_TS1 = divs_DL[522].text
    # Nuôi trồng thủy sản
    Ma_TS2 = divs_DL[523].text
    Ten_TS2 = divs_DL[524].text
    ToHop_TS2 = divs_DL[525].text
    ChiTieu_TS2 = divs_DL[526].text
    TT19_TS2 = divs_DL[527].text
    TT18_TS2 = divs_DL[528].text
    TT17_TS2 = divs_DL[529].text
    # Quản lý thủy sản
    Ma_TS3 = divs_DL[530].text
    Ten_TS3 = divs_DL[531].text
    ToHop_TS3 = divs_DL[532].text
    ChiTieu_TS3 = divs_DL[533].text
    TT19_TS3 = divs_DL[534].text
    TT18_TS3 = divs_DL[535].text
    TT17_TS3 = divs_DL[536].text
    # Công nghệ thông tin
    Ma_HA = divs_DL[537].text
    Ten_HA = divs_DL[538].text
    ToHop_HA = divs_DL[539].text
    ChiTieu_HA = divs_DL[540].text
    TT19_HA = divs_DL[541].text
    TT18_HA = divs_DL[542].text
    TT17_HA = divs_DL[543].text
    # Kinh doanh nông nghiệp
    Ma_HA1 = divs_DL[544].text
    Ten_HA1 = divs_DL[545].text
    ToHop_HA1 = divs_DL[546].text
    ChiTieu_HA1 = divs_DL[547].text
    TT19_HA1 = divs_DL[548].text
    TT18_HA1 = divs_DL[549].text
    TT17_HA1 = divs_DL[550].text
    # Kinh tế nông nghiệp
    Ma_HA2 = divs_DL[551].text
    Ten_HA2 = divs_DL[552].text
    ToHop_HA2 = divs_DL[553].text
    ChiTieu_HA2 = divs_DL[554].text
    TT19_HA2 = divs_DL[555].text
    TT18_HA2 = divs_DL[556].text
    TT17_HA2 = divs_DL[557].text
    # Kỹ thuật xây dựng
    Ma_HA3 = divs_DL[558].text
    Ten_HA3 = divs_DL[559].text
    ToHop_HA3 = divs_DL[560].text
    ChiTieu_HA3 = divs_DL[561].text
    TT19_HA3 = divs_DL[562].text
    TT18_HA3 = divs_DL[563].text
    TT17_HA3 = divs_DL[564].text
    # Luật
    Ma_HA4 = divs_DL[565].text
    Ten_HA4 = divs_DL[566].text
    TenCn_HA4 = divs_DL[567].text
    ToHop_HA4 = divs_DL[568].text
    ChiTieu_HA4 = divs_DL[569].text
    TT19_HA4 = divs_DL[570].text
    TT18_HA4 = divs_DL[571].text
    TT17_HA4 = divs_DL[572].text
    # Ngôn ngữ Anh
    Ma_HA5 = divs_DL[573].text
    Ten_HA5 = divs_DL[574].text
    ToHop_HA5 = divs_DL[575].text
    ChiTieu_HA5 = divs_DL[576].text
    TT19_HA5 = divs_DL[577].text
    TT18_HA5 = divs_DL[578].text
    TT17_HA5 = divs_DL[579].text
    # Quản trị kinh doanh
    Ma_HA6 = divs_DL[580].text
    Ten_HA6 = divs_DL[581].text
    ToHop_HA6 = divs_DL[582].text
    ChiTieu_HA6 = divs_DL[583].text
    TT19_HA6 = divs_DL[584].text
    TT18_HA6 = divs_DL[585].text
    TT17_HA6 = divs_DL[586].text
    # Việt Nam học
    Ma_HA7 = divs_DL[587].text
    Ten_HA7 = divs_DL[588].text
    TenCn_HA7 = divs_DL[589].text
    ToHop_HA7 = divs_DL[590].text
    ChiTieu_HA7 = divs_DL[591].text
    TT19_HA7 = divs_DL[592].text
    TT18_HA7 = divs_DL[593].text
    TT17_HA7 = divs_DL[594].text
    return Ma_HA7,Ten_HA7,ToHop_HA7,ChiTieu_HA7, TT19_HA7,TT18_HA7,TT17_HA7

# demo lay link video
def demo():
    link11 = "https://tuyensinh.ctu.edu.vn/chuong-trinh-dai-tra/841-danh-muc-nganh-va-chi-tieu-tuyen-sinh-dhcq.html/gioi-thieu-nganh/551-cong-nghe-ky-thuat-hoa-hoc"
    linkchu = "https://tuyensinh.ctu.edu.vn"
    html = rq.get(link11).text
    soup = BeautifulSoup(html)

    return linkchu + soup.source['src']

# ket noi heroku
def connect() :
    try:
        connection = psycopg2.connect(user="xdjbqgulyhzhck",
                                      password="d8aa4a5f3335d5489970c10428d5adbcd7c7ad5d215ec54b8d0fd8afdaf9b763",
                                      host="ec2-52-72-65-76.compute-1.amazonaws.com",
                                      port="5432",
                                      database="db3kr1a2ptuutr")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")


        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        reate_table_query = '''CREATE TABLE dmnganh(
                 Manganh          TEXT PRIMARY KEY NOT NULL,
                 Tennganh         TEXT NOT NULL,
                 Tohop            TEXT NOT NULL,
                 Chitieu          TEXT NOT NULL,
                 TT2019           TEXT NOT NULL,
                 TT2018           TEXT NOT NULL,
                 TT2017           TEXT NOT NULL); '''

        #cursor.execute(create_table_query)
        #print("creeate success")

        print("bảng danh mục ngành")
        cursor.execute("SELECT * FROM dmnganh;")
        records1 = cursor.fetchall()
        print(records1)

        print("bảng chi tiet nganh")
        cursor.execute("SELECT * FROM chitietnganh;")
        records2 = cursor.fetchall()
        print(records2)


        #cursor.execute("ALTER TABLE dmnganh1 RENAME TO chitietnganh;")
        #print("success")

        connection.commit()
        #print("Table created successfully in PostgreSQL ")



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
    # pip freeze > requirements.txt