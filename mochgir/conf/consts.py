from datetime import datetime
import os


APP_VERSION = '0.5'
API_URL = "http://targoman.ir/API/"

REQUEST_HEADERS = {
    "Host": "targoman.ir", "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Origin": "http://targoman.ir", "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Content-Type": "application/json",
    "Referer": "http://targoman.ir/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8"
}

REQUEST_PAYLOAD = {
    "jsonrpc": "2.0",
    "method": "Targoman::translate", "id": 1,
    "params": ["sSTargomanWUI", '', '', "127.0.0.10", "NMT", "true", "true", "true", "null"]
}

# error messages
NOT_FOUND_ERROR = 'File Not Found'
CONNECTION_ERROR = 'You have connection problems, please try again later.'
JSON_DECODE_ERROR = 'Cannot decode json response.'
KEY_ERROR = 'Key Error'
RETRY_ERROR = 'Retry limit exceeded.'
SERVER_ERROR = 'The server did not respond correctly. Status Code: {}'

MAX_RETRY = 2
DEFAULT_LANG = "fa2en"
SLEEP_TIME = 1
MAX_SEARCH = 10

CURRENT_TIME = str(datetime.now()).split()
CURRENT_TIME = ''.join(CURRENT_TIME[0].split('-')) + ''.join(CURRENT_TIME[1].split('.')[0].split(':'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_FOLDER = "export"

DEFAULT_PATH = os.path.join(BASE_DIR, EXPORT_FOLDER, "txt", "{}.txt".format(CURRENT_TIME))
DEFAULT_PATH_PDF = os.path.join(BASE_DIR, EXPORT_FOLDER, "pdf", "{}.pdf".format(CURRENT_TIME))


def create_folders():
    try:
        os.makedirs(os.path.join(BASE_DIR, EXPORT_FOLDER, "txt"))
        os.makedirs(os.path.join(BASE_DIR, EXPORT_FOLDER, "pdf"))
    except FileExistsError:
        pass

FONT_PATH = os.path.join(BASE_DIR, 'conf\\font\\Tahoma.ttf')

PDF_INTRO = "Created at {} with Mochgir {}"
