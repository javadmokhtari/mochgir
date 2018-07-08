[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)

# Proof Of Concept
1. [Introduction](https://github.com/javadmokhtari/mochgir/blob/master/README.md#1-introduction)
2. [Installation](https://github.com/javadmokhtari/mochgir#2-installation)

    2.1 [Install Using Pip](https://github.com/javadmokhtari/mochgir#21-using-pip)
    
    2.2 [Install From Source Code](https://github.com/javadmokhtari/mochgir#22-install-from-source)
    
3. [Examples](https://github.com/javadmokhtari/mochgir#3-examples)

    3.1 [Translating A String](https://github.com/javadmokhtari/mochgir#31-translating-a-string)
    
    3.2 [Translating A List of Strings](https://github.com/javadmokhtari/mochgir#32-translating-list-of-strings)
    
    3.3 [Translating A Document](https://github.com/javadmokhtari/mochgir#33-translating-a-document)
    
    3.4 [Analyzing A String](https://github.com/javadmokhtari/mochgir#34-analyzing-a-string)
    
    3.5 [Analyzing A List of Strings](https://github.com/javadmokhtari/mochgir#35-analyzing-a-list-of-strings)
    
    3.6 [Analyzing A Document](https://github.com/javadmokhtari/mochgir#36-analyzing-a-document)
    
    3.7 [Exporting Result](https://github.com/javadmokhtari/mochgir/blob/master/README.md#37-exporting-result)
    
4. [Requirements](https://github.com/javadmokhtari/mochgir#4-requirements)
5. [License](https://github.com/javadmokhtari/mochgir#5-licence)
5. [Credit](https://github.com/javadmokhtari/mochgir#6-credit)

![Image of Yaktocat](https://github.com/javadmokhtari/mochgir/blob/master/workflow.png)

# 1. Introduction
Mochgir is a small-tool for detecting plagiarism. It's lightweight and written with Python 3. You can analyze a document and detect possible scientific thiefs. Despite of it's usage in scientific detection, it can be used as a persian-to-english translator.

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
>>> "Hey, I hope you 're okay , buddy."
```
   ### 3.2 Translating List of Strings
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

   ### 3.4 Analyzing A String
   ```python
>>> from mochgir import Translate
>>> from mochgir import Analyze
>>> text = 'سلام، امیدوارم حالت خوب باشه رفیق'
>>> trasnlated_text = Translate.translate(text)
>>> result = Analyze.analyze(translated_text)
```

   ### 3.5 Analyzing A List of Strings
   ```python
>>> from mochgir import Translate
>>> from mochgir import Analyze
>>> text_list = ['امروز کلاس رفتی؟', 'چرا یهو درس ها سخت شد؟', 'می تونم یک ساعت دیگه با شما تماس بگیرم؟']
>>> translated_list = Translate.translate_list(text_list)
>>> result = Analyze.analyze_list(translated_list)
```

   ### 3.6 Analyzing A Document
   ```python
>>> from mochgir import Translate
>>> from mochgir import Analyze
>>> document_path = 'C:\ppp.docx'
>>> translated_document = Translate.translate_document(document_path)
>>> result = Analyze.analyze_list(translated_document)
```

   ### 3.7 Exporting Result
   Right now, text file (.txt) is the only available format for exporting analysis results. you can use `export_text()`, `export_list()` and `export_document()` methods for different situations. Support for other formats like PDF will be added soon.
   
   NOTE: you need to pass export path to the above methods.
# 4. Requirements
*requests>=2.19.1*

*python-docx>=0.2.4*

*google>=2.0.1*

*reportlab>=3.4.0*

# 5. Licence
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

# 6. Credit
Created by Javad M. Koushyar. This is an educational purpose project, so there is no warranty for it. Thank You!
