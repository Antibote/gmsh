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
st.set_page_config(page_title="🗓", layout="wide")

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
    "Библиотека Python pygmsh": "",
    "Что такое meshio?": "",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))
    

if choice == "Библиотека Python pygmsh":
    st.write("""##### Библиотека Python pygmsh""")
    st.write("""
    `pygmsh` — это Python-интерфейс для работы с `gmsh`, популярной open-source программой для генерации сеток.
    Он позволяет создавать геометрии и генерировать сетки с использованием Python, что делает процесс более гибким и интегрируемым.
    """)

    # Основные возможности
    st.markdown("###### Основные возможности `pygmsh`")
    st.write("""
    - Создание геометрий: точки, линии, поверхности, объемы.
    - Генерация сеток: 1D, 2D, 3D.
    - Поддержка булевых операций: объединение, вычитание, пересечение.
    - Экспорт сеток в форматы `.msh`, `.vtk`, `.stl` и другие.
    - Интеграция с Python-библиотеками: `numpy`, `scipy`, `matplotlib`, `meshio`.
    """)

    # Раскрывающийся список для каждой функции
    with st.expander("1. Точки"):
        st.write("""
        - **`add_point()`**: добавляет точку в геометрию. Параметры: координаты `[x, y, z]` и опционально **`mesh_size`** (размер элемента сетки).
        """)
        st.code("""
        p1 = geom.add_point([0.0, 0.0, 0.0], mesh_size=0.1)
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Point(1) = {0.0, 0.0, 0.0, 0.1};
        """, language="python")

    with st.expander("2. Линии"):
        st.write("""
        - **`add_line()`**: создает линию между двумя точками. **`add_circle_arc()`**: создает дугу окружности.
        """)
        st.code("""
        l1 = geom.add_line(p1, p2)
        arc = geom.add_circle_arc(p1, p2, p3)
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Line(1) = {1, 2};
        Circle(1) = {1, 2, 3};
        """, language="python")

    with st.expander("3. Кривые и контуры"):
        st.write("""
        - **`add_curve_loop()`**: создает замкнутый контур из линий или кривых.
        """)
        st.code("""
        loop = geom.add_curve_loop([l1, l2, l3, l4])
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Curve Loop(1) = {1, 2, 3, 4};
        """, language="python")

    with st.expander("4. Поверхности"):
        st.write("""
        - **`add_plane_surface()`**: создает плоскую поверхность внутри замкнутого контура.
        """)
        st.code("""
        surface = geom.add_plane_surface(loop)
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Plane Surface(1) = {1};
        """, language="python")

    with st.expander("5. Объемы"):
        st.write("""
        - **`add_volume()`**: создает объем на основе поверхностей.
        """)
        st.code("""
        volume = geom.add_volume([surface1, surface2])
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Volume(1) = {1, 2};
        """, language="python")

    with st.expander("6. Булевы операции"):
        st.write("""
        - **`boolean_union()`**: объединяет объекты.

        - **`boolean_difference()`**: вычитает один объект из другого.

        - **`boolean_intersection()`**: находит пересечение объектов.
        """)
        st.code("""
        result = geom.boolean_union([obj1, obj2])
        result = geom.boolean_difference(obj1, obj2)
        result = geom.boolean_intersection([obj1, obj2])
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        BooleanUnion{ Surface{1}; Delete; }{ Surface{2}; Delete; }
        BooleanDifference{ Surface{1}; Delete; }{ Surface{2}; Delete; }
        BooleanIntersection{ Surface{1}; Delete; }{ Surface{2}; Delete; }
        """, language="python")

    with st.expander("7. Физические группы"):
        st.write("""
        - **`add_physical_group()`**: группирует объекты для задания физических свойств.
        """)
        st.code("""
        phys_group = geom.add_physical_group("Line", [l1, l2])
        """, language="python")

        st.write("""- Аналог в **gmsh**""")

        st.code("""
        Physical Line(1) = {1, 2};
    """, language="python")
    def run_python_script_1():
        result = subprocess.run(['python3', './p_example.py'], capture_output=True, text=True)

        

    # Кнопка для запуска скрипта
    if st.button('Запустить пример'):
        output = run_python_script_1()


# elif choice == "Сравнение pygmsh и gmsh":
#
#     # Сравнение с `gmsh`
#     st.markdown("##### Сравнение `pygmsh` и `gmsh`")
#     st.write("""
#     | Характеристика               | `pygmsh`                                                                 | `gmsh`                                                                 |
#     |------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
#     | **Интерфейс**                | Python-интерфейс, удобен для интеграции с Python-библиотеками.           | Собственный скриптовый язык (.geo файлы) и графический интерфейс.      |
#     | **Гибкость**                 | Высокая, благодаря использованию Python.                                 | Ограничена синтаксисом .geo файлов.                                    |
#     | **Создание сложных геометрий**| Удобно использовать циклы и условия Python.                             | Требуется ручное описание в .geo файлах.                               |
#     | **Интеграция с другими инструментами** | Легко интегрируется с `numpy`, `scipy`, `matplotlib`, `meshio`.      | Требуется экспорт/импорт данных.                                       |
#     | **Поддержка форматов**       | Поддерживает экспорт в `.msh`, `.vtk`, `.stl` и другие.                 | Поддерживает множество форматов, включая `.msh`, `.stl`, `.step`.      |
#     | **Производительность**       | Немного медленнее из-за Python-обертки.                                 | Высокая, так как это нативный C++ код.                                 |
#     """)

elif choice == "Что такое meshio?":
    st.markdown("##### Что такое `meshio`?")
    st.write("""
    `meshio` — это библиотека для работы с файлами сеток (mesh files) в Python. Она предоставляет унифицированный интерфейс для чтения, записи и обработки сеток в различных форматах, таких как `.msh`, `.vtk`, `.stl`, `.xdmf` и многих других.
    """)

    # Основные возможности
    st.markdown("##### Основные возможности `meshio`")
    st.write("""
    - **Чтение и запись сеток**: поддержка более 30 форматов.
    - **Унифицированная структура данных**: точки, ячейки и данные.
    - **Поддержка различных типов ячеек**: треугольники, тетраэдры, линии и другие.
    - **Обработка данных**: добавление, удаление или изменение данных.
    - **Конвертация между форматами**: упрощает преобразование сеток.
    - **Интеграция с другими библиотеками**: `numpy`, `scipy`, `matplotlib`, `pyvista`.
    """)

    # Поддерживаемые форматы
    st.markdown("##### Поддерживаемые форматы")
    st.write("""
    `meshio` поддерживает множество форматов, включая:
    - **Gmsh**: `.msh`
    - **VTK**: `.vtk`, `.vtu`
    - **STL**: `.stl`
    - **XDMF**: `.xdmf`, `.xmf`
    - **OBJ**: `.obj`
    - **OFF**: `.off`
    - **PLY**: `.ply`
    - **ABAQUS**: `.inp`
    - **ANSYS**: `.cdb`
    - **и многие другие**.
    """)
