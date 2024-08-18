# SRT Automatic Translator Tool

This script translates the text inside SRT files from a language to another.

## Usage

```bash
$ pip install -r requirements # To install dependencies

$ usage: python srt_translator.py [-h] [--target-language TARGET_LANGUAGE] [--source-language SOURCE_LANGUAGE] file output
```

```bash
positional arguments:
  file                  The path to the SRT File
  output                The path to the output file. If the file does not exist, it will be created.

options:
  -h, --help            show this help message and exit
  --target-language TARGET_LANGUAGE, -t TARGET_LANGUAGE
                        The language that the SRT File is going to be translated to. (default: english)
  --source-language SOURCE_LANGUAGE, -s SOURCE_LANGUAGE
                        The language that the SRT File is being translated from. (default: auto)
```

## Under the hood

This scripts parses the SRT subtitles using [srt](https://pypi.org/project/srt/) library. The content of the subtitles is then parsed using [html5lib](https://github.com/html5lib/html5lib-python) and separate the text from the SRT tags. After this, the content is translated using [deep_translator](https://github.com/prataffel/deep_translator) with `GoogleTranslator` option.