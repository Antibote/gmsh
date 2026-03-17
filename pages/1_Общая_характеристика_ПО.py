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

st.set_page_config(page_title="📋", layout="wide")

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
    "Общая характеристика ПО": "",
    "Основные возможности Gmsh": "",
    "Применение Gmsh": ""
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))

if choice == "Общая характеристика ПО":
    st.write("""##### Общая характеристика ПО""")
    st.write(
            """
            **Gmsh** — это открытое программное обеспечение для генерации конечных элементов (mesh generation).
            Оно используется в численном моделировании и вычислительной механике, особенно в методе конечных элементов (FEM).
            """
        )

elif choice == "Основные возможности Gmsh":
    st.write("""##### Основные возможности Gmsh""")
    st.markdown(
        """
        - Генерация двумерных и трехмерных сеток
        - Поддержка различных типов элементов (треугольники, тетраэдры, гексаэдры и т. д.)
        - Встроенный язык сценариев (Gmsh scripting language)
        - Визуализация и постобработка
        - Импорт и экспорт в различные форматы (STEP, STL, MSH и др.)
        - Поддержка параметризированного моделирования
        """
        )
elif choice == "Применение Gmsh":
    st.write("""##### Применение Gmsh""")
    st.write(
        """
        - Аэродинамика
        - Машиностроение
        - Биомеханика
        - Электромагнетизм
        - Геофизика
        - ...
        """
        )
elif choice == "Пример кода для создания сетки":
    st.write("""##### Пример кода для создания сетки""")
    code = """
        // Подключение библиотеки
        SetFactory("OpenCASCADE");
        lc = 1e-2;

        // Определение точек
        Point(1) = {0, 0, 0, lc};
        Point(2) = {.1, 0, 0, lc};
        Point(3) = {.1, .3, 0, lc};
        Point(4) = {0, .3, 0, lc};

        // Построение отрезков
        Line(1) = {1, 2};
        Line(2) = {2, 3}; 
        Line(3) = {3, 4};
        Line(4) = {4, 1};

        // Построение замкнутого контура, поверхности
        Curve Loop(1) = {4, 1, -2, 3};
        Plane Surface(1) = {1};

        // Настройка сетки
        Geometry.PointNumbers = 1;
        Geometry.Color.Points = {160, 255, 0};
        General.Color.Text = White;
        Geometry.Color.Surfaces = Geometry.Color.Points;

        // 2-D сетка
        Mesh 2;
        
    """
    
    st.code(code, language="python")
    
    if st.button("Запустить пример"):
        file_path = "example.geo"
        with open(file_path, "w") as f:
            f.write(code)
        run_gmsh(file_path)
