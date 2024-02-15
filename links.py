import csv

link_lists_base = [
    'https://hasaki.vn/danh-muc/my-pham-high-end-c1907.html',
    'https://hasaki.vn/danh-muc/cham-soc-da-mat-c4.html',
    'https://hasaki.vn/danh-muc/trang-diem-c23.html',
    'https://hasaki.vn/danh-muc/cham-soc-toc-c96.html',
    'https://hasaki.vn/danh-muc/cham-soc-co-the-c12.html',
    'https://hasaki.vn/danh-muc/cham-soc-ca-nhan-c2049.html',
    'https://hasaki.vn/danh-muc/nuoc-hoa-c103.html',
    'https://hasaki.vn/danh-muc/thuc-pham-chuc-nang-c156.html'
]

link_id = [
            101109230,  #cham-soc-da-mat
            101201646,  #cham-soc-toc
            101198988,  #cham-soc-co-the
            101112932,  #trang-diem
            129246448,  #nuoc-hoa
            129246440,  #thuc-pham-chuc-nang
]
page_lists = [4, 81, 45, 19, 27, 16, 4, 4]
page_lists_shopee = [8, 2, 4, 3, 1, 2]

# Danh sách đường dẫn đến các file CSV
csv_paths = [
    "D:/Crawl_Hasaki_web/Data_hasaki_web/my-pham-high-end.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/cham-soc-da-mat.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/trang-diem.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/cham-soc-toc.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/cham-soc-co-the.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/cham-soc-ca-nhan.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/nuoc-hoa.csv",
    "D:/Crawl_Hasaki_web/Data_hasaki_web/thuc-pham-chuc-nang.csv"
]

csv_paths_shopee = [
    "D:/Crawl_Hasaki_web/cham-soc-da-mat-shopee.csv",
    "D:/Crawl_Hasaki_web/cham-soc-toc-shopee.csv",
    "D:/Crawl_Hasaki_web/cham-soc-co-the-shopee.csv",
    "D:/Crawl_Hasaki_web/trang-diem-shopee.csv-shopee",
    "D:/Crawl_Hasaki_web/nuoc-hoa-shopee.csv",
    "D:/Crawl_Hasaki_web/thuc-pham-chuc-nang-shopee.csv"
]