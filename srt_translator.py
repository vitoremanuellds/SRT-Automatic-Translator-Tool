import srt
import xml.etree.ElementTree as ET
import re
from deep_translator import GoogleTranslator
import html5lib
import argparse

def parseContent(subtitle: ET.Element, fromLang: str, toLang: str):
    pattern = re.compile(r'({\\an\d*})')
    if (subtitle.text != None):
        texts = pattern.split(subtitle.text)
        for i in range(len(texts)):
            text = texts[i]
            if pattern.match(text) == None:
                texts[i] = GoogleTranslator(source=fromLang, target=toLang).translate(text)
        subtitle.text = ''.join(texts)
    
    for child in subtitle:
        parseContent(child, fromLang, toLang)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="python srt_translator.py",
        description="This script translates the text inside SRT files from a language to another.")
    
    parser.add_argument("file", type=str, help="The path to the SRT File")
    parser.add_argument("output", type=str, help="The path to the output file. If the file does not exist, it will be created.")
    parser.add_argument("--target-language", "-t", type=str, help="The language that the SRT File is going to be translated to. (default: english)", default="english")
    parser.add_argument("--source-language", "-s", type=str, help="The language that the SRT File is being translated from. (default: auto)", default="auto")

    args = parser.parse_args()

srt_file_string = open(args.file, 'r').read()
subtitles = list(srt.parse(srt_file_string))
length = len(subtitles)

for i in range(length):
    content = html5lib.parse(subtitles[i].content)  
    parseContent(content, args.source, args.target)
    subtitles[i].content = html5lib.serialize(content)
    print ('\033[A                             \033[A')
    print(f'${(i/length):.2f}% completed.')
    
print ('\033[A                             \033[A')
print(f'100% completed. Writing...')

with open(args.output, encoding='utf-8', mode='w') as translated:
    translated.write(srt.compose(subtitles))