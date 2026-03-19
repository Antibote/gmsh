import streamlit as st

# Настройка страницы (если файл запускается отдельно)
st.set_page_config(page_title="🎉 Спасибо за внимание!", layout="wide")

# Скрываем меню и футер Streamlit для более чистого вида
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Основной контент
st.markdown("""
<style>
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}
@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink-caret {
    from, to { border-color: transparent; }
    50% { border-color: #666; }
}
@keyframes rainbow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: rainbow 15s ease infinite;
}
</style>
""", unsafe_allow_html=True)

# Центрируем весь контент
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Главный заголовок
    st.markdown("""
    <h1 style='text-align: center; font-size: 5rem; margin-bottom: 0; 
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
    background-size: 300% 300%;
    animation: rainbow 10s ease infinite;
    font-weight: bold;'>
    🎉 СПАСИБО 🎉
    </h1>
    <h2 style='text-align: center; font-size: 4rem; margin-top: 0; 
    background: linear-gradient(45deg, #f7971e, #ffd200);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    animation: pulse 2s infinite;'>
    ЗА ВНИМАНИЕ!
    </h2>
    """, unsafe_allow_html=True)

    # Вращающиеся звезды
    star_cols = st.columns(3)
    with star_cols[0]:
        st.markdown("<p style='text-align: center; font-size: 3rem; animation: spin 3s linear infinite;'>⭐</p>",
                    unsafe_allow_html=True)
    with star_cols[1]:
        st.markdown("<p style='text-align: center; font-size: 4rem; animation: spin 5s linear infinite;'>🌟</p>",
                    unsafe_allow_html=True)
    with star_cols[2]:
        st.markdown("<p style='text-align: center; font-size: 3rem; animation: spin 4s linear infinite;'>✨</p>",
                    unsafe_allow_html=True)

    # Украшение из эмодзи
    emoji_row1 = st.columns(7)
    emojis1 = ["🚀", "💻", "🔥", "⚡", "🎨", "🎮", "🎯"]
    for i, col in enumerate(emoji_row1):
        with col:
            st.markdown(
                f"<p style='text-align: center; font-size: 2.5rem; animation: float {1 + i * 0.3}s ease-in-out infinite;'>{emojis1[i]}</p>",
                unsafe_allow_html=True)

    emoji_row2 = st.columns(7)
    emojis2 = ["💡", "🎪", "🌈", "⭐", "🌀", "🎲", "🎭"]
    for i, col in enumerate(emoji_row2):
        with col:
            st.markdown(
                f"<p style='text-align: center; font-size: 2.5rem; animation: float {2 + i * 0.2}s ease-in-out infinite;'>{emojis2[i]}</p>",
                unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Кнопка с сюрпризом (во всю ширину)
    if st.button("🎊 УСТРОИТЬ ФЕЙЕРВЕРК! 🎊", use_container_width=True, type="primary"):
        st.balloons()
        st.snow()
        st.success("✨ Поздравляю! Вы только что сделали этот момент незабываемым! ✨")
        st.balloons()  # Двойная порция веселья
        st.balloons()

    st.markdown("<br>", unsafe_allow_html=True)

    # Метрики в стильном оформлении
    st.markdown("""
    <h3 style='text-align: center; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);'>
    📊 СТАТИСТИКА ПРЕЗЕНТАЦИИ 📊
    </h3>
    """, unsafe_allow_html=True)

    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.metric("Слайдов", "42", "🔥")
    with metric_cols[1]:
        st.metric("Строк кода", "∞", "⚡")
    with metric_cols[2]:
        st.metric("Кофе", "☕" * 3, "энергия")
    with metric_cols[3]:
        st.metric("Улыбок", "100%", "😊")

    st.markdown("<br>", unsafe_allow_html=True)

    # Блок с кодом успеха
    with st.expander("🔮 СЕКРЕТНЫЙ КОД УСПЕХА (нажми меня)"):
        col_code, col_gif = st.columns([2, 1])
        with col_code:
            st.code("""
            # Код идеальной презентации
            import magic
            import passion
            import knowledge

            class PerfectPresentation:
                def __init__(self):
                    self.energy = float('inf')
                    self.enthusiasm = 100
                    self.content = "gmsh + FEniCS"

                def present(self):
                    while self.audience.is_happy():
                        self.show_slide()
                        self.tell_joke()
                        self.answer_questions()

                    return "🎉 STANDING OVATION 🎉"

            # Запуск
            if __name__ == "__main__":
                my_pres = PerfectPresentation()
                result = my_pres.present()
                print(result)
            """, language="python")
        with col_gif:
            st.markdown("""
            <p style='text-align: center; font-size: 5rem; animation: pulse 1s infinite;'>
            🧠
            </p>
            <p style='text-align: center;'>Мозг после такой презентации</p>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Подпись с анимацией
    st.markdown("""
    <p style='text-align: center; font-size: 2rem; color: white; 
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    border-right: 3px solid white; 
    white-space: nowrap; 
    overflow: hidden;
    margin: 0 auto;
    width: fit-content;
    animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;'>
    Сделано с ❤️ и Python
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Интерактивный слайдер настроения
    st.markdown("<h4 style='text-align: center; color: white;'>Как вам презентация?</h4>", unsafe_allow_html=True)
    mood = st.select_slider(
        "",
        options=["😤", "😐", "😊", "🤩", "💖"],
        value="💖"
    )

    if mood == "💖":
        st.balloons()
        st.markdown("<p style='text-align: center; font-size: 2rem;'>Вы лучший зритель! 🌟</p>", unsafe_allow_html=True)
    elif mood == "🤩":
        st.markdown("<p style='text-align: center; font-size: 2rem;'>✨ Спасибо! ✨</p>", unsafe_allow_html=True)
    elif mood == "😊":
        st.markdown("<p style='text-align: center; font-size: 2rem;'>😊 Рад, что понравилось!</p>",
                    unsafe_allow_html=True)
    elif mood == "😐":
        st.markdown("<p style='text-align: center; font-size: 2rem;'>🤔 Дайте шанс!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='text-align: center; font-size: 2rem;'>😱 О нет!</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Финальная кнопка
    if st.button("👏 ВЫЗВАТЬ АПЛОДИСМЕНТЫ 👏", use_container_width=True):
        for _ in range(3):
            st.balloons()
        st.success("🎭 БРАВО! БИС! 🎭")
        st.confetti = True  # Магии ради