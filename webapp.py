from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, redirect, render_template, request, send_from_directory, url_for
import os
import werkzeug


# 設定ファイルの値を取得する
load_dotenv()

try:
    DOWNLOAD_DIR_PATH = os.getenv('DATA_DIR_PATH')
except:
    DOWNLOAD_DIR_PATH = 'data'

try:
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE'))
except:
    MAX_FILE_SIZE = 1024 * 1024


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

    # ファイルアップロード用
    if 'datafile' in request.files:
        file = request.files['datafile']
        if '' != file.filename:
            saveFileName = datetime.now().strftime("%Y%m%d%H%M%S%f") + \
                os.path.splitext(
                    werkzeug.utils.secure_filename(file.filename))[1]
            file.save(os.path.join(DOWNLOAD_DIR_PATH, saveFileName))
    #

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
    return make_response(jsonify({'result': downloadFile}))

# 例外処理


# ファイルアップロード用
@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    return 'The file is too large.'


# TODO 404


# main
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='localhost', port=3000)
