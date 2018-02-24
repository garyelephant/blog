# 各种小技巧

## markdown to word

```
# http://bob.yexley.net/generate-a-word-document-from-markdown-on-os-x/
$ brew install pandoc
$ pandoc -o output.docx -f markdown -t docx markdown-file.md
```