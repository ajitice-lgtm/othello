import streamlit as st
import numpy as np

# =================================================================
# 定数と初期設定
# =================================================================

# ゲームの状態定数
EMPTY = 0
BLACK = 1
WHITE = 2
BOARD_SIZE = 8
DIRECTIONS = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

# Streamlitのセッションステートでゲームの状態を管理
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    st.session_state.current_player = BLACK
    st.session_state.is_active = True
    st.session_state.pass_status = None
    
    # 初期配置
    st.session_state.board[3, 3] = WHITE
    st.session_state.board[3, 4] = BLACK
    st.session_state.board[4, 3] = BLACK
    st.session_state.board[4, 4] = WHITE

# =================================================================
# ゲームロジック (Python)
# =================================================================

def get_opponent(player):
    """相手のプレイヤーの色を取得"""
    return WHITE if player == BLACK else BLACK

def is_within_bounds(r, c):
    """座標が盤面内かチェック"""
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def check_direction_for_flips(r, c, dr, dc, player, board):
    """特定の方向でひっくり返せる駒をチェック"""
    opponent = get_opponent(player)
    flipped_pieces = []
    r_curr, c_curr = r + dr, c + dc

    while is_within_bounds(r_curr, c_curr):
        piece = board[r_curr, c_curr]
        if piece == opponent:
            flipped_pieces.append((r_curr, c_curr))
        elif piece == player:
            return flipped_pieces # 自分の駒で挟めた
        else: # EMPTY
            return [] # 間に自分の駒がない
        
        r_curr += dr
        c_curr += dc
    
    return []

def get_valid_flips(r, c, player, board):
    """指定したマスに打った場合にひっくり返せる全ての駒のリストを取得"""
    if board[r, c] != EMPTY:
        return []
    
    total_flips = []
    for dr, dc in DIRECTIONS:
        flips_in_direction = check_direction_for_flips(r, c, dr, dc, player, board)
        total_flips.extend(flips_in_direction)
        
    return total_flips

def get_all_valid_moves(player, board):
    """現在のプレイヤーが打てる全ての有効なマスをリストアップ"""
    valid_moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if get_valid_flips(r, c, player, board):
                valid_moves.append((r, c))
    return valid_moves

def make_move(r, c):
    """駒を打ち、ひっくり返し、プレイヤーを交代する処理"""
    if not st.session_state.is_active:
        return

    player = st.session_state.current_player
    flips = get_valid_flips(r, c, player, st.session_state.board)

    if not flips:
        # この警告は、Streamlitの再実行を伴うため、ボタンのクリックハンドラ内で
        # st.warningを呼び出すとエラーの原因となる可能性があります。
        # 今回はエラー回避のため、無効な手の場合は何もしないようにします。
        return

    # 駒を打ち、ひっくり返す
    new_board = st.session_state.board.copy()
    new_board[r, c] = player
    for flip_r, flip_c in flips:
        new_board[flip_r, flip_c] = player
    st.session_state.board = new_board
    
    # プレイヤーを交代し、パス判定
    switch_player()

def switch_player():
    """プレイヤーを交代し、パス・終了判定を行う"""
    current_player = st.session_state.current_player
    next_player = get_opponent(current_player)

    # 1. 次のプレイヤーが打てるか？
    if get_all_valid_moves(next_player, st.session_state.board):
        st.session_state.current_player = next_player
        st.session_state.pass_status = None
        return

    # 2. 次のプレイヤーが打てない場合、現在のプレイヤーに戻って打てるか？ (パス)
    elif get_all_valid_moves(current_player, st.session_state.board):
        st.session_state.current_player = current_player # パスして手番が戻る
        st.session_state.pass_status = next_player
    
    # 3. 両方打てない場合、ゲーム終了
    else:
        st.session_state.is_active = False
        st.session_state.pass_status = None

def get_scores(board):
    """現在のスコアを計算"""
    score = {
        BLACK: np.sum(board == BLACK),
        WHITE: np.sum(board == WHITE)
    }
    return score

def reset_game():
    """ゲームの状態をリセット"""
    st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    st.session_state.current_player = BLACK
    st.session_state.is_active = True
    st.session_state.pass_status = None
    
    st.session_state.board[3, 3] = WHITE
    st.session_state.board[3, 4] = BLACK
    st.session_state.board[4, 3] = BLACK
    st.session_state.board[4, 4] = WHITE

# =================================================================
# Streamlit UI (表示)
# =================================================================

st.set_page_config(page_title="オセロ (リバーシ)", layout="centered")

st.title("簡易オセロ (リバーシ) アプリ")

board = st.session_state.board
current_player = st.session_state.current_player
scores = get_scores(board)

# ----------------- ステータス表示 -----------------

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown(f"**黒** :black_circle: {scores[BLACK]} 駒")
with col3:
    st.markdown(f"**白** :white_circle: {scores[WHITE]} 駒")

with col2:
    if st.session_state.is_active:
        player_name = "黒" if current_player == BLACK else "白"
        player_icon = ":black_circle:" if current_player == BLACK else ":white_circle:"
        st.info(f"{player_icon} **{player_name}** の番です", icon="👉")
        
        if st.session_state.pass_status:
            passer_name = "黒" if st.session_state.pass_status == BLACK else "白"
            st.warning(f"{passer_name} は打つ場所がなくパスしました。", icon="⚠️")
    else:
        # ゲーム終了判定
        if scores[BLACK] > scores[WHITE]:
            st.balloons()
            st.success(f"ゲーム終了！ **黒** の勝利です ({scores[BLACK]} vs {scores[WHITE]})")
        elif scores[WHITE] > scores[BLACK]:
            st.success(f"ゲーム終了！ **白** の勝利です ({scores[WHITE]} vs {scores[BLACK]})")
        else:
            st.info(f"ゲーム終了！ **引き分け** です ({scores[BLACK]} vs {scores[WHITE]})")


# ----------------- 盤面の描画 -----------------

valid_moves = get_all_valid_moves(current_player, board) if st.session_state.is_active else []

# CSSを使って盤面をきれいに表示
# ボタンのデフォルトスタイルを上書きし、盤面を中央に表示
st.markdown("""
<style>
    /* Streamlit標準のボタンの枠線を消して、盤面らしく見せる */
    .stButton > button {
        border: 1px solid #10b981; /* セルの枠線 */
        background-color: #059669; /* セルの背景 */
        padding: 0 !important;
        margin: 0 !important;
        height: 100%;
        width: 100%;
        min-height: 40px; /* セルの最小高さ */
    }
    
    /* 盤面のコンテナ設定 */
    .board-container {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 600px;
        margin: 10px auto;
        border: 4px solid #065f46;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        aspect-ratio: 1 / 1;
    }
    .othello-row {
        display: flex;
        flex: 1; /* 各行の高さを均等にする */
    }
    .othello-cell-wrapper {
        flex: 1; /* 各列の幅を均等にする */
        display: flex;
        justify-content: center;
        align-items: center;
        /* セル内のボタンをコンテナ幅いっぱいに使うための調整 */
        padding: 0;
    }
    
    .piece-icon {
        font-size: 2.5em; 
        line-height: 1;
        opacity: 1;
        transition: transform 0.2s ease-out;
    }
    .hint-dot {
        font-size: 0.8em;
        color: #fcd34d; /* yellow */
    }
</style>
""", unsafe_allow_html=True)

# 盤面全体を格納するコンテナ
st.markdown('<div class="board-container">', unsafe_allow_html=True)

# Streamlitのcolumnを使い、ボタンのクリックイベントを正確に処理する
for r in range(BOARD_SIZE):
    # 各行のコンテナ
    st.markdown('<div class="othello-row">', unsafe_allow_html=True)
    
    # 8つの列を定義（ボタンを配置するためのコンテナ）
    cols = st.columns(BOARD_SIZE)
    
    for c in range(BOARD_SIZE):
        with cols[c]:
            # セルの内容を決定
            piece = board[r, c]
            is_valid = (r, c) in valid_moves
            cell_content = ""
            button_label = " " # ボタンのラベルは空にして、CSSで調整

            if piece == BLACK:
                cell_content = '<span class="piece-icon">⚫</span>'
            elif piece == WHITE:
                cell_content = '<span class="piece-icon">⚪</span>'
            elif is_valid:
                cell_content = '<span class="hint-dot">🟡</span>'
            else:
                cell_content = " " # 空のマス

            # 駒またはヒントがある場合は、その内容をボタンに埋め込む
            if st.session_state.is_active and is_valid:
                # 有効な手であればボタンとして表示し、クリックで make_move を実行
                st.button(
                    cell_content,
                    key=f"cell_{r}_{c}",
                    on_click=make_move,
                    args=(r, c),
                    # Streamlitのボタンはデフォルトで use_container_width=True
                    # help=f"({r+1}, {c+1})に駒を置く"
                )
            else:
                # 駒が置かれているマス、または無効な空のマスは、HTMLで表示
                # これにより、再描画時のボタンの生成・削除によるエラーを回避
                st.markdown(f'<div class="othello-cell-wrapper">{cell_content}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # othello-row の閉じタグ

st.markdown('</div>', unsafe_allow_html=True) # board-container の閉じタグ

# ----------------- リセットボタン -----------------
st.button("ゲームをリセット", on_click=reset_game, use_container_width=True)
