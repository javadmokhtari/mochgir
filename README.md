# Proof Of Concept
1. [Introduction](https://github.com/javadmokhtari/mochgir/blob/master/README.md#1-introduction)
2. [Installation](http://www.google.com)

    2.1 [Install Using Pip](http://www.google.com)
    
    2.2 [Install From Source Code](http://www.google.com)
    
3. [Examples](http://www.google.com)

    3.1 [Translating A String](http://www.google.com)
    
    3.2 [Translating A List of Texts](http://www.google.com)
    
    3.3 [Translating A Document](http://www.google.com)
    
    3.4 [Analyzing A Text](http://www.google.com)
    
    3.5 [Analyzing A List of Texts](http://www.google.com)
    
    3.6 [Analyzing A Document](http://www.google.com)
    
4. [Requirements](http://www.google.com)
5. [Credit](http://www.google.com)

# 1. Introduction
Mochgir is a small-tool for detecting plagiarism. It's lightweight and written with Python 3. You can analyze a document and detect possible sceintific thiefs.

# 2. Installation
   ### 2.1 Using Pip
   you can install mochgir on Windows, Linux and MAC OS using pip:
   `pip install mochgir`
   ### 2.2 Install From Source
   we recommend you to install mochgir with pip, but for any reason you may want to install mochgir from source code. Here is the instruction:
   
   &nbsp;&nbsp;**a**) Download This repository
   
   &nbsp;&nbsp;**b**) Uncompress it wherever you want
   
   &nbsp;&nbsp;**c**) Open Terminal / Command Line and go to uncompressed directory
   
   &nbsp;&nbsp;**d**) Run this command: `python setup.py install`
   
   Note: you must use python 3 to install mochgir.
   
# 3. Examples
   ### 3.1 Translating A String
   ```python
>>> from mochgir import Translate


>>> text = 'سلام، امیدوارم حالت خوب باشه رفیق'
>>> Translate.translate(text)
>>> 'Hey, I hope you 're okay , buddy.'
```
   ### 3.2 Translating List of Texts
   ```python
>>> from mochgir import Translate

>>> text_list = ['امروز کلاس رفتی؟', 'چرا یهو درس ها سخت شد؟', 'می تونم یک ساعت دیگه با شما تماس بگیرم؟']
>>> Translate.translate_list(text_list)
>>> ['Did you go to class today?', 'Why are the lessons suddenly difficult?', 'Can I call you in an hour?']
```

   ### 3.3 Translating A Document
   ```python
>>> from mochgir import Translate


>>> document_path = 'C:\ppp.docx'
>>> Translate.translate_document(document_path)
>>> 'In the name of god A minimum spanning tree of a connected graph ....'

```
