import streamlit as st
import random
import time
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("🏀 アジアの奇跡（日本） vs グローバルガーディアン（アメリカ）")

# 試合会場の画像 
image_path = "./images/basketball_game.png"

if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(
        img,
        caption="バスケットボール会場での試合風景（イメージ）",
        use_container_width=True
    )
else:
    st.warning("試合会場の画像が見つかりません")

# チーム・ポジション別の選手データ
rosters = {
    "日本": {
        "PG": "河村 勇輝",
        "SG": "富永 啓生",
        "SF": "渡邊 雄太",
        "PF": "八村 塁",
        "C": "ジョシュ・ホーキンソン"
    },
    "アメリカ": {
        "PG": "ステフィン・カリー",
        "SG": "アンソニー・エドワーズ",
        "SF": "レブロン・ジェームス",
        "PF": "ケビン・デュラント"

# 試合開始ボタン
if st.button("🔥 試合開始（ティップオフ！）", type="primary"):
    japan_total = 0
    global_total = 0

    # リアルタイム更新用のスコアボード枠（画面上部に固定）
    scoreboard_placeholder = st.empty()

    st.subheader("🎙️ リアルタイム実況ログ（最新が上）")
    # 高さを指定してスクロール可能にするコンテナ
    log_container = st.container(height=300)
    with log_container:
        log_placeholder = st.empty()
    log_history = []

    # 発生するプレイのパターン（テキスト, 得点）
    plays = [
        ("✨ 鮮やかな3ポイントシュートが決まった！", 3),
        ("🏀 ドライブからレイアップで2点追加！", 2),
        ("💥 豪快なダンクシュート！！会場が沸く！", 2),
        ("🎯 ミドルレンジのジャンプシュート成功！", 2),
        ("🛡️ 激しいディフェンス！シュートはリングに嫌われた…", 0),
        ("🚫 見事なブロックショット！得点を許さない！", 0),
    ]

    def update_scoreboard(q_text, time_text, j_score, g_score):
        # スコアボードを最新状態に書き換える
        with scoreboard_placeholder.container():
            st.markdown(f"### ⏱️ {q_text} | {time_text}")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="🇯🇵 アジアの奇跡（日本）", value=f"{j_score}点")
            with col2:
                st.metric(label="🇺🇸 グローバルガーディアン（アメリカ）", value=f"{g_score}点")

    # 初期スコア表示（ここからインデントを関数の外に戻しました）
    update_scoreboard("試合開始前", "残り 10:00", 0, 0)

    for quarter in range(1, 5):
        log_history.insert(0, f"**--- 🔥 第{quarter}クォーター開始！ ---**")

        for minute in range(10, 0, -1):
            time.sleep(0.4)

            # 攻撃チームとプレイ内容をランダムに決定
            team = "日本" if random.random() < 0.5 else "アメリカ"
            play_text, points = random.choice(plays)

            if points > 0:
                if team == "日本":
                    japan_total += points
                    event_msg = f"🔴 **[Q{quarter} 残り{minute}分] 日本**：{play_text}（+{points}点）"
                else:
                    global_total += points
                    event_msg = f"🔵 **[Q{quarter} 残り{minute}分] アメリカ**：{play_text}（+{points}点）"
            else:
                event_msg = f"⚪ **[Q{quarter} 残り{minute}分] {team}の攻撃**：{play_text}"

            # スコアボードとログを更新
            update_scoreboard(f"第{quarter}クォーター", f"残り {minute}分", japan_total, global_total)

            log_history.insert(0, event_msg)
            # コンテナ内のプレースホルダーを最新履歴で上書き表示
            log_placeholder.markdown("\n\n".join(log_history))

        log_history.insert(0, f"▶ **第{quarter}クォーター終了（日本 {japan_total} - {global_total} アメリカ）**")
        log_placeholder.markdown("\n\n".join(log_history))

    # 試合終了時のスコアボード更新
    update_scoreboard("試合終了", "FINAL", japan_total, global_total)

    st.divider()
    st.subheader("🏁 最終結果")

    if japan_total > global_total:
        st.balloons()  # 勝利時に風船を飛ばす
        st.success(f"🏆 **{japan_total} - {global_total}** で アジアの奇跡（日本）の勝利！！")
    elif japan_total < global_total:
        st.error(f"💀 **{japan_total} - {global_total}** で グローバルガーディアン（アメリカ）の勝利…")
    else:
        st.info(f"🤝 **{japan_total} - {global_total}** で 引き分け！")
