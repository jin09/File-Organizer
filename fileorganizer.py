import os

docs = ["DOC", "DOCX", "PPT", "PPTX", "PAGES", "PDF", "ODT", "ODP", "XLSX", "XLS", "ODS", "TXT", "IN", "OUT", "RTF"]
images = ["JPG", "JPEG", "GIF", "PNG", "SVG"]
audio = ["MP3", "WAV", "WMA", "MKA", "AAC", "MID", "RA", "RAM", "RM", "OGG"]
video = ["FLV", "WMV", "MOV", "MP4", "MPEG", "3GP", "MKV"]
code = ["CPP", "RB", "PY", "HTML", "CSS", "JS"]
sys_files = ["DEB", "EXE", "SH", "BUNDLE"]
compressed = ["RAR", "JAR", "ZIP", "TAR", "MAR", "ISO", "LZ", "7ZIP", "TGZ", "GZ", "BZ2"]
subtitles = ["SRT"]
torrent = ["TORRENT"]


def create_folders():
    current = os.getcwd()
    list_dir = []
    docs_folder = current + "\\docs"
    list_dir.append(docs_folder)
    images_folder = current + "\\images"
    list_dir.append(images_folder)
    audio_folder = current + "\\audio"
    list_dir.append(audio_folder)
    video_folder = current + "\\video"
    list_dir.append(video_folder)
    code_folder = current + "\\code"
    list_dir.append(code_folder)
    sys_files_folder = current + "\\system_files"
    list_dir.append(sys_files_folder)
    compressed_folder = current + "\\compressed"
    list_dir.append(compressed_folder)
    subtitles_folder = current + "\\subtitles"
    list_dir.append(subtitles_folder)
    torrent_folder = current + "\\torrent"
    list_dir.append(torrent_folder)
    misc_folder = current + "\\misc"
    list_dir.append(misc_folder)

    for i in list_dir:
        if not os.path.exists(i):
            os.makedirs(i)

"""
Creates a dictionary of file types of the form:

{'RAM': 'audio', 'MKA': 'audio', 'DOC': 'docs', 'MID': 'audio', 'FLV': 'video',
 'MKV': 'video', 'MP4': 'video', 'EXE': 'sys_files', 'ISO': 'compressed', 'MP3': 'audio',
  'PDF': 'docs', 'CPP': 'code', 'DEB': 'sys_files', 'XLS': 'docs', 'TORRENT': 'torrent',
   'AAC': 'audio', 'TAR': 'compressed', 'ODP': 'docs', 'ODS': 'docs', 'ODT': 'docs', 'HTML': 'code',
    'RAR': 'compressed', 'RA': 'audio', 'RB': 'code', 'PPT': 'docs', 'RM': 'audio', 'TXT': 'docs',
     'LZ': 'compressed', 'OUT': 'docs', 'PPTX': 'docs', 'XLSX': 'docs', 'DOCX': 'docs', 'ZIP': 'compressed',
      '7ZIP': 'compressed', 'SVG': 'images', 'JAR': 'compressed', 'WMV': 'video', 'JPEG': 'images',
       'GZ': 'compressed', 'GIF': 'images', 'MAR': 'compressed', 'BUNDLE': 'sys_files', 'SRT': 'subtitles',
        'IN': 'docs', 'WAV': 'audio', 'WMA': 'audio', 'JS': 'code', 'CSS': 'code', 'MPEG': 'video',
         'BZ2': 'compressed', 'MOV': 'video', 'JPG': 'images', 'TGZ': 'compressed', 'SH': 'sys_files',
          'PY': 'code', 'OGG': 'audio', '3GP': 'video', 'PAGES': 'docs', 'PNG': 'images'}

"""
def create_dictionary_of_file_types():
    hash = {}
    for i in docs:
        hash[i] = "docs"
    for i in images:
        hash[i] = "images"
    for i in audio:
        hash[i] = "audio"
    for i in video:
        hash[i] = "video"
    for i in code:
        hash[i] = "code"
    for i in sys_files:
        hash[i] = "sys_files"
    for i in compressed:
        hash[i] = "compressed"
    for i in subtitles:
        hash[i] = "subtitles"
    for i in torrent:
        hash[i] = "torrent"
    print(hash)
    return hash


def put_files_in_folder():
    dictionary = create_dictionary_of_file_types()

    for root, dirs, files in os.walk(os.getcwd()):
        for i in files:
            if not i.startswith("."):
                print i
                x = i.split(".")
                file_type = x[-1]
                print file_type
                file_name = x[0]
                print file_name
                file_type = file_type.upper()
                print(file_type)
                if file_type in dictionary:
                    actual_destination_folder = dictionary[file_type]
                    if file_name != "fileorganizer":
                        os.rename(os.getcwd() + "\\" + i, os.getcwd() + "\\" + actual_destination_folder + "\\" + i)
                else:
                    if file_name != "fileorganizer":
                        os.rename(os.getcwd() + "\\" + i, os.getcwd() + "\\misc\\" + i)

create_folders()
put_files_in_folder()
