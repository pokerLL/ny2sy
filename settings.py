import os

tag_dict = {
    "title": "BOOK/",
    "author": "AU/",
    "create_time": "TIME/",
}

"""
json_data_file_path = "static/羊皮卷(伪).json"
template_md_file_path = "static/template.md"
output_md_file_path = "static/{}_out.md".format(json_data_file_path.split("/")[-1].split(".")[0])
"""

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
NOTE_DIR = os.path.join(DATA_DIR, "note")
STATIC_DIR = os.path.join(DATA_DIR, "static")
CARD_TEMPLATE_FILE = os.path.join(STATIC_DIR, "template.md")