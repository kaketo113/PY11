# 0　ライブラリ・モジュールのインポート
# 必要な外部ライブラリとtkinterモジュールを読み込み

# 1　データ処理機能
# 1-1 ユーザー登録機能 (add_user関数)
#     ├─ 入力値の検証（バリデーション）
#     ├─ CSVファイルの保存先指定
#     ├─ データのCSVファイルへの書き込み
#     ├─ 登録結果の画面表示
#     └─ 入力フォームのクリア
#
# 1-2 データ読み込み機能 (open_file関数)
#     ├─ CSVファイルの選択
#     ├─ ファイル内容の読み込み
#     ├─ データ形式の検証
#     └─ 入力フォームへのデータ設定

# 2　サブウィンドウ（入力フォーム）の構築
# 2-1 ウィンドウ作成関数 (create_window関数)
# 2-2 サブウィンドウの生成と基本設定
# 2-3 タイトルバーの作成
# 2-4 入力フォームの構築
#     ├─ 氏名入力欄
#     ├─ 年齢入力欄
#     ├─ 性別選択欄
#     ├─ 住所入力欄
#     └─ 電話番号入力欄
# 2-5 操作ボタンの配置
#     ├─ 登録ボタン
#     ├─ ファイルを開くボタン
#     └─ 戻るボタン
# 2-6 結果表示欄の設置
# 2-7 モーダルウィンドウの設定

# 3　メインアプリケーション
# 3-1 グローバル変数の宣言
# 3-2 メインウィンドウの生成
# 3-3 アプリケーションタイトルの表示
# 3-4 メニューボタンの配置
# 3-5 終了ボタンの配置
# 3-6 ウィジェット変数の初期化
# 3-7 サブウィンドウ変数の初期化
# 3-8 アプリケーションの実行開始

#0 import
import ctypes               #C言語のDLLを呼び出すためのモジュール
import tkinter              #デスクトップアプリモジュール
from tkinter import ttk     #デスクトップアプリモジュール(ttk)
import csv                  #CSVファイル操作モジュール
from tkinter import messagebox #メッセージボックスモジュール
import os                   #OS操作モジュール
import tkinter.filedialog  #ファイルダイアログモジュール


# 1-1 ユーザー登録機能 (add_user関数)
def add_user():
    # 1-1-1 入力値の検証（バリデーション）
    if w_name.get()=="" or w_age.get()=="" or w_sex.get()=="" or w_address.get()=="" or w_tel.get()=="": #isdigit()は数字かどうかを判定する
        messagebox.showerror("入力エラー", "項目を正しく入力してください。")
        return
    elif not w_age.get().isdigit():
        messagebox.showerror("入力エラー", "年齢は数字で入力してください。")
        return
    elif not w_tel.get().isdigit():
        messagebox.showerror("入力エラー", "電話番号は数字で入力してください。")
        return

    # 1-1-2 CSVファイルの保存先指定
    # 初期ディレクトリを生成する
    fTyp = [("","*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    # initialDir: は初期ディレクトリ"/"は"C:￥"になる
    file = tkinter.filedialog.asksaveasfilename(filetype = fTyp,initialdir = iDir)
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        csv_txt =[
            w_name.get(),
            w_age.get(),
            w_sex.get(),
            w_address.get(),
            w_tel.get()
        ]

    # 1-1-3 データのCSVファイルへの書き込み
        writer.writerow(csv_txt) 
        mes ="登録しました"

    # 1-1-4 登録結果の画面表示
        w_res.set(mes)

    # 1-1-5 入力フォームのクリア
        w_name.set('')
        w_age.set('')
        w_sex.set('')
        w_address.set('')
        w_tel.set('')


# 1-2 データ読み込み機能 (open_file関数)
def open_file():
    # 1-2-1 CSVファイルの選択
    fTyp = [("","*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes= fTyp,initialdir= iDir)
    # 1-2-2 ファイル内容の読み込み
    with open(file, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

        # dataが空の場合
        if len(data) == 0:
            messagebox.showerror("エラー", "ファイルが空です。")
            return
        # 最後の行のデータを取得
        ins_data = data[-1]

    # 1-2-3 データ形式の検証
        if len(ins_data) < 5:
            messagebox.showerror("エラー", "ファイルのデータ形式が不正です。")
            return
        
    # 1-2-4 入力フォームへのデータ設定
        w_name.set(ins_data[0])
        w_age.set(ins_data[1])
        w_sex.set(ins_data[2])
        w_address.set(ins_data[3])
        w_tel.set(ins_data[4])
    w_res.set("データを読み込みました")

# 2-1 ウィンドウ作成関数 (create_window関数)
def create_window():
    
# 2-2 サブウィンドウの生成と基本設定
    global sub_window
 
    #子画面インスタンスの生成
    sub_window = tkinter.Toplevel(root)
    sub_window.title("ユーザー登録フォーム")
    sub_window.geometry("900x700")
    sub_window.configure(bg='#f0f0f0')
    sub_window.resizable(False, False)
 
# 2-3 タイトルバーの作成
    # メインタイトル
    title_frame = tkinter.Frame(sub_window, bg='#2c3e50', height=80)
    title_frame.pack(fill='x', pady=(0, 20))
    title_frame.pack_propagate(False)
    
    l_s = tkinter.Label(
        title_frame,
        text="👤 ユーザー登録フォーム",
        bg='#2c3e50',
        fg='white',
        font=("メイリオ", "24", "bold")
    )
    l_s.pack(expand=True)
 
# 2-4 入力フォームの構築
    # 入力フォームのメインフレーム
    form_frame = tkinter.Frame(sub_window, bg='#f0f0f0')
    form_frame.pack(fill='both', expand=True, padx=40, pady=20)

# 2-4-1 氏名入力欄
    global w_name
    # 氏名入力セクション
    name_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    name_frame.pack(fill='x', pady=15)
    
    #氏名の入力欄(タイトル)
    l_name = tkinter.Label(
        name_frame,
        text="📝 氏名",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_name.pack(side='left', padx=(0, 20))

    #氏名の入力欄
    entry_name = tkinter.Entry(
        name_frame,
        textvariable=w_name,
        width=25,
        font=("メイリオ", 12),
        bg='white',
        fg='#2c3e50',
        relief='solid',
        bd=2,
        justify='left'
    )
    entry_name.pack(side='left')
 
# 2-4-2 年齢入力欄
    global w_age
    
    # 年齢入力セクション
    age_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    age_frame.pack(fill='x', pady=15)
 
    #年齢の入力欄(タイトル)
    l_age = tkinter.Label(
        age_frame,
        text="🎂 年齢",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_age.pack(side='left', padx=(0, 20))
 
    #年齢の入力欄
    entry_age = tkinter.Entry(
        age_frame,
        textvariable=w_age,
        width=8,
        font=("メイリオ", 12),
        bg='white',
        fg='#2c3e50',
        relief='solid',
        bd=2,
        justify='center'
    )
    entry_age.pack(side='left', padx=(0, 10))
    
    #年齢の入力欄(単位)
    l_age_unit = tkinter.Label(
        age_frame,
        text="歳",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_age_unit.pack(side='left')
    
# 2-4-3 性別選択欄
    global w_sex
    
    # 性別入力セクション
    sex_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    sex_frame.pack(fill='x', pady=15)

    #性別の選択欄（タイトル）
    l_sex = tkinter.Label(
        sex_frame,
        text="⚥ 性別",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_sex.pack(side='left', padx=(0, 20))
 
    #性別の選択欄
    options = ["男性", "女性", "その他"]
    combobox = ttk.Combobox(
        sex_frame,
        width=15,
        textvariable=w_sex,
        values=options,
        state="readonly",
        font=("メイリオ", "12"),
    )
    combobox.pack(side='left')
 
# 2-4-4 住所入力欄
    global w_address
    
    # 住所入力セクション
    address_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    address_frame.pack(fill='x', pady=15)

    #住所の入力欄（タイトル）
    l_address = tkinter.Label(
        address_frame,
        text="🏠 住所",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_address.pack(side='left', padx=(0, 20))

    #住所入力欄
    entry_address = tkinter.Entry(
        address_frame,
        textvariable=w_address,
        width=30,
        font=("メイリオ", 12),
        bg='white',
        fg='#2c3e50',
        relief='solid',
        bd=2,
        justify='left'
    )
    entry_address.pack(side='left')

# 2-4-5 電話番号入力欄
    global w_tel
    
    # 電話番号入力セクション
    tel_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    tel_frame.pack(fill='x', pady=15)

    #電話番号の入力欄（タイトル）
    l_tel = tkinter.Label(
        tel_frame,
        text="📞 電話番号",
        bg='#f0f0f0',
        fg='#2c3e50',
        font=("メイリオ", "14", "bold")
    )
    l_tel.pack(side='left', padx=(0, 20))

    #電話番号の入力欄
    entry_tel = tkinter.Entry(
        tel_frame,
        textvariable=w_tel,
        width=20,
        font=("メイリオ", 12),
        bg='white',
        fg='#2c3e50',
        relief='solid',
        bd=2,
        justify='left'
    )
    entry_tel.pack(side='left', padx=(0, 10))
    
    #ハイフンは不要テキストの追加
    l_tel_hyphen = tkinter.Label(
        tel_frame,
        text="(ハイフン不要)",
        bg='#f0f0f0',
        fg='#7f8c8d',
        font=("メイリオ", "10")
    )
    l_tel_hyphen.pack(side='left')
 
# 2-5 操作ボタンの配置
    # ボタンフレーム
    button_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    button_frame.pack(fill='x', pady=30)
    
    b_registry = tkinter.Button(
        button_frame,
        text="✅ 登録",
        width=15,
        height=2,
        font=("メイリオ", "16", "bold"),
        bg='#27ae60',
        fg='white',
        relief='flat',
        bd=0,
        command=add_user,
        cursor='hand2'
    )
    b_registry.pack(side='left', padx=(0, 20))
 
# 2-6 結果表示欄の設置
    # 結果表示フレーム
    result_frame = tkinter.Frame(form_frame, bg='#f0f0f0')
    result_frame.pack(fill='x', pady=20)
    
    entry_Result = tkinter.Entry(
        result_frame,
        textvariable=w_res,
        width=40,
        font=("メイリオ", 14),
        bg='#ecf0f1',
        fg='#2c3e50',
        relief='solid',
        bd=2,
        justify='center',
        state='readonly'
    )
    entry_Result.pack()
    
# 2-7 ファイルを開くボタンの追加
    opend_file = tkinter.Button(
        button_frame,
        text="📁 ファイルを開く",
        width=15,
        height=2,
        font=("メイリオ", "14", "bold"),
        bg='#3498db',
        fg='white',
        relief='flat',
        bd=0,
        command=open_file,
        cursor='hand2'
    )
    opend_file.pack(side='left', padx=(0, 20))
    
# 2-8 戻るボタンの追加
    b_exit = tkinter.Button(
        button_frame,
        text="❌ 戻る",
        width=10,
        height=2,
        font=("メイリオ", "14", "bold"),
        bg='#e74c3c',
        fg='white',
        relief='flat',
        bd=0,
        command=sub_window.destroy,
        cursor='hand2'
    )
    b_exit.pack(side='right')

# 2-9 モーダルウィンドウの設定
    sub_window.grab_set()
 
 
# 3-1 グローバル変数の宣言
if __name__ == "__main__":
    #ウィジェット変数をGlobal化する
    
    #氏名
    global w_name

    #年齢
    global w_age

    #性別
    global w_sex

    #住所
    global w_address

    #電話番号
    global w_tel

    #結果表示
    global w_res

    #↓のコードは、Windows環境で Tkinter GUI を使う際に、
    #DPI（ディスプレイの解像度）スケーリングの問題を回避するための設定です。
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
 
# 3-2 メインウィンドウの生成
    #main-window
    root = tkinter.Tk()
    root.title("ユーザー管理システム")
    root.geometry("900x700")
    root.configure(bg='#f0f0f0')
    root.resizable(False, False)
   
# 3-3 アプリケーションタイトルの表示
    # メインタイトルフレーム
    main_title_frame = tkinter.Frame(root, bg='#2c3e50', height=100)
    main_title_frame.pack(fill='x', pady=(0, 30))
    main_title_frame.pack_propagate(False)
    
    l = tkinter.Label(
        main_title_frame,
        text="🏠 ユーザー管理システム",
        bg='#2c3e50',
        fg='white',
        font=("メイリオ", "28", "bold")
    )
    l.pack(expand=True)
   
# 3-4 メニューボタンの配置
    # メインコンテンツフレーム
    main_content_frame = tkinter.Frame(root, bg='#f0f0f0')
    main_content_frame.pack(fill='both', expand=True, padx=50, pady=20)
    
    # 説明ラベル
    desc_label = tkinter.Label(
        main_content_frame,
        text="ユーザー情報を登録・管理するシステムです",
        bg='#f0f0f0',
        fg='#7f8c8d',
        font=("メイリオ", "14")
    )
    desc_label.pack(pady=(0, 40))
    
    b1 = tkinter.Button(
        main_content_frame,
        text="📝 ユーザー登録フォーム",
        width=25,
        height=3,
        font=("メイリオ", "18", "bold"),
        bg='#27ae60',
        fg='white',
        relief='flat',
        bd=0,
        command=create_window,
        cursor='hand2'
    )
    b1.pack(pady=20)

# 3-5 終了ボタンの配置
    # フッターフレーム
    footer_frame = tkinter.Frame(root, bg='#f0f0f0')
    footer_frame.pack(fill='x', side='bottom', pady=20)
    
    b4 = tkinter.Button(
        footer_frame,
        text="❌ 終了",
        width=10,
        height=2,
        font=("メイリオ", "14", "bold"),
        bg='#e74c3c',
        fg='white',
        relief='flat',
        bd=0,
        command=root.quit,
        cursor='hand2'
    )
    b4.pack(side='right', padx=50)

 
# 3-6 ウィジェット変数の初期化
    #氏名
    w_name = tkinter.StringVar()
    w_name.set('')

    #年齢
    w_age = tkinter.StringVar()
    w_age.set('')

    #性別
    w_sex = tkinter.StringVar()
    w_sex.set('')

    #住所
    w_address = tkinter.StringVar()
    w_address.set('')

    #電話番号
    w_tel = tkinter.StringVar()
    w_tel.set('')

    #結果表示
    w_res = tkinter.StringVar()
    w_res.set('')
 
# 3-7 サブウィンドウ変数の初期化
    sub_win = None
 
# 3-8 アプリケーションの実行開始
    root.mainloop()