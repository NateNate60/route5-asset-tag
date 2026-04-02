#!/bin/python

import qrcode

def generate (start: int, count: int):
    file_text = "<html><body><table><tbody>"
    for i in range(start, start + count):
        tag_no = 'A' + str(i).zfill(4)
        img = qrcode.make(f"https://inventory-new.routefivecollectibles.com/tag/{tag_no}")
        img.save(f"{tag_no}.png")
        file_text += f'<tr><td style="margin-top: 100px"><img src="./{tag_no}.png" height="70"/></td><td width="150"><p ><span style="font-family: Overpass ExtraBold">Route Five Collectibles</span><br/><span style="font-family: Overpass">{tag_no}</span></p></td></tr>'
    file_text += "</tbody></table></body></html>"
    with open("tags800.html", 'w') as f:
        f.write(file_text)

if __name__ == "__main__":
    generate(750, 50)