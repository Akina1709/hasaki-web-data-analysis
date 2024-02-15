import links
import requests
from bs4 import BeautifulSoup
import numpy as np


def get_links_from_hasaki(link_lists_base, num_pages):
    list_links = []
    for link, num in zip(link_lists_base, num_pages):
        list_links.extend([link + f'?p={i}' for i in range(1, num + 1)])
    return list_links


link_lists = get_links_from_hasaki(links.link_lists_base, links.page_lists)


def get_detailed_info(idx, lists, f):
    print('counter :', idx)
    li = lists[idx]
    print("link:", li)
    html_doc = requests.get(li)
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    # get new price, discount, old price.
    block_price = soup.find_all('div', {'class': 'width_common block_price space_bottom_3'})
    # get name
    name_lists = soup.find_all('div', {'class': 'width_common txt_color_1 space_bottom_3'})
    # get description
    vn_names_divs = soup.find_all('div', class_='vn_names')
    print("len block price:", len(block_price))
    str1 = ' '
    for block, item, des in zip(block_price, name_lists, vn_names_divs):
        new_price = block.find('strong', class_='item_giamoi txt_16').text.strip()
        span_element_discount = block.find('span', class_='discount_percent2_deal')
        if span_element_discount is not None:
            discount_percent = span_element_discount.text.strip()
        else:
            discount_percent = "not available"

        span_element_old_price = block.find('span', class_='item_giacu txt_12 right')
        if span_element_old_price is not None:
            old_price = span_element_old_price.text.strip()
        else:
            old_price = "not available"
        item_name = item.find('strong').text.strip()
        describe = des.text.strip()
        describe_before_comma = describe.split(',')[0].strip()
        str1 = f'{item_name}, {describe_before_comma}, {new_price}, {discount_percent}, {old_price}, \n'
        f.write(str1)


print("link_lists", len(link_lists))


def write_info_to_csv(lists, pages):
    idx_page = 0
    idx = 0
    cumulative_sum_pages = np.cumsum(np.array(pages))
    while idx_page < len(pages):
        print("idx_page:", idx_page)
        f = open(links.csv_paths[idx_page], 'w', encoding='utf-8-sig')
        header = "NSX, Description, New Price, Discount percent, Old Price, \n"
        f.write(header)
        while idx < len(lists):
            if (idx + 1) != cumulative_sum_pages[idx_page]:
                get_detailed_info(idx, lists, f)
                idx += 1
            elif (idx + 1) == cumulative_sum_pages[idx_page]:
                get_detailed_info(idx, lists, f)
                idx += 1
                break
        f.close()
        idx_page += 1


write_info_to_csv(link_lists, links.page_lists)


