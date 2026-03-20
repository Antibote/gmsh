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

st.set_page_config(page_title="🛠️", layout="wide")

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
    "Явное задание через точки, линии и поверхности": "",
    "OpenCASCADE": "",
    "Импорт CAD-модели": "",
    "Замечание":"",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
st.write("""##### Создание области""")
if choice == "Явное задание через точки, линии и поверхности":
    st.write("""##### Явное задание через точки, линии и поверхности""")
    st.write("""
    Этот метод использует базовые геометрические элементы Gmsh: точки, линии, поверхностные петли и объемы
     - **0D -> 1D -> 2D -> 3D**
    """)
    st.subheader("Шаг 1. Определение точек")
    st.write("""###### Шаг 1. Определение точек""")

    geo_code1 = """
    // Создаем точки
    L = 1.0; // Длина ребра куба
    Nx = 10; // Число элементов по X
    Ny = 10; // Число элементов по Y
    Nz = 10; // Число элементов по Z

    Point(1) = {0, 0, 0, L/Nx};
    Point(2) = {L, 0, 0, L/Nx};
    Point(3) = {L, L, 0, L/Nx};
    Point(4) = {0, L, 0, L/Nx};
    Point(5) = {0, 0, L, L/Nx};
    Point(6) = {L, 0, L, L/Nx};
    Point(7) = {L, L, L, L/Nx};
    Point(8) = {0, L, L, L/Nx};
    """
    show_code(geo_code1, "python")

    st.write("""###### Шаг 2. Построение ребер куба""")

    geo_code2 = """
    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};
    Line(5) = {5, 6};
    Line(6) = {6, 7};
    Line(7) = {7, 8};
    Line(8) = {8, 5};
    Line(9) = {1, 5};
    Line(10) = {2, 6};
    Line(11) = {3, 7};
    Line(12) = {4, 8};
    
    """
    show_code(geo_code2, "python")

    st.write("""###### Шаг 3. Построение поверхности куба""")

    geo_code3 = """
    // Создаём поверхности
    Line Loop(13) = {1, 2, 3, 4};
    Plane Surface(14) = {13};
    Line Loop(15) = {5, 6, 7, 8};
    Plane Surface(16) = {15};
    Line Loop(17) = {1, 10, -5, -9};
    Plane Surface(18) = {17};
    Line Loop(19) = {2, 11, -6, -10};
    Plane Surface(20) = {19};
    Line Loop(21) = {3, 12, -7, -11};
    Plane Surface(22) = {21};
    Line Loop(23) = {4, 9, -8, -12};
    Plane Surface(24) = {23};

    """
    show_code(geo_code3, "python")

    st.write("""###### Шаг 4. Построение объема""")

    geo_code4 = """
    // Создаём объем
    Surface Loop(25) = {14, 16, 18, 20, 22, 24};
    Volume(26) = {25};

    // Определяем сетку
    Transfinite Line {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} = Nx+1 Using Progression 1;
    Transfinite Surface {14, 16, 18, 20, 22, 24};
    Transfinite Volume {26};
    Recombine Surface {14, 16, 18, 20, 22, 24};
    Physical Volume("Cube1") = {26};
    Color Red {Volume{26};}
    Mesh 3;
    """
    show_code(geo_code4, "python")

    geo_full_code = geo_code1 + geo_code2 + geo_code3 + geo_code4

    # Загрузка файла примера
    def save_example_file():
        example_file_path = './example.geo'
        with open(example_file_path, 'w') as f:
            f.write(geo_full_code)
        return example_file_path

    # Кнопка для загрузки и запуска примера
    if st.button("Пример 1"):
        example_file_path = save_example_file()
        run_gmsh(example_file_path)

    st.write("""
     - Недостатки: трудно задавать сложную геометрию
     - Преимущества: полный контроль над топологией
    """)

elif choice == "OpenCASCADE":
    st.write("""##### OpenCASCADE""")
    
    st.write("""
    Этот метод упрощает построение сложных геометрий за счет использования встроенных примитивов
    """)
    geo_code5 = """
    // Определяем размеры кубов
    L = 1.0; // Длина ребра куба
    Nx = 10; // Число элементов по X
    Ny = 10; // Число элементов по Y
    Nz = 10; // Число элементов по Z

    // Первый куб (классический способ)
    Point(1) = {0, 0, 0, L/Nx};
    Point(2) = {L, 0, 0, L/Nx};
    Point(3) = {L, L, 0, L/Nx};
    Point(4) = {0, L, 0, L/Nx};
    Point(5) = {0, 0, L, L/Nx};
    Point(6) = {L, 0, L, L/Nx};
    Point(7) = {L, L, L, L/Nx};
    Point(8) = {0, L, L, L/Nx};

    Line(1) = {1, 2};
    Line(2) = {2, 3};
    Line(3) = {3, 4};
    Line(4) = {4, 1};
    Line(5) = {5, 6};
    Line(6) = {6, 7};
    Line(7) = {7, 8};
    Line(8) = {8, 5};
    Line(9) = {1, 5};
    Line(10) = {2, 6};
    Line(11) = {3, 7};
    Line(12) = {4, 8};

    Line Loop(13) = {1, 2, 3, 4};
    Plane Surface(14) = {13};
    Line Loop(15) = {5, 6, 7, 8};
    Plane Surface(16) = {15};
    Line Loop(17) = {1, 10, -5, -9};
    Plane Surface(18) = {17};
    Line Loop(19) = {2, 11, -6, -10};
    Plane Surface(20) = {19};
    Line Loop(21) = {3, 12, -7, -11};
    Plane Surface(22) = {21};
    Line Loop(23) = {4, 9, -8, -12};
    Plane Surface(24) = {23};

    Surface Loop(25) = {14, 16, 18, 20, 22, 24};
    Volume(26) = {25};

    Physical Volume("Cube1") = {26};
    Color Red {Volume{26};}

    // Второй куб (через OpenCASCADE)
    SetFactory("OpenCASCADE");
    Box(27) = {L + 0.5, 0, 0, L, L, L};
    Physical Volume("Cube2") = {27};
    Color Blue {Volume{27};}

    // Определяем сетку
    Transfinite Line {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12} = Nx+1 Using Progression 1;
    Transfinite Surface {14, 16, 18, 20, 22, 24};
    Transfinite Volume {26};
    Recombine Surface {14, 16, 18, 20, 22, 24};
    Mesh 3;
    """
    show_code(geo_code5, "python")

    # Загрузка файла примера
    def save_example_file():
        example_file_path = './example.geo'
        with open(example_file_path, 'w') as f:
            f.write(geo_code5)
        return example_file_path

    # Кнопка для загрузки и запуска примера
    if st.button("Пример 2"):
        example_file_path = save_example_file()
        run_gmsh(example_file_path)

    st.write("""
     - Преимущества: меньше кода, удобное управление геометрией
     - Недостатки: меньше контроля над отдельными гранями
    """)

elif choice == "Импорт CAD-модели":

    st.write("""##### Импорт CAD-модели""")
    st.write("""
    Если у вас есть готовая CAD-модель цилиндра, например, в формате STEP, можно просто импортировать и создать сетку
    """)

    geo_code6 = """
    // Импортируем CAD-модель
    Merge "cylinder.step";

    // Устанавливаем размер сетки
    MeshSize {1} = 0.2;

    // Генерируем объемную сетку
    Mesh 3;
    """
    show_code(geo_code6, "python")

    st.write("""
     - Преимущества: можно использовать сложные геометрии из других программ (SolidWorks, FreeCAD)
     - Недостатки: нельзя редактировать геометрию в Gmsh
    """)

elif choice == "Замечание":
    st.write("""##### Замечание""")

    st.write("""
     - Классический метод полезен для учебных целей и тонкого контроля
     - OpenCASCADE — оптимальный вариант для большинства задач
     - Импорт CAD хорош, если у вас уже есть готовая модель
    """)