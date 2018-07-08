import json
import string
from time import sleep

import requests
from docx import Document
from docx.opc import exceptions
from googlesearch import search
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from conf.consts import *


# TODO: Update README.MD in github, and replace it with current readme in project folder
# TODO: Create installable package with  pip
# TODO: Mochgir only works with Python 3.x
# TODO: Writing some good example, for each part of package
# TODO: Analyze.export_to_pdf(Analyze.analyze('Mehrad Hidden', 3)) produces 15 results, why?
# TODO: Create a diagram / schema for whole package
class DocumentHandler(object):
    def __init__(self, file_name):
        """  
        :param file_name: Address of document 
        :type file_name: str
                
        :except exceptions.PackageNotFoundError: cannot find a file with file_name path
        
        :return document object
        """
        self.file_name = file_name
        try:
            self.document_object = Document(self.file_name)
        except exceptions.PackageNotFoundError:
            raise Exception(NOT_FOUND_ERROR)

    def extract_text(self):
        """
        :return: a list containing text of each paragraph 
        """
        return [para.text for para in self.document_object.paragraphs]


class Translate(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _extract_printable(text):
        """
        :param text: messy text that may contain extra spaces and non-printable characters
        :type text: str
        
        :return: refined text
        """
        return ''.join(list(filter(lambda x: x in set(string.printable), text))).lstrip(' ')

    @staticmethod
    def _retry_request(request_function, text, retry):
        """
        :param request_function: 
        :type request_function: request function object
        
        :param text: 
        :type text: str
        
        :param retry: number of possible retries
        :type retry: int
        
        :return: None
        """
        if retry <= 0:
            raise Exception(RETRY_ERROR)
        else:
            retry -= 1
            sleep(SLEEP_TIME)
            request_function(text, retry)

    @staticmethod
    def translate(text, retry=MAX_RETRY, lang=DEFAULT_LANG):
        """
        :param text: text to translate
        :type text: str
        
        :param retry: number of possible retries
        :type retry: int
        
        :param lang: language to do translation (e.g. fa2en, en2fa)
        :type lang: str
        
        :return: translated text (str)
        """
        payload = REQUEST_PAYLOAD
        payload['params'][1] = text
        payload['params'][2] = lang

        def __extract_text(messy_text):
            """
            :param messy_text: response of successful request to translation API
            :type messy_text: dict
            
            :return: translated text (str)
            """
            try:
                output = messy_text['result']['tr']['base'][0][1]
            except KeyError:
                raise Exception(KEY_ERROR)

            return output

        def __check_status(request_object):
            """
            :param request_object: 
            :type request_object: request.get
            
            :return: None
            """
            if request_object.status_code != 200:
                raise Exception(SERVER_ERROR.format(request_object.status_code))

        try:
            translate_request = requests.post(API_URL, data=json.dumps(payload), headers=REQUEST_HEADERS)
            __check_status(translate_request)
            translate_response = json.loads(translate_request.content.decode())
            translated_text = __extract_text(translate_response)

        except requests.exceptions.ConnectionError:
            Translate._retry_request(Translate.translate, text, retry)
            raise Exception(CONNECTION_ERROR)

        except json.decoder.JSONDecodeError:
            Translate._retry_request(Translate.translate, text, retry)
            raise Exception(JSON_DECODE_ERROR)

        response = Translate._extract_printable(translated_text)

        return response

    @staticmethod
    def translate_list(text_list, retry=MAX_RETRY, lang=DEFAULT_LANG):
        """
        :param text_list: list of texts
        :type text_list: list
        
        :param retry: number of possible retries
        :type retry: int
        
        :param lang: language to do translation (e.g. fa2en, en2fa)
        :type lang: str
        
        :return: list of translated text(s)
        """
        text_list = list(filter(None, text_list))
        return list(
            map(lambda text: Translate.translate(text, retry, lang),
                text_list)
        )

    @staticmethod
    def translate_document(document_path, retry=MAX_RETRY, lang=DEFAULT_LANG):
        """
        
        :param document_path: Address of document
        :type document_path: str
        
        :param retry: number of possible retries
        :type retry: int
        
        :param lang: language to do translation (e.g. fa2en, en2fa)
        :type lang: str
        
        :return: list containing translated text of document
        """
        document_object = DocumentHandler(document_path)
        text_list = document_object.extract_text()
        translated_list = Translate.translate_list(text_list, retry, lang)

        return translated_list


class Analyze(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def find_related_sites(text, count=MAX_SEARCH):
        """
        :param text: text to search with search engine (google)
        :type text: str
        
        :param count: number of expected search results (if available)
        :type count: int
        
        :return: list containing search results
        """
        # TODO: Remove blocked sites from the list
        search_result = search(text, stop=count)

        return list(search_result)

    @staticmethod
    def check_text_in_site(text, site):
        """
        :param text: text to search in site content
        :type text: str
        
        :param site: URL address exported from search engine results
        :type site: str
        
        :return: True if text is in site content, else False
        """
        try:
            request_to_site = requests.get(site)
            site_text = request_to_site.text
        except Exception:
            return False
        return text in site_text

    @staticmethod
    def analyze(text, count=MAX_SEARCH):
        """
        :param text: text to analyze
        :type text: str
        
        :param count: number of expected search results (if available)
        :type count: int
        
        :return: dictionary contains analyze result. key is text and urls are values.
        """
        sites = Analyze.find_related_sites(text, count)

        url_list = []
        result_dict = {}

        for site in sites:
            if Analyze.check_text_in_site(text, site):
                url_list.append(site)
            result_dict[text] = url_list

        return result_dict

    @staticmethod
    def analyze_list(text_list, count=MAX_SEARCH):
        """
        :param text_list: list of text(s) to analyze
        :type text_list: list
        
        :param count: number of expected search results for each text in text_list (if available)
        :type count: int
        
        :return: list of dictionaries that represent analyze result for each text in text_list
        """
        result_list = []
        for text in text_list:
            try:
                result_list.append(Analyze.analyze(text, count))
            except Exception:
                pass

        return result_list

    @staticmethod
    def export(analyze_result, path=DEFAULT_PATH):
        """
        :param analyze_result: result returned from analyze or analyze_list or analyze_document methods
        :type analyze_result: list / dict
        
        :param path: path to save results
        :type path: str
        
        :return: None
        """

        create_folders()
        with open(path, 'w+', encoding="utf-8") as fh:
            if type(analyze_result) is list:
                for result in [analyze_result]:
                    fh.write(json.dumps(result, ensure_ascii=False))
            else:
                fh.write(json.dumps(analyze_result, ensure_ascii=False))

    @staticmethod
    def export_to_pdf(analyze_result, path=DEFAULT_PATH_PDF):
        """
        :param analyze_result: result returned from analyze or analyze_list or analyze_document methods
        :type analyze_result: list / dict
        
        :param path: path to save results
        :type path: str
        
        :return: None
        """

        create_folders()
        # pdfmetrics.registerFont(TTFont('tahoma', FONT_PATH))

        doc = SimpleDocTemplate(path, pagesize=letter,
                                rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

        style_sheet = getSampleStyleSheet()
        style_sheet.add(ParagraphStyle(
            name='ParaStyle',
            leading=12,
            fontSize=12,
        ))

        style_sheet.add(ParagraphStyle(
            name='IntroStyle',
            leading=12,
            fontSize=8
        ))

        report = []

        report.append(Paragraph('<font color="green">{content}</font>'.format(
            content=PDF_INTRO.format(str(datetime.now()), APP_VERSION)),
            style=style_sheet['IntroStyle']))

        report.append(Spacer(1, 12))

        if type(analyze_result) is list:
            for result in analyze_result:
                for key in result.keys():

                    report.append(Paragraph('<font color="black">{content}</font>'.format(
                        content=key + ' ({count})'.format(count=len(result[key]))),
                        style=style_sheet['ParaStyle']))

                    for link in result[key]:
                        report.append(Paragraph('<font color="blue">{content}</font>'.format(
                            content=link),
                            style=style_sheet['ParaStyle']))

                    report.append(Spacer(1, 12))
        else:
            for key in analyze_result.keys():

                report.append(Paragraph('<font color="black">{content}</font>'.format(
                    content=key + ' ({count})'.format(count=len(analyze_result[key]))),
                    style=style_sheet['ParaStyle']))

                for link in analyze_result[key]:
                    report.append(Paragraph('<font color="blue">{content}</font>'.format(
                        content=link),
                        style=style_sheet['ParaStyle']))

                report.append(Spacer(1, 12))

        doc.build(report)


# Analyze.export_to_pdf(Analyze.analyze('javad'))
