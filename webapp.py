from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory
import os


# 設定ファイルの値を取得する
load_dotenv()
DOWNLOAD_DIR_PATH = os.getenv('DATA_DIR_PATH')


app = Flask(__name__, static_folder=None)


def get_mimetype(ext):
    """
    拡張子からMIMEタイプを取得する
    """

    if '.mp4' == ext:
        return 'video/mp4'
    elif '.webm' == ext:
        return 'video/webm'
    else:
        return ''


def validate_param(param):
    """
    パラメーターを検査する
    """

    return param


# Routing
@app.route('/', methods=['GET'])
def root():
    """
    トップページを出力する
    """

    return render_template('root.html', title='Root')


@app.route('/start', methods=['POST'])
def start_command():
    """
    パラメーターを指定してコマンドを開始する
    """

    proc_id = request.form['param']
    # TODO
    return render_template('start.html', proc_id=proc_id)


@app.route('/download', methods=['GET'])
def download_form():
    """
    ダウンロードフォームを出力する
    """

    return render_template('download.html', title='Root')


@app.route('/download', methods=['POST'])
def download_file():
    """
    処理結果ファイルをダウンロードする
    """

    proc_id = request.form['proc_id']

    downloadFile = proc_id

    # TODO
    # return send_from_directory(
    #     DOWNLOAD_DIR_PATH,
    #     downloadFile,
    #     as_attachment=True,
    #     # attachment_filename=renamed_filename,
    #     mimetype=get_mimetype(os.path.splitext(downloadFile)[1])
    # )
    return downloadFile


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='localhost', port=3000)
