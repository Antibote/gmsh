import streamlit as st
from PIL import Image
import base64
import subprocess
import os
import math
import gmsh
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import plotly.graph_objects as go  # Для 3D-визуализации

st.set_page_config(page_title="📱", layout="wide")

# Функция для отображения кода с возможностью копирования
def show_code(code, language="python"):
    st.code(code, language)

def run_gmsh(file_path):
    try:
        env = os.environ.copy()
        env["LIBGL_ALWAYS_SOFTWARE"] = "1"  # Используем программный рендеринг
        subprocess.run(["gmsh", file_path], check=True, env=env)
        st.success("Gmsh успешно запущен в программном режиме!")
    except FileNotFoundError:
        st.error("Gmsh не найден. Убедитесь, что он установлен и доступен в PATH.")
    except subprocess.CalledProcessError as e:
        st.error(f"Ошибка при запуске Gmsh: {e.returncode}")
        st.text(f"Вывод ошибки:\n{e.stderr}")

sections = {
    "Шаг 1. Создание новой геометрии": "",
    "Шаг 2. Определение точек": "",
    "Шаг 3. Соединение точек": "",
    "Шаг 4. Создание поверхности":"",
    "Шаг 5. Генерация сетки": "",
    "Шаг 6. Визуализация": "",
    "Шаг 7. Сохранение файла": "",
    "Пример файла Gmsh": "", 
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
st.write("""##### Интерактивные возможности создания области""")
if choice == "Шаг 1. Создание новой геометрии":

    st.markdown("""
    <style>
    pre, code {
        background-color: #e6e6e6 !important; /* Светло-серый фон */
        color: #008000 !important; /* Зелёный текст */
        font-weight: normal !important; /* Обычный шрифт */
        padding: 8px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)


    # Шаг 1: Создание новой геометрии
    st.write("""##### Шаг 1. Создание новой геометрии""")
    st.write("""
    1. Откройте Gmsh
    ``` bash 
            gmsh
    ```
    2. Перейдите в меню "File" и выберите "New" для создания нового файла
    """)
    # Место для картинки (шаг 1)
    st.image("step1_create_geometry.png", caption="Шаг 1: Создание новой геометрии",use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 2. Определение точек":

    # Шаг 2: Определение точек
    st.write("""##### Шаг 2. Определение точек""")
    st.write("""
    Для создания прямоугольника начнем с определения 4 точек.
    В верхнем меню выберите "Geometry" -> "Elementary entitie" -> "Add" -> "Point"  и щелкните на рабочей области, чтобы разместить точки
    - точка 1: [0,0,0]
    - точка 2: [L, 0, 0] — где L — длина области
    - точка 3: [L, W, 0] — где W — ширина области
    - точка 4: [0, W, 0]
    """)
    # Место для картинки (шаг 2)
    st.image("step2_define_points.png", caption="Шаг 2: Определение точек", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 3. Соединение точек":

    # Шаг 3: Соединение точек
    st.write("""##### Шаг 3. Соединение точек""")
    st.write("""
    После того как точки размещены, их нужно соединить
    1. В верхнем меню выберите "Geometry" -> "Elementary entitie" -> "Add" -> "Line"
    2. Соедините точки с помощью линий
    - линия 1 соединяет точку 1 и точку 2
    - линия 2 соединяет точку 2 и точку 3
    - линия 3 соединяет точку 3 и точку 4
    - линия 4 соединяет точку 4 и точку 1
    """)
    # Место для картинки (шаг 3)
    st.image("step3_connect_points.png", caption="Шаг 3: Соединение точек", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 4. Создание поверхности":

    # Шаг 4: Создание поверхности
    st.write("""##### Шаг 4. Создание поверхности""")
    st.write("""
    Теперь, когда у нас есть все линии, можно создать поверхность, заключенную в этих линиях
    1. Перейдите в меню "Geometry" -> "Elementary entitie" -> "Add" -> "Plane surface"
    2. Выберите линии для создания поверхности
    """)
    # Место для картинки (шаг 4)
    st.image("step4_create_surface.png", caption="Шаг 4: Создание поверхности", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 5. Генерация сетки":

    # Шаг 5: Генерация сетки
    st.write("""##### Шаг 5. Генерация сетки""")
    st.write("""
    После создания геометрии можно генерировать сетку
    1. Перейдите в меню "Mesh" и выберите "2D" для генерации двумерной сетки для поверхности
    2. Gmsh автоматически сгенерирует сетку для вашего прямоугольника
    """)
    # Место для картинки (шаг 5)
    st.image("step5_generate_mesh.png", caption="Шаг 5: Генерация сетки", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 6. Визуализация":

    # Шаг 6: Визуализация
    st.write("""##### Шаг 6. Визуализация""")
    st.write("""
    После генерации сетки вы можете переключиться на вкладку "View" и включить отображение сетки.
    Вы также можете управлять цветами, отображением и другими параметрами визуализации
    """)
    # Место для картинки (шаг 6)
    st.image("step6_visualize.png", caption="Шаг 6: Визуализация сетки", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Шаг 7. Сохранение файла":

    # Шаг 7: Сохранение файла
    st.write("""##### Шаг 7: Сохранение файла""")
    st.write("""
    Вы можете сохранить файл, выбрав "File" -> "Save Mesh"
    """)
    # Место для картинки (шаг 7)
    st.image("step7_save_file.png", caption="Шаг 7: Сохранение файла", use_container_width=True)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Пример файла Gmsh":

    # Пример команды GMSH
    st.write("""##### Пример файла Gmsh""")
    st.write("""
    Вы также можете использовать Gmsh для создания геометрии и сетки через текстовый файл. Вот пример скрипта для создания прямоугольной области

    ```bash
    // Прямоугольная область с размерами LxW

    L = 10;  // длина
    W = 5;   // ширина

    // Определение точек
    Point(1) = {0, 0, 0, 1};
    Point(2) = {L, 0, 0, 1};
    Point(3) = {L, W, 0, 1};
    Point(4) = {0, W, 0, 1};

    // Определение линий
    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};

    // Создание поверхности
    Line Loop(1) = {1, 2, 3, 4};
    Plane Surface(1) = {1};

    // Генерация сетки
    Mesh 2;
    """)

    def run_gmsh_view():
        try:
            # Попытка запустить GMSH
            subprocess.run(["gmsh"], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Ошибка при запуске Gmsh: {e}")
        except FileNotFoundError:
            st.error("Gmsh не найден. Убедитесь, что GMSH установлен и доступен в пути.")

    if st.button("Запустить Gmsh"):
        run_gmsh_view()

elif choice == "Замечание":
    st.write("""##### Замечание""")
    st.write(""" Gmsh предоставляет множество инструментов для создания и визуализации геометрий с помощью графического интерфейса. Мы можем использовать Gmsh для построения простых геометрических областей, генерации сеток и их визуализации. Визуализация и настройка сетки возможна через интерфейс, что упрощает процесс проектирования. """)