#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'おはようございます。元気ですか？'
    # to_translate = 'Bonjour comment allez vous?'
    print(translate(to_translate))
    print(translate(to_translate, 'ja'))
    print(translate(to_translate, 'zh-TW'))


if __name__ == '__main__':
    main()
