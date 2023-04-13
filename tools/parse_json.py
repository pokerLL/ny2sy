import json
import copy

from tools.utils import get_book_info
from settings import *

def parse_json_to_md(json_data_file_path,template_md_file_path,output_md_file_path):
    with open(json_data_file_path,"r",encoding="utf-8") as f:
        josn_data = json.load(f)

    with open(template_md_file_path,'r',encoding="utf-8") as f:
        note_template_md = f.read()

    search_text = josn_data['bookName']
    book_info = get_book_info(search_text)

    outf = open(output_md_file_path,"w+",encoding='utf-8')

    for note_data in josn_data["noteList"]:
        temp_text = note_template_md
        note_item_text = note_data["text"]
        note_item_note = note_data["note"]
        note_item_time = note_data["showTime"].split(" ")[0]

        note_item_text = note_item_text.replace("\n\n","\n> ")
        note_item_note = note_item_note.replace("\n\n","\n> ")

        temp_data= copy.copy(book_info)
        temp_data["text"] = note_item_text
        temp_data["note"] = note_item_note
        temp_data["create_time"] = note_item_time


        for k,v in temp_data.items():
            temp_text = temp_text.replace("{{"+k+"}}",tag_dict.get(k,'')+v)
        
        outf.write(temp_text)

    outf.close()

