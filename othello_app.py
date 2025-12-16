{\rtf1\ansi\ansicpg932\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red111\green14\blue195;\red236\green241\blue247;\red0\green0\blue0;
\red77\green80\blue85;\red164\green69\blue11;\red24\green112\blue43;}
{\*\expandedcolortbl;;\cssrgb\c51765\c18824\c80784;\cssrgb\c94118\c95686\c97647;\cssrgb\c0\c0\c0;
\cssrgb\c37255\c38824\c40784;\cssrgb\c70980\c34902\c3137;\cssrgb\c9412\c50196\c21961;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh20960\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  streamlit \cf2 \strokec2 as\cf0 \strokec4  st\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  numpy \cf2 \strokec2 as\cf0 \strokec4  np\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # \uc0\u23450 \u25968 \u12392 \u21021 \u26399 \u35373 \u23450 \cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # \uc0\u12466 \u12540 \u12512 \u12398 \u29366 \u24907 \u23450 \u25968 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 EMPTY = \cf6 \strokec6 0\cf0 \cb1 \strokec4 \
\cb3 BLACK = \cf6 \strokec6 1\cf0 \cb1 \strokec4 \
\cb3 WHITE = \cf6 \strokec6 2\cf0 \cb1 \strokec4 \
\cb3 BOARD_SIZE = \cf6 \strokec6 8\cf0 \cb1 \strokec4 \
\cb3 DIRECTIONS = [\cb1 \
\cb3     (\cf6 \strokec6 -1\cf0 \strokec4 , \cf6 \strokec6 0\cf0 \strokec4 ), (\cf6 \strokec6 -1\cf0 \strokec4 , \cf6 \strokec6 1\cf0 \strokec4 ), (\cf6 \strokec6 0\cf0 \strokec4 , \cf6 \strokec6 1\cf0 \strokec4 ), (\cf6 \strokec6 1\cf0 \strokec4 , \cf6 \strokec6 1\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 1\cf0 \strokec4 , \cf6 \strokec6 0\cf0 \strokec4 ), (\cf6 \strokec6 1\cf0 \strokec4 , \cf6 \strokec6 -1\cf0 \strokec4 ), (\cf6 \strokec6 0\cf0 \strokec4 , \cf6 \strokec6 -1\cf0 \strokec4 ), (\cf6 \strokec6 -1\cf0 \strokec4 , \cf6 \strokec6 -1\cf0 \strokec4 )\cb1 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Streamlit\uc0\u12398 \u12475 \u12483 \u12471 \u12519 \u12531 \u12473 \u12486 \u12540 \u12488 \u12391 \u12466 \u12540 \u12512 \u12398 \u29366 \u24907 \u12434 \u31649 \u29702 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 'board'\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  st.session_state:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=\cf2 \strokec2 int\cf0 \strokec4 )\cb1 \
\cb3     st.session_state.current_player = BLACK\cb1 \
\cb3     st.session_state.is_active = \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # \uc0\u21021 \u26399 \u37197 \u32622 \cf0 \cb1 \strokec4 \
\cb3     st.session_state.board[\cf6 \strokec6 3\cf0 \strokec4 , \cf6 \strokec6 3\cf0 \strokec4 ] = WHITE\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 3\cf0 \strokec4 , \cf6 \strokec6 4\cf0 \strokec4 ] = BLACK\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 4\cf0 \strokec4 , \cf6 \strokec6 3\cf0 \strokec4 ] = BLACK\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 4\cf0 \strokec4 , \cf6 \strokec6 4\cf0 \strokec4 ] = WHITE\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # \uc0\u12466 \u12540 \u12512 \u12525 \u12472 \u12483 \u12463  (Python)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  get_opponent(player):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u30456 \u25163 \u12398 \u12503 \u12524 \u12452 \u12516 \u12540 \u12398 \u33394 \u12434 \u21462 \u24471 """\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  WHITE \cf2 \strokec2 if\cf0 \strokec4  player == BLACK \cf2 \strokec2 else\cf0 \strokec4  BLACK\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  is_within_bounds(r, c):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u24231 \u27161 \u12364 \u30436 \u38754 \u20869 \u12363 \u12481 \u12455 \u12483 \u12463 """\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 0\cf0 \strokec4  <= r < BOARD_SIZE \cf2 \strokec2 and\cf0 \strokec4  \cf6 \strokec6 0\cf0 \strokec4  <= c < BOARD_SIZE\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  check_direction_for_flips(r, c, dr, dc, player, board):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u29305 \u23450 \u12398 \u26041 \u21521 \u12391 \u12402 \u12387 \u12367 \u12426 \u36820 \u12379 \u12427 \u39378 \u12434 \u12481 \u12455 \u12483 \u12463 """\cf0 \cb1 \strokec4 \
\cb3     opponent = get_opponent(player)\cb1 \
\cb3     flipped_pieces = []\cb1 \
\cb3     r_curr, c_curr = r + dr, c + dc\cb1 \
\
\cb3     \cf2 \strokec2 while\cf0 \strokec4  is_within_bounds(r_curr, c_curr):\cb1 \
\cb3         piece = board[r_curr, c_curr]\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  piece == opponent:\cb1 \
\cb3             flipped_pieces.append((r_curr, c_curr))\cb1 \
\cb3         \cf2 \strokec2 elif\cf0 \strokec4  piece == player:\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  flipped_pieces \cf5 \strokec5 # \uc0\u33258 \u20998 \u12398 \u39378 \u12391 \u25375 \u12417 \u12383 \cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 : \cf5 \strokec5 # EMPTY\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  [] \cf5 \strokec5 # \uc0\u38291 \u12395 \u33258 \u20998 \u12398 \u39378 \u12364 \u12394 \u12356 \cf0 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         r_curr += dr\cb1 \
\cb3         c_curr += dc\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  []\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  get_valid_flips(r, c, player, board):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u25351 \u23450 \u12375 \u12383 \u12510 \u12473 \u12395 \u25171 \u12387 \u12383 \u22580 \u21512 \u12395 \u12402 \u12387 \u12367 \u12426 \u36820 \u12379 \u12427 \u20840 \u12390 \u12398 \u39378 \u12398 \u12522 \u12473 \u12488 \u12434 \u21462 \u24471 """\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  board[r, c] != EMPTY:\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  []\cb1 \
\cb3     \cb1 \
\cb3     total_flips = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  dr, dc \cf2 \strokec2 in\cf0 \strokec4  DIRECTIONS:\cb1 \
\cb3         flips_in_direction = check_direction_for_flips(r, c, dr, dc, player, board)\cb1 \
\cb3         total_flips.extend(flips_in_direction)\cb1 \
\cb3         \cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  total_flips\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  get_all_valid_moves(player, board):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u29694 \u22312 \u12398 \u12503 \u12524 \u12452 \u12516 \u12540 \u12364 \u25171 \u12390 \u12427 \u20840 \u12390 \u12398 \u26377 \u21177 \u12394 \u12510 \u12473 \u12434 \u12522 \u12473 \u12488 \u12450 \u12483 \u12503 """\cf0 \cb1 \strokec4 \
\cb3     valid_moves = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  r \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (BOARD_SIZE):\cb1 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (BOARD_SIZE):\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  get_valid_flips(r, c, player, board):\cb1 \
\cb3                 valid_moves.append((r, c))\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  valid_moves\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  make_move(r, c):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u39378 \u12434 \u25171 \u12385 \u12289 \u12402 \u12387 \u12367 \u12426 \u36820 \u12375 \u12289 \u12503 \u12524 \u12452 \u12516 \u12540 \u12434 \u20132 \u20195 \u12377 \u12427 \u20966 \u29702 """\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  st.session_state.is_active:\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \cb1 \strokec4 \
\
\cb3     player = st.session_state.current_player\cb1 \
\cb3     flips = get_valid_flips(r, c, player, st.session_state.board)\cb1 \
\
\cb3     \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  flips:\cb1 \
\cb3         st.warning(\cf7 \strokec7 "\uc0\u12381 \u12371 \u12395 \u12399 \u25171 \u12390 \u12414 \u12379 \u12435 \u12290 \u26377 \u21177 \u12394 \u12510 \u12473 \u12434 \u12463 \u12522 \u12483 \u12463 \u12375 \u12390 \u12367 \u12384 \u12373 \u12356 \u12290 "\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 # \uc0\u39378 \u12434 \u25171 \u12385 \u12289 \u12402 \u12387 \u12367 \u12426 \u36820 \u12377 \cf0 \cb1 \strokec4 \
\cb3     new_board = st.session_state.board.copy()\cb1 \
\cb3     new_board[r, c] = player\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  flip_r, flip_c \cf2 \strokec2 in\cf0 \strokec4  flips:\cb1 \
\cb3         new_board[flip_r, flip_c] = player\cb1 \
\cb3     st.session_state.board = new_board\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # \uc0\u12503 \u12524 \u12452 \u12516 \u12540 \u12434 \u20132 \u20195 \u12375 \u12289 \u12497 \u12473 \u21028 \u23450 \cf0 \cb1 \strokec4 \
\cb3     switch_player()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  switch_player():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u12503 \u12524 \u12452 \u12516 \u12540 \u12434 \u20132 \u20195 \u12375 \u12289 \u12497 \u12473 \u12539 \u32066 \u20102 \u21028 \u23450 \u12434 \u34892 \u12358 """\cf0 \cb1 \strokec4 \
\cb3     current_player = st.session_state.current_player\cb1 \
\cb3     next_player = get_opponent(current_player)\cb1 \
\
\cb3     \cf5 \strokec5 # 1. \uc0\u27425 \u12398 \u12503 \u12524 \u12452 \u12516 \u12540 \u12364 \u25171 \u12390 \u12427 \u12363 \u65311 \cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  get_all_valid_moves(next_player, st.session_state.board):\cb1 \
\cb3         st.session_state.current_player = next_player\cb1 \
\cb3         st.session_state.pass_status = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf0 \cb1 \strokec4 \
\
\cb3     \cf5 \strokec5 # 2. \uc0\u27425 \u12398 \u12503 \u12524 \u12452 \u12516 \u12540 \u12364 \u25171 \u12390 \u12394 \u12356 \u22580 \u21512 \u12289 \u29694 \u22312 \u12398 \u12503 \u12524 \u12452 \u12516 \u12540 \u12395 \u25147 \u12387 \u12390 \u25171 \u12390 \u12427 \u12363 \u65311  (\u12497 \u12473 )\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  get_all_valid_moves(current_player, st.session_state.board):\cb1 \
\cb3         st.session_state.current_player = current_player \cf5 \strokec5 # \uc0\u12497 \u12473 \u12375 \u12390 \u25163 \u30058 \u12364 \u25147 \u12427 \cf0 \cb1 \strokec4 \
\cb3         st.session_state.pass_status = next_player\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # 3. \uc0\u20001 \u26041 \u25171 \u12390 \u12394 \u12356 \u22580 \u21512 \u12289 \u12466 \u12540 \u12512 \u32066 \u20102 \cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         st.session_state.is_active = \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3         st.session_state.pass_status = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  get_scores(board):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u29694 \u22312 \u12398 \u12473 \u12467 \u12450 \u12434 \u35336 \u31639 """\cf0 \cb1 \strokec4 \
\cb3     score = \{\cb1 \
\cb3         BLACK: np.\cf2 \strokec2 sum\cf0 \strokec4 (board == BLACK),\cb1 \
\cb3         WHITE: np.\cf2 \strokec2 sum\cf0 \strokec4 (board == WHITE)\cb1 \
\cb3     \}\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  score\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  reset_game():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """\uc0\u12466 \u12540 \u12512 \u12398 \u29366 \u24907 \u12434 \u12522 \u12475 \u12483 \u12488 """\cf0 \cb1 \strokec4 \
\cb3     st.session_state.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=\cf2 \strokec2 int\cf0 \strokec4 )\cb1 \
\cb3     st.session_state.current_player = BLACK\cb1 \
\cb3     st.session_state.is_active = \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3     st.session_state.pass_status = \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 3\cf0 \strokec4 , \cf6 \strokec6 3\cf0 \strokec4 ] = WHITE\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 3\cf0 \strokec4 , \cf6 \strokec6 4\cf0 \strokec4 ] = BLACK\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 4\cf0 \strokec4 , \cf6 \strokec6 3\cf0 \strokec4 ] = BLACK\cb1 \
\cb3     st.session_state.board[\cf6 \strokec6 4\cf0 \strokec4 , \cf6 \strokec6 4\cf0 \strokec4 ] = WHITE\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # Streamlit UI (\uc0\u34920 \u31034 )\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # =================================================================\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.set_page_config(page_title=\cf7 \strokec7 "\uc0\u12458 \u12475 \u12525  (\u12522 \u12496 \u12540 \u12471 )"\cf0 \strokec4 , layout=\cf7 \strokec7 "centered"\cf0 \strokec4 )\cb1 \
\
\cb3 st.title(\cf7 \strokec7 "\uc0\u31777 \u26131 \u12458 \u12475 \u12525  (\u12522 \u12496 \u12540 \u12471 ) \u12450 \u12503 \u12522 "\cf0 \strokec4 )\cb1 \
\
\cb3 board = st.session_state.board\cb1 \
\cb3 current_player = st.session_state.current_player\cb1 \
\cb3 scores = get_scores(board)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ----------------- \uc0\u12473 \u12486 \u12540 \u12479 \u12473 \u34920 \u31034  -----------------\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 col1, col2, col3 = st.columns([\cf6 \strokec6 1\cf0 \strokec4 , \cf6 \strokec6 2\cf0 \strokec4 , \cf6 \strokec6 1\cf0 \strokec4 ])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf0 \strokec4  col1:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.markdown(\cf7 \strokec7 f"**\uc0\u40658 ** :black_circle: \cf0 \strokec4 \{scores[BLACK]\}\cf7 \strokec7  \uc0\u39378 "\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf0 \strokec4  col3:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.markdown(\cf7 \strokec7 f"**\uc0\u30333 ** :white_circle: \cf0 \strokec4 \{scores[WHITE]\}\cf7 \strokec7  \uc0\u39378 "\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 with\cf0 \strokec4  col2:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 if\cf0 \strokec4  st.session_state.is_active:\cb1 \
\cb3         player_name = \cf7 \strokec7 "\uc0\u40658 "\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  current_player == BLACK \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 "\uc0\u30333 "\cf0 \cb1 \strokec4 \
\cb3         player_icon = \cf7 \strokec7 ":black_circle:"\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  current_player == BLACK \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 ":white_circle:"\cf0 \cb1 \strokec4 \
\cb3         st.info(\cf7 \strokec7 f"\cf0 \strokec4 \{player_icon\}\cf7 \strokec7  **\cf0 \strokec4 \{player_name\}\cf7 \strokec7 ** \uc0\u12398 \u30058 \u12391 \u12377 "\cf0 \strokec4 , icon=\cf7 \strokec7 "\uc0\u55357 \u56393 "\cf0 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  st.session_state.pass_status:\cb1 \
\cb3             passer_name = \cf7 \strokec7 "\uc0\u40658 "\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  st.session_state.pass_status == BLACK \cf2 \strokec2 else\cf0 \strokec4  \cf7 \strokec7 "\uc0\u30333 "\cf0 \cb1 \strokec4 \
\cb3             st.warning(\cf7 \strokec7 f"\cf0 \strokec4 \{passer_name\}\cf7 \strokec7  \uc0\u12399 \u25171 \u12388 \u22580 \u25152 \u12364 \u12394 \u12367 \u12497 \u12473 \u12375 \u12414 \u12375 \u12383 \u12290 "\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 # \uc0\u12466 \u12540 \u12512 \u32066 \u20102 \u21028 \u23450 \cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  scores[BLACK] > scores[WHITE]:\cb1 \
\cb3             st.balloons()\cb1 \
\cb3             st.success(\cf7 \strokec7 f"\uc0\u12466 \u12540 \u12512 \u32066 \u20102 \u65281  **\u40658 ** \u12398 \u21213 \u21033 \u12391 \u12377  (\cf0 \strokec4 \{scores[BLACK]\}\cf7 \strokec7  vs \cf0 \strokec4 \{scores[WHITE]\}\cf7 \strokec7 )"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 elif\cf0 \strokec4  scores[WHITE] > scores[BLACK]:\cb1 \
\cb3             st.success(\cf7 \strokec7 f"\uc0\u12466 \u12540 \u12512 \u32066 \u20102 \u65281  **\u30333 ** \u12398 \u21213 \u21033 \u12391 \u12377  (\cf0 \strokec4 \{scores[WHITE]\}\cf7 \strokec7  vs \cf0 \strokec4 \{scores[BLACK]\}\cf7 \strokec7 )"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             st.info(\cf7 \strokec7 f"\uc0\u12466 \u12540 \u12512 \u32066 \u20102 \u65281  **\u24341 \u12365 \u20998 \u12369 ** \u12391 \u12377  (\cf0 \strokec4 \{scores[BLACK]\}\cf7 \strokec7  vs \cf0 \strokec4 \{scores[WHITE]\}\cf7 \strokec7 )"\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ----------------- \uc0\u30436 \u38754 \u12398 \u25551 \u30011  -----------------\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 valid_moves = get_all_valid_moves(current_player, board) \cf2 \strokec2 if\cf0 \strokec4  st.session_state.is_active \cf2 \strokec2 else\cf0 \strokec4  []\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # CSS\uc0\u12434 \u20351 \u12387 \u12390 \u30436 \u38754 \u12434 \u12365 \u12428 \u12356 \u12395 \u34920 \u31034 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.markdown(\cf7 \strokec7 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 <style>\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     .board-container \{\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         display: grid;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         grid-template-columns: repeat(8, 1fr);\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         grid-template-rows: repeat(8, 1fr);\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         border: 4px solid #065f46; /* dark green */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         aspect-ratio: 1 / 1;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         margin: 10px auto;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     \}\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     .othello-cell \{\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         display: flex;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         justify-content: center;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         align-items: center;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         border: 1px solid #10b981; /* emerald green */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         background-color: #059669; /* medium green */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         min-height: 40px;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     \}\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     .piece-black \{\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         font-size: 2.5em; /* \uc0\u39378 \u12398 \u12469 \u12452 \u12474  */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         line-height: 1;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         opacity: 1;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         transition: transform 0.2s ease-out;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     \}\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     .piece-white \{\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         font-size: 2.5em; /* \uc0\u39378 \u12398 \u12469 \u12452 \u12474  */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         line-height: 1;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         opacity: 1;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         transition: transform 0.2s ease-out;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     \}\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     .hint-dot \{\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         font-size: 0.8em;\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7         color: #fcd34d; /* yellow */\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     \}\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 </style>\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 """\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.markdown(\cf7 \strokec7 '<div class="board-container">'\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Streamlit\uc0\u12398 column\u27231 \u33021 \u12434 \u20351 \u12387 \u12390 8x8\u12398 \u12464 \u12522 \u12483 \u12489 \u12434 \u20316 \u25104 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  r \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (BOARD_SIZE):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     cols = st.columns(BOARD_SIZE)\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (BOARD_SIZE):\cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  cols[c]:\cb1 \
\cb3             cell_content = \cf7 \strokec7 ""\cf0 \cb1 \strokec4 \
\cb3             cell_class = \cf7 \strokec7 "othello-cell"\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3             piece = board[r, c]\cb1 \
\cb3             is_valid = (r, c) \cf2 \strokec2 in\cf0 \strokec4  valid_moves\cb1 \
\
\cb3             \cf2 \strokec2 if\cf0 \strokec4  piece == BLACK:\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u40658 \u39378 : Unicode\u12398 \u40658 \u20024 \cf0 \cb1 \strokec4 \
\cb3                 cell_content = \cf7 \strokec7 '<span class="piece-black">\uc0\u9899 </span>'\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  piece == WHITE:\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u30333 \u39378 : Unicode\u12398 \u30333 \u20024 \cf0 \cb1 \strokec4 \
\cb3                 cell_content = \cf7 \strokec7 '<span class="piece-white">\uc0\u9898 </span>'\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 elif\cf0 \strokec4  is_valid:\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u26377 \u21177 \u12394 \u25163 : \u12498 \u12531 \u12488 \u12398 \u28857 \cf0 \cb1 \strokec4 \
\cb3                 cell_content = \cf7 \strokec7 '<span class="hint-dot">\uc0\u55357 \u57313 </span>'\cf0 \cb1 \strokec4 \
\
\cb3             \cf5 \strokec5 # \uc0\u39378 \u12434 \u32622 \u12367 \u12508 \u12479 \u12531  (\u26377 \u21177 \u12394 \u25163 \u12398 \u12415 \u26377 \u21177 \u21270 )\cf0 \cb1 \strokec4 \
\cb3             st.markdown(\cf7 \strokec7 f'<div class="\cf0 \strokec4 \{cell_class\}\cf7 \strokec7 ">'\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  st.session_state.is_active \cf2 \strokec2 and\cf0 \strokec4  is_valid:\cb1 \
\cb3                 \cf5 \strokec5 # Streamlit\uc0\u12398 \u12508 \u12479 \u12531 \u12391 \u12463 \u12522 \u12483 \u12463 \u12434 \u20966 \u29702 \cf0 \cb1 \strokec4 \
\cb3                 st.button(\cb1 \
\cb3                     cell_content,\cb1 \
\cb3                     key=\cf7 \strokec7 f"cell_\cf0 \strokec4 \{r\}\cf7 \strokec7 _\cf0 \strokec4 \{c\}\cf7 \strokec7 "\cf0 \strokec4 ,\cb1 \
\cb3                     on_click=make_move,\cb1 \
\cb3                     args=(r, c),\cb1 \
\cb3                     \cf5 \strokec5 # \uc0\u12508 \u12479 \u12531 \u12398 \u35211 \u12383 \u30446 \u12434 \u36879 \u26126 \u12395 \u12375 \u12289 \u20013 \u12398 \u12467 \u12531 \u12486 \u12531 \u12484 \u12398 \u12415 \u12364 \u35211 \u12360 \u12427 \u12424 \u12358 \u12395 \u12377 \u12427 \cf0 \cb1 \strokec4 \
\cb3                     use_container_width=\cf2 \strokec2 True\cf0 \strokec4 ,\cb1 \
\cb3                     \cf2 \strokec2 help\cf0 \strokec4 =\cf7 \strokec7 f"(\cf0 \strokec4 \{r+1\}\cf7 \strokec7 , \cf0 \strokec4 \{c+1\}\cf7 \strokec7 )\uc0\u12395 \u39378 \u12434 \u32622 \u12367 "\cf0 \cb1 \strokec4 \
\cb3                 )\cb1 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 \cf5 \strokec5 # \uc0\u39378 \u12420 \u12498 \u12531 \u12488 \u12364 \u12354 \u12427 \u22580 \u25152 \u12289 \u12414 \u12383 \u12399 \u12466 \u12540 \u12512 \u38750 \u27963 \u24615 \u26178 \u12399 \u12467 \u12531 \u12486 \u12531 \u12484 \u12434 \u30452 \u25509 \u34920 \u31034 \cf0 \cb1 \strokec4 \
\cb3                 st.markdown(cell_content, unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\cb3             st.markdown(\cf7 \strokec7 '</div>'\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\cb3 st.markdown(\cf7 \strokec7 '</div>'\cf0 \strokec4 , unsafe_allow_html=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ----------------- \uc0\u12522 \u12475 \u12483 \u12488 \u12508 \u12479 \u12531  -----------------\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.button(\cf7 \strokec7 "\uc0\u12466 \u12540 \u12512 \u12434 \u12522 \u12475 \u12483 \u12488 "\cf0 \strokec4 , on_click=reset_game, use_container_width=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
}