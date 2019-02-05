# jazh-char-forms
日文汉字、简体中文、繁体中文字形对照库 | Database for comparison between Japanese Kanji and Chinese (simplied and traditional) characters

曾经，日文、繁体中文文字被发布到百度贴吧后，其中不属于 GB2312-80 字符集（全是简体中文）的字会被自动转码成 GB2312-80 中的另一个字。该 repo 的目的是检测一段本应是日文或繁体字的文字是否被转码，并尽量纠正。不过鉴于日文、繁体中文、简体中文之间的转换都不是一对一关系，自动纠正不是简单编程便能做到的，仍需人工甄别。

## 缩写
| 缩写 | 字形 |
|-|-|
| zhs | 简体中文 |
| zht | 繁体中文 |
| ja | 日文汉字 |

## 字符集
`char_forms`文件夹。

| 字库 | 已有字形 | 说明 |
|-|-|-|
|  `GB2312-80` | zhs,zht | 百度贴吧曾使用的编码，只有简体中文。共 6763 字。 |
| 日本語常用漢字（ `jouyoukanji`） | ja,zhs | 日语常用汉字，包括新字体（`shinjitai`，2136 字）、旧字体（`kyuujitai`，363 字）。 |

## 字形对照表
`dict` 文件夹。csv 格式。

## 脚本
`scripts`文件夹。

`compare.py`

用途：生成 csv 格式的字符对照表。需提供两份文件，第一份是原来的字符，第二份是转码后的字符。两份文件都每行一个字，并且相对应的字符在两份文件中的位置相同。

用法：
```
python3 compare.py original_forms.txt converted_forms.txt
```

`detector.py`

用途：检测输入文件中是否有可能被转码的字符，并给出字符位置。目前仅检测日文新字体。

用法：
```
python3 detector.py test.txt
```
