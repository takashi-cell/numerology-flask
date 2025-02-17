from subprocess import Popen
import time

# Flask アプリの起動
processes = []

try:
    # numerology_flask (5001) の起動
    processes.append(Popen(["python", "numerology_flask/app.py"]))

    # ton-shin-chi (5002) の起動
    processes.append(Popen(["python", "ton-shin-chi/app.py"]))

    # メインアプリ (5000) の起動
    time.sleep(2)  # 他のアプリが先に起動するのを待つ
    processes.append(Popen(["python", "main_app/app.py"]))

    # 各アプリを起動したままにする
    for p in processes:
        p.wait()

except KeyboardInterrupt:
    # 強制終了時に全プロセスを停止
    for p in processes:
        p.terminate()
