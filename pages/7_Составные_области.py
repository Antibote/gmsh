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

st.set_page_config(page_title="⬜🟦🟥", layout="wide")

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
        st.error(f"Команда Compound не поддерживается")
sections = {
    "Составные области": "",
    "Пример": "",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
if choice == "Составные области":

    st.write("""##### Составные области""")
    st.write(
        """
        **Составные области в Gmsh** — это способ объединения нескольких геометрических объектов (линий, поверхностей или объемов) в единый составной объект. 
        Это позволяет упростить работу с сложными геометриями и улучшить качество сетки 
            
        Основным способом логического объединения объектов для назначения материальных свойств, граничных условий и экспорта меток в решатели являются команды объединения в физические группы(Physical groups). 
        Для управления генерацией стеки используются команды `Compound Curve`, `Compound Surface`, `Compound Volume`. 
        Они указывают Gmsh рассматривать группу объектов как единое целое при построении сетки
        """)

    st.write("""###### Команды Compound""")

    st.write("Объединяет линии (отрезки, дуги, сплайны) в единую логическую кривую")

    st.write("Объединяет поверхности в группу")

    st.write("Объединяет объемы в логическую группу")

    st.write("""Когда задаются команды `Compound Curve`, `Compound Surface` при генерации сетки осуществляется следующая последовательность операций
        """)
    st.write("""
        - Для каждого элементарного базового геометрического объекта формируется сетка 
        - Создается дискретный объект, объединяющий все отдельные сетки
        - Вычисляется дискретная параметризация (т. е. кусочно-линейное отображение) на этот дискретный объект  
        - Формируется сетка дискретного объекта с использованием этой дискретной параметризации вместо базового геометрического описания базовых элементарных объектов, составляющих соединение 
        """)
               
    st.write("""Таким образом, операции `Compound` осуществляют логическое объединение для управления сеткой, при этом не сохраняются в файле `.msh` как отдельные сущности
    """)
    st.write("""###### Булевы операции в Gmsh""")

    st.write("Создает объект, объединяющий два или более исходных объекта")

    st.write("Удаляет из первого объекта все части, пересекающиеся со вторым объектом")

    st.write("Оставляет только область пересечения объектов")

    st.write("Разбивает объекты на общие и уникальные части")

elif choice == "Пример":
    st.write("""##### Пример""")
    geo_code_07 = """
    SetFactory("OpenCASCADE");

    // Создаем два куба
    Box(1) = {0, 0, 0, 1, 1, 1};
    Box(2) = {1, 0, 0, 1, 1, 1};

    // Объединяем их через BooleanUnion
    BooleanUnion(3) = {Volume{1}; Delete;} {Volume{2}; Delete;};

    // Назначаем физическую группу на результат
    Physical Volume("Merged_Volumes") = {3};

    // Объединяем границы для сетки
    Compound Surface(200) = {1, 2, 5, 6}; // Внешние грани
    Physical Surface("External_Walls") = {Surface{:}};
                
    Mesh.CharacteristicLengthMin = 0.2;
    Mesh 3;
    """
    show_code(geo_code_07,"python")

    def save_example_file():
        example_file_path = './example.geo'
        with open(example_file_path, 'w') as f:
            f.write(geo_code_07)
        return example_file_path

    # Кнопка для загрузки и запуска примера
    ##if st.button("Пример "):
        example_file_path = save_example_file()
        run_gmsh(example_file_path)