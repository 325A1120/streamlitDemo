import streamlit as st
import random
import time
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("🏀 アジアの奇跡（日本） vs グローバルガーディアン（アメリカ）")

# ===== 試合会場の画像 =====
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

# ===== 試合開始ボタン =====
if st.button("試合開始"):
    japan_total = 0
    global_total = 0

    for quarter in range(1, 5):
        st.subheader(f"🔥 第{quarter}試合開始！")

        japan = 0
        global_g = 0

        for minute in range(10, 0, -1):
            time.sleep(0.3)

            if random.random() < 0.5:
                japan += 2
                st.write(f"第{quarter}試合 残り{minute}分：日本が2点！")
            else:
                global_g += 2
                st.write(f"第{quarter}試合 残り{minute}分：アメリカが2点！")

        st.write(f"▶ 第{quarter}試合結果：日本 {japan} - アメリカ {global_g}")

        japan_total += japan
        global_total += global_g

    st.subheader("🏁 最終結果")
    st.write(f"日本 {japan_total} vs アメリカ {global_total}")

    if japan_total > global_total:
        st.success("🏆 アジアの奇跡（日本）の勝利！")
    elif japan_total < global_total:
        st.error("💀 グローバルガーディアン（アメリカ）の勝利…")
    else:
        st.info("🤝 引き分け！")
